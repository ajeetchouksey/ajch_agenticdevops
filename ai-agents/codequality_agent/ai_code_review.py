# AI Code Review Script for GitHub PRs

"""
This script fetches pull request diffs, sends them to an AI model for review, and posts suggestions as comments on the PR.
You need a GitHub token and an AI API key (e.g., Azure OpenAI, OpenAI, etc.).
"""

import os
import requests

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')  # e.g., 'owner/repo'
PR_NUMBER = os.getenv('PR_NUMBER')
AI_API_KEY = os.getenv('AI_API_KEY')
AI_API_URL = os.getenv('AI_API_URL')  # e.g., Azure OpenAI endpoint

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def get_pr_diff():
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/pulls/{PR_NUMBER}"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    pr = r.json()
    diff_url = pr['diff_url']
    diff = requests.get(diff_url, headers=headers).text
    return diff

def ai_review(diff):
    # Example for OpenAI-compatible API
    prompt = (
        "You are an expert code reviewer and DevOps advisor. Only comment on the changes in this PR diff. "
        "Organize your suggestions into two main categories: 'Critical' (must-fix, security, compliance, correctness, or process blockers) and 'General' (style, maintainability, documentation, test coverage, process, or minor improvements). "
        "For each category, provide both code-related and non-code-related recommendations. Non-code recommendations may include process, documentation, test coverage, CI/CD, or other DevOps best practices. "
        "Make all suggestions highly visible using markdown headings, emojis, and clear separation. "
        "Output your suggestions in the following format:\n"
        "<details><summary>🚀 <b>AI PR Review Suggestions (click to expand)</b></summary>\n\n"
        "### 🛑 Critical Recommendations\n"
        "#### Code Issues\n"
        "- ...\n"
        "\n#### Other Critical Issues (Process, Docs, Tests, etc.)\n"
        "- ...\n"
        "\n### ✨ General Recommendations\n"
        "#### Code Suggestions\n"
        "- ...\n"
        "\n#### Other General Suggestions (Process, Docs, Tests, etc.)\n"
        "- ...\n"
        "</details>\n\n"
        "At the end, show a clear, visually highlighted heading: '### ✅ Recommended for approval: Yes' or '### ❌ Recommended for approval: No' based on your review. "
        "If there are no Critical issues, recommend approval."
    )
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": diff}
        ]
    }
    response = requests.post(
        AI_API_URL,
        headers={"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"},
        json=payload
    )
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

def post_pr_comment(body):
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/issues/{PR_NUMBER}/comments"
    r = requests.post(url, headers=headers, json={"body": body})
    r.raise_for_status()
    return r.json()

def main():
    diff = get_pr_diff()
    review = ai_review(diff)
    # Make the review section even more visible and clarify the heading
    comment = (
        "---\n"
        "## 🚀 <span style='color:#2b6cb0'>AI Code Improvement Suggestions as PR review by AI Agent</span>\n"
        "---\n\n"
        f"{review}"
    )
    post_pr_comment(comment)

if __name__ == "__main__":
    main()
