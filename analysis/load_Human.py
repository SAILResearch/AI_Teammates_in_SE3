import pandas as pd
import requests
import re
from tqdm import tqdm
import dotenv
import os

dotenv.load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

pd.set_option('display.max_columns', None)

def run_query(query, variables):
    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    
    response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    if "errors" in data:
        raise Exception(data["errors"])
    return data["data"]

def parse_pr_url(url):
    match = re.search(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)", url)
    if match:
        return match.group(1), match.group(2), int(match.group(3))
    return None, None, None

PR_QUERY = """
query($owner: String!, $repo: String!, $number: Int!) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $number) {
      number
      additions
      deletions
      changedFiles

      commits { totalCount }
      comments { totalCount }

      reviews(first: 100) {
        totalCount
        nodes {
          author {
            login
          }
        }
      }

      reviewRequests(first: 100) {
        nodes {
          requestedReviewer {
            __typename
            ... on User { login }
            ... on Team { name }
            ... on Mannequin { login }
            ... on Bot { login }
          }
        }
      }
    }
  }
}
"""

def get_pr_stats(url):
    owner, repo, number = parse_pr_url(url)

    if owner is None:
        return {
            "additions": None,
            "deletions": None,
            "changed_files": None,
            "commit_count": None,
            "review_count": None,
            "comment_count": None,
            "assigned_reviewers": None
        }

    variables = {"owner": owner, "repo": repo, "number": number}

    try:
        data = run_query(PR_QUERY, variables)
        pr = data["repository"]["pullRequest"]

        reviewers = [
            r["requestedReviewer"]["login"]
            for r in pr["reviewRequests"]["nodes"]
            if r["requestedReviewer"] is not None
        ]

        return {
            "additions": pr["additions"],
            "deletions": pr["deletions"],
            "changed_files": pr["changedFiles"],
            "commit_count": pr["commits"]["totalCount"],
            "review_count": pr["reviews"]["totalCount"],
            "comment_count": pr["comments"]["totalCount"],
            "assigned_reviewers": reviewers,
        }

    except Exception as e:
        print("ERROR for PR:", url)
        print(e)
        return {
            "additions": None,
            "deletions": None,
            "changed_files": None,
            "commit_count": None,
            "review_count": None,
            "comment_count": None,
            "assigned_reviewers": None
        }

def enrich_df_with_pr_stats(df, url_column="html_url"):
    results = []

    for _, row in tqdm(df.iterrows(), total=len(df)):
        url = row[url_column]
        stats = get_pr_stats(url)
        results.append(stats)

    stats_df = pd.DataFrame(results)
    enriched = pd.concat([df.reset_index(drop=True), stats_df], axis=1)
    return enriched

if __name__ == "__main__":
    human_pr_df = pd.read_parquet("hf://datasets/hao-li/AIDev/human_pull_request.parquet")
    limited_df = human_pr_df.head(15)  # For testing, limit to first 5 rows
    
    enriched = enrich_df_with_pr_stats(limited_df, url_column="html_url")
    print(enriched)
