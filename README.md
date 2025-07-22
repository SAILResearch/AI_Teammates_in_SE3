# The Rise of AI Teammates in Software Engineering (SE) 3.0: Replication Package

This repository contains the replication package for the paper "The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping SE". The package includes all datasets, analysis scripts, and generated figures used in the research.

## Overview

This study analyzes the impact of AI coding agents on software engineering practices by examining pull requests (PRs) from various AI teammates including GitHub Copilot, Cursor, Devin, Claude Code, and OpenAI Codex, compared against human developers. The research provides insights into productivity patterns, code quality, and collaboration dynamics in the era of AI-assisted software development.

## Repository Structure

```
├── AIDev-pop/              # Main dataset organized by AI agent
│   ├── Claude_Code/        # Data for Claude Code agent (101 PRs, 68 developers, 61 repos)
│   ├── Copilot/           # Data for GitHub Copilot (1,462 PRs, 1 developer, 215 repos)
│   ├── Cursor/            # Data for Cursor agent (144 PRs, 66 developers, 52 repos)
│   ├── Devin/             # Data for Devin agent (2,729 PRs, 1 developer, 130 repos)
│   ├── Human/             # Human developer baseline (6,628 PRs, 2,515 developers, 818 repos)
│   ├── OpenAI_Codex/      # Data for OpenAI Codex (2,686 PRs, 522 developers, 467 repos)
│   └── summary_scope.csv   # Summary statistics across all agents
├── analysis/              # Analysis scripts and Jupyter notebooks
│   ├── dataset_overview.ipynb    # Dataset overview and basic statistics
│   ├── helper.py                 # Shared utility functions
│   ├── language_usage.ipynb     # Programming language usage analysis
│   ├── productivity.ipynb       # Productivity metrics analysis
│   └── reviewers.ipynb          # Code review patterns analysis
├── figs/                  # Generated figures and results
│   ├── pr_cumulative.png              # Cumulative PR trends
│   ├── pr_cumulative_popular.png      # Popular repositories PR trends
│   ├── pr_merge_compare_radar.png     # Comparative merge rate analysis
│   ├── total_language_percentages_top.png  # Language usage distribution
│   ├── turnaround_distribution.png    # PR turnaround time analysis
│   ├── turnaround_enhanced.csv       # Enhanced turnaround data
│   └── turnaround_enhanced.tex       # LaTeX table for turnaround results
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Dataset Description

### Data Organization

Each AI agent directory contains standardized CSV files with the following structure:

- **`prs.csv`**: Pull request metadata (title, description, state, merge status, timestamps)
- **`pr_commits.csv`**: Commit information for each PR (SHA, message, author, timestamp)
- **`pr_comments.csv`**: Comments on pull requests (author, content, timestamp)
- **`pr_reviews.csv`**: Code review data (reviewer, state, comments)
- **`issues.csv`**: Related GitHub issues (title, description, labels, state)
- **`issue_timelines.csv`**: Issue lifecycle events and timestamps
- **`pr_timelines.csv`**: PR lifecycle events and timestamps
- **`related_issues.csv`**: Links between PRs and issues
- **`post_pr_issues.csv`**: Issues created after PR merges
- **`repo_metadata.csv`**: Repository information (name, description, language, stars)
- **`developer_metadata.csv`**: Developer profile information (available for AI agents)
- **`gpt_conventional_commits.csv`**: GPT-classified conventional commit types
- **`prs_without_issues.csv`**: PRs not linked to issues (available for AI agents)

### Summary Statistics

| Agent        | PRs   | % Open | % Closed | % Merged | Developers | Repositories |
|--------------|-------|--------|----------|----------|------------|--------------|
| Claude_Code  | 101   | 14.9%  | 32.7%    | 52.5%    | 68         | 61           |
| Copilot      | 1,462 | 29.7%  | 32.1%    | 38.2%    | 1          | 215          |
| Cursor       | 144   | 27.1%  | 21.5%    | 51.4%    | 66         | 52           |
| Devin        | 2,729 | 2.6%   | 48.4%    | 48.9%    | 1          | 130          |
| Human        | 6,628 | 7.1%   | 16.2%    | 76.7%    | 2,515      | 818          |
| OpenAI_Codex | 2,686 | 13.4%  | 21.3%    | 65.3%    | 522        | 467          |

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/SAILResearch/AI_Teammates_in_SE3.git
cd AI_Teammates_in_SE3
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Additional Data

Download the complete AIDev dataset from [Google Drive](https://drive.google.com/file/d/12HYEa_4aEsCSi8Q1X-TkOHPiNUJW9FBF/view?usp=sharing) if you need access to the full raw data beyond what's included in this repository.

## Usage

### Running the Analysis

The analysis is organized into Jupyter notebooks that can be run independently:

1. **Dataset Overview**:
```bash
jupyter notebook analysis/dataset_overview.ipynb
```

2. **Language Usage Analysis**:
```bash
jupyter notebook analysis/language_usage.ipynb
```

3. **Productivity Metrics**:
```bash
jupyter notebook analysis/productivity.ipynb
```

4. **Code Review Patterns**:
```bash
jupyter notebook analysis/reviewers.ipynb
```

### Using Helper Functions

The `analysis/helper.py` module provides utility functions for data loading and statistical analysis:

```python
from analysis.helper import *

# Example usage in your own scripts
import pandas as pd
from pathlib import Path

# Load data for a specific agent
agent_data = load_agent_data('Copilot')
```

### Reproducing Figures

All figures in the `figs/` directory can be regenerated by running the corresponding analysis notebooks. The notebooks include both the analysis code and the figure generation logic.

## Data Format and Schema

### Pull Request Data Schema

Key columns in `prs.csv`:
- `id`: Unique PR identifier
- `title`: PR title
- `state`: open/closed/merged
- `created_at`: PR creation timestamp
- `merged_at`: PR merge timestamp (if applicable)
- `repository`: Repository name
- `author`: PR author

### Commit Data Schema

Key columns in `pr_commits.csv`:
- `pr_id`: Associated PR identifier
- `sha`: Commit SHA
- `message`: Commit message
- `author_date`: Commit author timestamp
- `files_changed`: Number of files modified

## Research Applications

This dataset enables research in several areas:

1. **AI Agent Productivity Analysis**: Compare merge rates, turnaround times, and development patterns
2. **Code Quality Assessment**: Analyze commit patterns, review feedback, and issue resolution
3. **Collaboration Dynamics**: Study interaction patterns between AI agents and human developers
4. **Programming Language Trends**: Examine language preferences across different AI systems
5. **Repository Impact**: Assess how AI contributions affect project health and maintainability

## Citation

If you use this dataset or code in your research, please cite our paper:

```bibtex
@article{ai_teammates_se3_2024,
  title={The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping SE},
  author={[Authors will be added upon publication]},
  journal={[Journal will be added upon publication]},
  year={2024}
}
```

## Contributing

We welcome contributions to improve the analysis scripts or extend the dataset. Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request with a clear description

## License

This project is released under the terms specified in the research paper. Please refer to the paper for licensing information regarding data usage and redistribution.

## Contact

For questions about the dataset or analysis, please open an issue in this repository or contact the authors through the channels provided in the research paper.

## Acknowledgments

We thank the open-source community and the developers of the AI coding tools studied in this research for making this analysis possible.