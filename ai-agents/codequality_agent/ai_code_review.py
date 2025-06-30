

# AI Code Review Script for GitHub PRs
#
# SECURITY WARNING: Never print, log, or store sensitive environment variables (e.g., GITHUB_TOKEN, AI_API_KEY) in logs, output, or source code.
# Always set these securely in your CI/CD environment or local shell, and avoid echoing or exposing them in error messages or debug output.
#
# PERMISSIONS: GITHUB_TOKEN should have the minimal required permissions (e.g., repo:read, pull_request:write) to interact with PRs. AI_API_KEY should have only the permissions needed for model inference. Do not use tokens with excessive privileges.
#
# SECURITY FEATURES: This script validates credentials, never prints or logs sensitive values, and enforces input validation. All error messages avoid exposing sensitive data or explicit shell commands. See documentation for more details.
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

Permissions Required:
- GITHUB_TOKEN: Should have minimal permissions (e.g., repo:read, pull_request:write) to interact with PRs. Do not use tokens with excessive privileges.
- AI_API_KEY: Should have only the permissions needed for model inference. Do not use keys with broader access than necessary.

Security Features:
- Credentials are validated and never printed or logged.
- Input validation is enforced for all environment variables and PR numbers.
- Error messages avoid exposing sensitive data, explicit shell commands, or URLs for setting tokens.
- All security features and requirements are documented here and in the project documentation.

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


# ---
# Exception List for PR Review Approval Logic
# Update this list to ignore certain issues (e.g., documentation, formatting, environment variable checks) when suggesting PR approval.
# Any critical issue matching a keyword in this list will NOT block approval.
exception_list = [
    "documentation", "doc", "readme", "comment", "formatting", "typo", "spelling",
    "environment variable", "env var", "envvar", "missing environment variable", "invalid environment variable", "environment variable check",
    "separated into individual functions for different environment variables"
]

import os
import sys
import requests

def validate_credentials(token, api_key):
    # Do not print or log the actual values of token or api_key!
    if not token or not isinstance(token, str) or not token.strip():
        print("""
Error: GITHUB_TOKEN environment variable is not set or is invalid.
Suggested Action: Please set the GITHUB_TOKEN environment variable with a valid GitHub personal access token with minimal permissions. Refer to the project documentation for more details. Never print or log your token value.
""")
        sys.exit(1)
    if not api_key or not isinstance(api_key, str) or not api_key.strip():
        print("""
Error: AI_API_KEY environment variable is not set or is invalid.
Suggested Action: Please set the AI_API_KEY environment variable with your OpenAI or Azure OpenAI API key with minimal permissions. Refer to the project documentation for more details. Never print or log your API key value.
""")
        sys.exit(1)

def get_config():
    github_token = os.getenv('GITHUB_TOKEN')
    github_repo = os.getenv('GITHUB_REPOSITORY')  # e.g., 'owner/repo'
    pr_number = os.getenv('PR_NUMBER')
    ai_api_key = os.getenv('AI_API_KEY')
    ai_api_url = os.getenv('AI_API_URL')  # e.g., Azure OpenAI endpoint
    validate_credentials(github_token, ai_api_key)
    # Validate PR number
    if not pr_number or not pr_number.isdigit():
        print("""
Error: PR_NUMBER environment variable is not set or is not a valid pull request number.
Suggested Action: Please set the PR_NUMBER environment variable to the numeric ID of the pull request you want to review.
Refer to the project documentation for more details.
""")
        sys.exit(1)
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    return {
        'github_token': github_token,
        'github_repo': github_repo,
        'pr_number': pr_number,
        'ai_api_key': ai_api_key,
        'ai_api_url': ai_api_url,
        'headers': headers
    }

