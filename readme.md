https://github-repo-analyzer-s4vj.onrender.com
# 📊 GitHub Repo Analyzer

A simple Python script to fetch and display basic statistics for any public GitHub repository: **stars**, **forks**, and **open issues**. You can export the results to either **JSON** or **CSV** format.

---

## 🚀 Features

- Fetch GitHub repo stats using the GitHub API
- Export data to JSON or CSV
- Simple and lightweight

---

## 📦 Requirements

- Python 3.6+
- `requests` library

Install dependencies:

```bash
pip install -r requirements.txt

#usage
python github_analyzer.py <owner> <repo> [json|csv]
<owner>: GitHub username or organization

<repo>: Repository name

[json|csv]: (Optional) Output format. Default is json.

#example
python github_analyzer.py octocat Hello-World json

This will create output.json with the following structure:
{
    "full_name": "octocat/Hello-World",
    "stars": 1800,
    "forks": 1600,
    "open_issues": 42
}
## 📝 License

This project is licensed under the [MIT License](LICENSE).
 #ignore this plss
 cd .\github-repo-analyzer\

