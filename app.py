from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_repo_stats(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, f"Repo Error: {response.status_code} - {response.json().get('message', '')}"
    data = response.json()
    return {
        "repo_full_name": data["full_name"],
        "description": data.get("description"),
        "default_branch": data["default_branch"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "watchers": data["watchers_count"],
        "license": data["license"]["name"] if data["license"] else None,
        "repo_created_at": data["created_at"],
        "repo_updated_at": data["updated_at"],
        "size_kb": data["size"],
        "topics": ', '.join(data.get("topics", []))
    }, None

def fetch_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, f"User Error: {response.status_code} - {response.json().get('message', '')}"
    data = response.json()
    return {
        "username": data["login"],
        "name": data.get("name"),
        "public_repos": data["public_repos"],
        "followers": data["followers"],
        "following": data["following"],
        "user_created_at": data["created_at"],
        "bio": data.get("bio"),
        "location": data.get("location"),
        "company": data.get("company")
    }, None

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        owner = request.form.get("owner")
        repo = request.form.get("repo")

        user_info, user_error = fetch_user_info(owner)
        repo_stats, repo_error = fetch_repo_stats(owner, repo)

        if user_error:
            error = user_error
        elif repo_error:
            error = repo_error
        else:
            result = {**user_info, **repo_stats}
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    print("✅ Flask app is starting...")
    app.run(debug=True)

