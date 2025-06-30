

# Agentic DevOps Playground

AgenticDevOps is a next-generation, modular DevOps automation framework for Azure. It empowers teams to deliver secure, high-quality software faster by combining Infrastructure as Code (Terraform) with intelligent, autonomous AI agents for code quality, security, and cost optimization. The result: modern, scalable, and compliant DevOps workflows that accelerate innovation and reduce manual toil.

---

## 📦 Latest Release Notes ([v0.0.1](https://github.com/ajeetchouksey/ajch_agenticdevops/releases/tag/v0.0.1))

### 🚀 AI PR Review Agent Highlights

- **Automated AI-Powered PR Review**: Fetches pull request diffs from GitHub, sends them to an AI model (OpenAI/Azure OpenAI), and posts structured, actionable review comments directly on the PR.
- **Critical & General Recommendations**: Clearly separates and highlights critical (must-fix, security, compliance, correctness) and general (style, maintainability, documentation, test coverage) suggestions, including both code and non-code/process feedback.
- **Highly Visible, Customizable Output**: Uses markdown formatting, headings, and emojis for maximum visibility in PR comments. Output format and prompt are fully customizable.
- **Exception List for Approval Logic**: Maintains an external `pr_review_exception_list.txt` file to define which issues should not block PR approval. Exception list is loaded at runtime for easy updates.
- **Robust Error Handling & Validation**: Validates all required environment variables and handles network/API errors gracefully with clear user-facing messages.
- **Security Best Practices**: Never prints or logs sensitive credentials, enforces input validation, and documents all security features.
- **CI/CD Integration**: Designed to run in GitHub Actions or other CI/CD environments. Example workflow provided for automated PR review on every pull request.
- **Documentation & Comparison**: Detailed documentation on setup, usage, and security, plus a comparison with GitHub Copilot PR Review.
- **Extensible & Maintainable**: Modular code structure for easy extension and maintenance. Unit and integration test coverage recommended for all new features.

#### 📝 Git Hooks and Commit/PR Standards
- **Commit Message Validation**: Git hook provided to enforce commit message standards (e.g., Conventional Commits).
- **Branch and PR Naming Enforcement**: GitHub Actions/local hooks ensure branch names, PR titles, and commit messages follow repository conventions.
- **Developer Experience**: Immediate feedback to contributors, reducing review friction and improving repository hygiene.

> **Upgrade Notes:**
> - To customize which issues are ignored for PR approval, edit `pr_review_exception_list.txt`.
> - Review and update environment variables and secrets in your CI/CD pipeline.

---


## 🚀 Key Features

- **Modular Terraform Core**: Reusable, CIS-compliant modules for Azure resources (VNET, NSG, Subnet, VMSS, Resource Groups, etc.) under `core-modules/`.
- **Landing Zones**: Predefined landing zones for application, management, connectivity, and AVD, supporting rapid, secure environment provisioning.
- **AI Agents for DevOps** (`ai-agents/`):
  - **Code Quality & Security Agent**: Integrates with code scanning tools and uses AI (e.g., Azure OpenAI) to review PRs, suggest improvements, and block insecure code.
  - **Cost Optimization Agent**: Analyzes Azure resource usage, identifies cost-saving opportunities, and sends actionable reports or automates remediation.
- **CI/CD Integration**: GitHub Actions workflows for automated code review, branch/PR naming enforcement, and pipeline orchestration.
- **Naming Conventions & Compliance**: Enforced naming standards and tagging for Azure resources, ensuring clarity and compliance.
- **Extensible Architecture**: Easily add new AI agents (e.g., for remediation, ChatOps, impact analysis) to automate more DevOps tasks.

---


## 🏗️ Technical Architecture

- **Terraform Modules**: Located in `core-modules/`, each module (e.g., `vnet`, `nsg`, `subnet`, `vmss`) is self-contained, parameterized, and follows best practices for security and maintainability.
- **Landing Zones**: Under `landingzones/`, these aggregate core modules for specific scenarios (application, management, connectivity, AVD).
- **AI Agents**: Python-based agents in `ai-agents/` folder, each with its own setup, requirements, and documentation.
- **CI/CD**: `.github/workflows/` contains automation for code review, naming checks, and more.

---


## 🗂️ Repository Structure

```text
core-modules/         # Reusable Terraform modules for Azure resources
landingzones/         # Composable landing zones for different environments
ai-agents/            # AI-powered DevOps agents (code quality, cost optimization, etc.)
.github/              # GitHub Actions workflows, PR templates, branch naming policies
NAMING_CONVENTIONS.md # Naming and tagging standards
README.md             # Project overview and getting started
```

---


## ⚡ Getting Started

1. **Clone the Repository**
   ```sh
   git clone https://github.com/ajeetchouksey/ajch_agenticdevops.git
   cd ajch_agenticdevops
   ```

2. **Provision Infrastructure**
   - Navigate to a landing zone or core module and follow the README for deployment instructions using Terraform.

3. **Set Up AI Agents**
   - See `ai-agents/codequality_agent/README.md` and `ai-agents/costopt_agent/README.md` for setup, configuration, and usage.

4. **CI/CD & Automation**
   - GitHub Actions are pre-configured for code review, naming enforcement, and more. Customize workflows as needed.

---


## 🛡️ Security & Compliance

- All Terraform modules are designed for CIS compliance and secure defaults.
- AI agents enforce secure credential handling and minimal permissions.
- Naming conventions and tagging are strictly enforced for traceability and governance.

---


## 📚 Documentation & References

- [Naming Conventions](NAMING_CONVENTIONS.md)
- [Code Quality Agent Guide](ai-agents/codequality_agent/README.md)
- [Cost Optimization Agent Guide](ai-agents/costopt_agent/README.md)
- [AI PR Review vs Copilot Comparison](ai-agents/codequality_agent/AI_PR_REVIEW_COMPARISON.md)
- [Terraform Azure Provider Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Azure DevOps Best Practices](https://learn.microsoft.com/en-us/azure/devops/)

---


## 🤝 Contributing

Contributions are welcome! Please follow the naming conventions, use PR templates, and ensure all code passes automated checks.

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for details.

---

_#DevOps #AI #Automation #AgenticDevOps #ContinuousImprovement #Cloud #Innovation_