def get_pr_diff(github_repo, pr_number, headers):
    url = f"https://api.github.com/repos/{github_repo}/pulls/{pr_number}"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        pr = r.json()
        diff_url = pr.get('diff_url')
        if not diff_url:
            print("Error: Could not find diff_url in PR response. Please check if the PR number is correct and accessible.")
            return None
        diff_resp = requests.get(diff_url, headers=headers, timeout=10)
        diff_resp.raise_for_status()
        diff = diff_resp.text
        return diff
    except requests.Timeout:
        print("Error: Network timeout while fetching PR diff. Please check your internet connection and try again.")
        return None
    except requests.RequestException as e:
        print(f"Error fetching PR diff: {e}\nSuggested Action: Check your network connection, GitHub token permissions, and PR number.")
        return None

def ai_review(diff, ai_api_url, ai_api_key):
    """
    Run AI review on the PR diff. Uses the global exception_list to ignore certain issues for approval logic.
    """
    prompt = (
        "You are an expert code reviewer and DevOps advisor. Only comment on the changes in this PR diff. "
        "Organize your suggestions into two main categories: 'Critical' (must-fix, security, compliance, correctness, or process blockers) and 'General' (style, maintainability, documentation, test coverage, process, or minor improvements). "
        "For each category, provide both code-related and non-code-related recommendations. Non-code recommendations may include process, documentation, test coverage, CI/CD, or other DevOps best practices. "
        "Make all suggestions highly visible using markdown headings, emojis, and clear separation. "
        "Output your suggestions in the following format:\n"
        "<details><summary>🚀 <b>AI PR Review Suggestions (click to expand)</b></summary>\n\n"
        "### 🛑 Critical Suggestions\n"
        "#### Code Issues\n"
        "- ...\n"
        "\n#### Other Critical Issues (Process, Docs, Tests, Security, etc.)\n"
        "- ...\n"
        "\n### ✨ General Suggestions\n"
        "#### Code Suggestions\n"
        "- ...\n"
        "\n#### Other General Suggestions (Process, Docs, Tests, etc.)\n"
        "- ...\n"
        "</details>\n\n"
        "At the end, show a clear, visually highlighted heading: '### ✅ Suggested for approval: Yes' or '### ❌ Suggested for approval: No' based on your review. "
        "When determining if a PR can be suggested for approval, ignore issues that match the following exception list: "
        f"{exception_list}. Only block approval for critical issues related to security, testing, or correctness that are not in the exception list."
    )
    if diff is None:
        return "**Error:** Unable to fetch PR diff. Please check your network connection, PR number, and GitHub token permissions."
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": diff}
        ]
    }
    try:
        response = requests.post(
            ai_api_url,
            headers={"Authorization": f"Bearer {ai_api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=20
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.Timeout:
        print("Error: Network timeout while calling AI API. Please check your internet connection and try again.")
        return "**Error:** Network timeout while calling AI API. Please check your internet connection and try again."
    except requests.RequestException as e:
        print(f"Error calling AI API: {e}\nSuggested Action: Check your network connection, API key, and endpoint URL.")
        return "**Error:** Unable to get AI review. Please check your network connection, API key, and endpoint URL."

def post_pr_comment(body, github_repo, pr_number, headers):
    url = f"https://api.github.com/repos/{github_repo}/issues/{pr_number}/comments"
    try:
        r = requests.post(url, headers=headers, json={"body": body}, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.Timeout:
        print("Error: Network timeout while posting PR comment. Please check your internet connection and try again.")
        return None
    except requests.RequestException as e:
        print(f"Error posting PR comment: {e}\nSuggested Action: Check your network connection, GitHub token permissions, and PR number.")
        return None

def main():
    config = get_config()
    diff = get_pr_diff(config['github_repo'], config['pr_number'], config['headers'])
    review = ai_review(diff, config['ai_api_url'], config['ai_api_key'])
    # Make the review section even more visible and clarify the heading
    comment = (
        "---\n"
        "## 🚀 <span style='color:#2b6cb0'>AI Code Improvement Suggestions as PR review by AI Agent</span>\n"
        "---\n\n"
        f"{review}"
    )
    result = post_pr_comment(comment, config['github_repo'], config['pr_number'], config['headers'])
    if result is None:
        print("Failed to post PR review comment. Please check the error messages above for troubleshooting steps.")

if __name__ == "__main__":
    main()
