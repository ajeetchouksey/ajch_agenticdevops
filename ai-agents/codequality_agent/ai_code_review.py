

# AI Code Review Script for GitHub PRs
#
# SECURITY NOTE: All code improvements and additions must not bypass existing security checks or introduce new vulnerabilities. 
# Ensure secure handling of dynamic content and input validation to mitigate security threats (e.g., SQL injection, XSS).
#
# TEST COVERAGE: Ensure comprehensive test coverage for new features or changes, including integration with automated test pipelines (CI/CD) for dynamic and security testing.
#
# DOCUMENTATION: Any change to the AI agent's behavior (especially in identifying critical issues, including non-code recommendations) must be documented for clarity and team alignment.
#
# NOTE: Unit tests should be added to cover error handling and output formatting logic for robustness.

"""
This script fetches pull request diffs, sends them to an AI model for review, and posts suggestions as comments on the PR.
You need a GitHub token and an AI API key (e.g., Azure OpenAI, OpenAI, etc.).

Security Best Practices:
- Do not bypass or weaken security checks in any code changes.
- Validate and sanitize all dynamic content and user input.
- Review for vulnerabilities (e.g., SQL injection, XSS) in all PRs.

Test Coverage:
- Add/maintain unit and integration tests for all new features and changes.
- Ensure CI/CD pipelines run automated tests, including security tests.

AI Agent Behavior Documentation:
- Document any changes to how the AI agent identifies and reports critical or general issues, especially for non-code/process recommendations.
- Keep documentation up to date for team and user clarity.

Error Handling & Credential Validation:
- The script now checks for required environment variables (GITHUB_TOKEN, AI_API_KEY) before proceeding and exits with a clear error if missing.
- Error handling is implemented for network/API failures and is documented here for maintainability and troubleshooting.
"""

import os
import requests


import sys

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')  # e.g., 'owner/repo'
PR_NUMBER = os.getenv('PR_NUMBER')
AI_API_KEY = os.getenv('AI_API_KEY')
AI_API_URL = os.getenv('AI_API_URL')  # e.g., Azure OpenAI endpoint

# Explicitly check for required credentials
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable is not set.")
    sys.exit(1)
if not AI_API_KEY:
    print("Error: AI_API_KEY environment variable is not set.")
    sys.exit(1)

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def get_pr_diff():
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/pulls/{PR_NUMBER}"
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        pr = r.json()
        diff_url = pr['diff_url']
        diff_resp = requests.get(diff_url, headers=headers)
        diff_resp.raise_for_status()
        diff = diff_resp.text
        return diff
    except requests.RequestException as e:
        print(f"Error fetching PR diff: {e}")
        return None

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
    if diff is None:
        return "**Error:** Unable to fetch PR diff. Please check the logs."
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": diff}
        ]
    }
    try:
        response = requests.post(
            AI_API_URL,
            headers={"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"},
            json=payload
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.RequestException as e:
        print(f"Error calling AI API: {e}")
        return "**Error:** Unable to get AI review. Please check the logs."

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
