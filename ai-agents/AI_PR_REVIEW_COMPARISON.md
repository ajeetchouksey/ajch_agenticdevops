# AI PR Review vs GitHub Copilot PR Review

This document explains the differences between the custom AI PR Review agent in this repository and GitHub Copilot's PR review features.

---

## AI PR Review Agent (Custom)
- **Location:** `ai-agents/codequality_agent/ai_code_review.py`
- **How it works:**
  - Fetches pull request diffs from GitHub.
  - Sends the diff to an AI model (e.g., Azure OpenAI, OpenAI API).
  - The AI reviews only the changes in the PR and organizes suggestions into 'Critical' and 'General' categories.
  - Posts a formatted review comment directly on the PR.
- **Customization:**
  - You control the prompt, review style, and which AI model is used.
  - Can be integrated into CI/CD or run manually.
- **Use cases:**
  - Enforce custom review standards.
  - Use private or organization-specific AI models.
  - Add organization-specific review logic or formatting.

## GitHub Copilot PR Review
- **How it works:**
  - GitHub Copilot (and Copilot for PRs) uses OpenAI models to suggest code changes and review pull requests directly in the GitHub UI.
  - Provides inline suggestions, explanations, and can summarize PRs.
  - Integrated natively with GitHub and requires a Copilot subscription.
- **Customization:**
  - Limited; you cannot change the underlying prompt or model.
  - Review style and output are determined by GitHub's implementation.
- **Use cases:**
  - Quick, out-of-the-box AI review for any PR on GitHub.
  - Useful for individual developers and teams using GitHub's web interface.

---

## Summary Table

| Feature                | AI PR Review Agent (Custom) | GitHub Copilot PR Review |
|------------------------|-----------------------------|--------------------------|
| Model Choice           | Any (OpenAI, Azure, etc.)   | OpenAI (GitHub managed)  |
| Custom Prompts         | Yes                         | No                       |
| Integration            | Script/CI/CD                | GitHub UI                |
| Review Categories      | Critical/General            | General suggestions      |
| Formatting             | Fully customizable          | GitHub default           |
| Cost                   | Your AI usage               | Copilot subscription     |

---

Choose the custom AI PR Review agent if you need full control, custom logic, or want to use your own AI models. Use GitHub Copilot PR Review for convenience and seamless GitHub integration.
