"""Shared helper functions for this project."""

from __future__ import annotations

import json
import pathlib
from typing import Any

from scipy import stats

from cliffs_delta import cliffs_delta


ROOT_DIR = pathlib.Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
CLEAN_DIR = ROOT_DIR / "clean_data"
PR_DIR = DATA_DIR / "prs"
DEVELOPER_DIR = DATA_DIR / "developers"
COMMENTS_DIR = DATA_DIR / "pr_comments"
REVIEWS_DIR = DATA_DIR / "pr_reviews"
COMMITS_DIR = DATA_DIR / "pr_commits"
COMMIT_DETAILS_DIR = DATA_DIR / "commit_details"
TIMELINE_DIR = DATA_DIR / "pr_timelines"
ISSUE_TIMELINE_DIR = DATA_DIR / "issue_timelines"
DEV_REPO_PR_DIR = DATA_DIR / "dev_repo_prs"
ISSUES_DIR = DATA_DIR / "issues"
REPO_PR_DIR = pathlib.Path("/media/leo/LeoHarddisk/mining_data") / "repo_prs"
ANALYSIS_DIR = ROOT_DIR / "analysis"
CSV_DIR = ROOT_DIR / "AIDev"
FIG_DIR = ROOT_DIR / "figs"
PROJECT_META_DIR = DATA_DIR / "project_metadata"
PROJECT_META_RAW_DIR = DATA_DIR / "project_metadata_raw"
PROTOTYPE_DIR = DATA_DIR / "prototype"
SCOPE_DIR = ROOT_DIR / "AIDev-pop"

COLOR_MAP = {
    "Human": "#56B4E9",
    "OpenAI_Codex": "#D55E00",
    "OpenAI Codex": "#D55E00",
    "Codex": "#F0E442",
    "Devin": "#009E73",
    "Copilot": "#0072B2",
    "GitHub Copilot": "#0072B2",
    "Cursor": "#785EF0",
    "Claude_Code": "#DC267F",
    "Claude Code": "#DC267F",
}

NAME_MAPPING = {
    "OpenAI_Codex": "OpenAI Codex",
    "Codex": "OpenAI Codex",
    "Devin": "Devin",
    "Copilot": "GitHub Copilot",
    "Cursor": "Cursor",
    "Claude_Code": "Claude Code",
    "Claude": "Claude Code",
    "Human": "Human",
    "OpenAI Codex": "OpenAI Codex",
    "GitHub Copilot": "GitHub Copilot",
    "Claude Code": "Claude Code",
}
for key, value in NAME_MAPPING.items():
    if key not in COLOR_MAP:
        COLOR_MAP[key] = COLOR_MAP[value]

PREFER_ORDER = [
    "Human",
    "OpenAI_Codex",
    "Devin",
    "Copilot",
    "Cursor",
    "Claude_Code"
]

FLOW_ORDER = [
    "feat",  # new functionality
    "fix",  # bug fixes
    "perf",  # performance work
    "refactor",  # code reshaping
    "style",  # lint / formatting
    "docs",  # documentation
    "test",  # testing
    "chore",  # misc maintenance
    "build",  # packaging / build sys
    "ci",  # continuous-integration
    "other",  # continuous-integration
]


def save_json(data: Any, filepath: str | pathlib.Path, indent: int = 2) -> None:
    """Write *data* to *filepath* as JSON."""

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)


def read_json(filepath: str | pathlib.Path) -> Any:
    """Return JSON data loaded from *filepath*."""

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def filter_pr_df(df: "pd.DataFrame", agent: str) -> "pd.DataFrame":
    """Return *df* after applying agent-specific PR filters."""

    agent_key = agent.lower()

    if agent_key == "claude_code":
        mask = df["body"].str.contains("Co-Authored-By: Claude", case=False, na=False)
        return df.loc[mask]
    if agent_key == "copilot":
        mask = df["user"].str.lower() == "copilot"
        return df.loc[mask]
    return df


def mannUandCliffdelta(dist1, dist2):
    d, size = cliffs_delta(dist1, dist2)
    print(f"Cliff's delta: {size}, d={d}")
    u, p = stats.mannwhitneyu(dist1, dist2, alternative="two-sided")
    print(f"Mann-Whitney-U-test: u={u} p={p}")
    return u, p, d, size
