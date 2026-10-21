<p align="center">
  <img src="figs/aidev_logo.png" alt="Description" width="300"/>
</p>

# AIDev: Studying AI Coding Agents on GitHub (The Rise of AI Teammates in Software Engineering 3.0)

[![Paper](https://img.shields.io/badge/arXiv-2507.15003-b31b1b.svg)](https://arxiv.org/abs/2507.15003)
[![Paper](https://img.shields.io/badge/arXiv-2602.09185-b31b1b.svg)](https://arxiv.org/abs/2602.09185)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-dataset-blue?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/hao-li/AIDev)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16919272.svg)](https://doi.org/10.5281/zenodo.16919272)

> 📢 **The dataset, its documentation, and all announcements live on Hugging Face:**
> **https://huggingface.co/datasets/hao-li/AIDev**
>
> The dataset card there is the single source of truth for the latest release (currently
> **AIDev v5 / AIDev-7.6M**, cutoff March 31, 2026), per-agent statistics, the table
> schema, memory-safe loading instructions, how agent PRs are identified, the version
> history, and the open **calls for papers** (e.g., the AAAI-27 Workshop on Agentic
> Software Engineering, deadline November 20, 2026). This GitHub repository only hosts
> the example notebooks and the replication material for the papers.

- **Papers:**
  - [The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping Software Engineering](https://arxiv.org/abs/2507.15003)
  - [AIDev: Studying AI Coding Agents on GitHub](https://arxiv.org/abs/2602.09185)
- **Dataset (Hugging Face):** https://huggingface.co/datasets/hao-li/AIDev

## Quick Start

Each release is a git tag on the Hub (`v3`, `v4`, `v5`, ...), so pin the revision you use:

```py
import pandas as pd

all_repo_df = pd.read_parquet("hf://datasets/hao-li/AIDev@v5/all_repository.parquet")
all_user_df = pd.read_parquet("hf://datasets/hao-li/AIDev@v5/all_user.parquet")
```

> ⚠️ `all_pull_request.parquet` (~6.7 GB) and `pr_commit_details.parquet` (~12.4 GB) do not
> fit in a typical machine's RAM. Use the column/row-group patterns from the
> [dataset card](https://huggingface.co/datasets/hao-li/AIDev#loading-the-dataset-without-blowing-up-your-ram)
> or the [`scripts/`](https://huggingface.co/datasets/hao-li/AIDev/tree/v5/scripts) folder of the dataset.

## Example Notebooks

Updated for AIDev v5 (October 2026). Each notebook runs on Colab against
`hf://datasets/hao-li/AIDev@v5` and mirrors the memory-safe
[`scripts/`](https://huggingface.co/datasets/hao-li/AIDev/tree/v5/scripts) folder of the dataset.

| Description                          | Notebook Link                                                                                       | Open in Colab                                                                                                                |
|--------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Basic usage                          | [load_AIDev.ipynb](analysis/load_AIDev.ipynb)                                                       | <a href="https://colab.research.google.com/github/SAILResearch/AI_Teammates_in_SE3/blob/main/analysis/load_AIDev.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| Dataset overview                     | [dataset_overview.ipynb](analysis/dataset_overview.ipynb)                                           | <a href="https://colab.research.google.com/github/SAILResearch/AI_Teammates_in_SE3/blob/main/analysis/dataset_overview.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| Analysis of programming usage        | [language_usage.ipynb](analysis/language_usage.ipynb)                                               | <a href="https://colab.research.google.com/github/SAILResearch/AI_Teammates_in_SE3/blob/main/analysis/language_usage.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| PR merge rate and turnaround time    | [productivity.ipynb](analysis/productivity.ipynb)                                                   | <a href="https://colab.research.google.com/github/SAILResearch/AI_Teammates_in_SE3/blob/main/analysis/productivity.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |

To run them locally:

```bash
pip install -r requirements.txt
```

## Replication Material for the SE 3.0 Paper

The analyses in *The Rise of AI Teammates in Software Engineering 3.0* were run on the
August 2025 snapshot of AIDev (the `v3` tag on the Hub) and its **AIDev-pop** subset
(repositories with more than 100 stars). Numbers and figures in the paper therefore
refer to that snapshot, not to the current release.

- **Snapshot used in the paper:** https://huggingface.co/datasets/hao-li/AIDev/tree/v3
- **Raw AIDev-pop data:** https://drive.google.com/file/d/1l0_RjS7ZT0Y27V3mv0oJK-jfeRkhq5l5/view?usp=drive_link
- **PR task-type classification:** [`analysis/classify_pr.py`](analysis/classify_pr.py) produces the
  `pr_task_type` table (Conventional-Commit style labels). This table ships only with the `v3`
  release: `pd.read_parquet("hf://datasets/hao-li/AIDev@v3/pr_task_type.parquet")`.
- **Reviewer analysis:** [`analysis/reviewers.ipynb`](analysis/reviewers.ipynb) (written for the paper's snapshot).
- **Figures from the paper:** [`figs/`](figs/).

## Repository Structure

```
├── analysis/               # Example notebooks (v5) and paper replication scripts
├── figs/                   # Logo and figures from the paper
├── AIDev_preprint.pdf      # Preprint of the SE 3.0 paper
├── AIDev_Challenge.pdf     # MSR 2026 Mining Challenge paper (AIDev: Studying AI Coding Agents on GitHub)
├── requirements.txt        # Python dependencies for the notebooks
└── README.md               # This file
```

## Citation

If you use this dataset or code in your research, please cite our paper:

```bibtex
@misc{li2025aiteammates,
      title={The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping Software Engineering}, 
      author={Hao Li and Haoxiang Zhang and Ahmed E. Hassan},
      year={2025},
      eprint={2507.15003},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2507.15003}, 
}
```
