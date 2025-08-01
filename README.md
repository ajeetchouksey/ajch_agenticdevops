

# Agentic DevOps: Human-on-the-Sidelines Framework

AgenticDevOps is a revolutionary DevOps automation framework that transitions from **human-in-the-loop** to **human-on-the-sidelines** operations. Our autonomous AI agents handle routine DevOps tasks with minimal human intervention, escalating only when necessary. This approach delivers unprecedented efficiency gains, error reduction, and scalability while maintaining safety and compliance.

## 🎯 The Human-on-the-Sidelines Revolution

Traditional DevOps practices rely on human intervention at critical junctures, creating bottlenecks and inefficiencies. Our autonomous agents change this paradigm:

- **Autonomous Decision Making**: AI agents make intelligent decisions based on context, patterns, and policies
- **Exception-Only Escalation**: Humans are alerted only when agent confidence is low or critical thresholds are exceeded
- **Continuous Learning**: Agents improve their decision-making through machine learning and pattern recognition
- **Fail-Safe Design**: Agents default to human escalation when uncertain, ensuring safety and compliance

---

## 📦 Latest Release Notes ([v0.0.2]([https://github.com/ajeetchouksey/ajch_agenticdevops/releases/tag/v0.0.2]))

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

### Autonomous DevOps Agents
- **CI/CD Orchestration Agent**: Autonomous pipeline management with smart triggering, dynamic workflow selection, and automatic rollback capabilities
- **Infrastructure Management Agent**: Intelligent resource provisioning, dynamic scaling, and cost optimization with predictive analytics
- **Incident Response Agent**: Autonomous incident detection, analysis, and resolution with ML-powered pattern recognition
- **Enhanced Code Quality Agent**: AI-powered code review with security scanning and compliance checking
- **Cost Optimization Agent**: Continuous cost analysis with automated resource cleanup and optimization

### Human-on-the-Sidelines Operations
- **Executive Dashboards**: Real-time overview of all agent activities with minimal intervention points
- **Exception-Only Alerts**: Humans are notified only when thresholds are exceeded or manual approval is required
- **Intelligent Escalation**: Smart escalation based on confidence scores, severity levels, and business impact
- **Comprehensive Audit Trail**: Complete logging of all autonomous decisions for compliance and learning

### Infrastructure Foundation
- **Modular Terraform Core**: Reusable, CIS-compliant modules for Azure resources (VNET, NSG, Subnet, VMSS, Resource Groups, etc.) under `core-modules/`
- **Landing Zones**: Predefined landing zones for application, management, connectivity, and AVD, supporting rapid, secure environment provisioning
- **CI/CD Integration**: GitHub Actions workflows for automated orchestration and monitoring
- **Naming Conventions & Compliance**: Enforced naming standards and tagging for Azure resources, ensuring clarity and compliance

---


## 🏗️ Technical Architecture

- **Terraform Modules**: Located in `core-modules/`, each module (e.g., `vnet`, `nsg`, `subnet`, `vmss`) is self-contained, parameterized, and follows best practices for security and maintainability.
- **Landing Zones**: Under `landingzones/`, these aggregate core modules for specific scenarios (application, management, connectivity, AVD).
- **AI Agents**: Python-based agents in `ai-agents/` folder, each with its own setup, requirements, and documentation.
- **CI/CD**: `.github/workflows/` contains automation for code review, naming checks, and more.

---


## 🗂️ Repository Structure

```text
ai-agents/                          # Autonomous DevOps agents
├── cicd_orchestration_agent/       # CI/CD pipeline orchestration and automation
├── infrastructure_management_agent/ # Infrastructure provisioning and optimization
├── incident_response_agent/        # Autonomous incident detection and resolution
├── codequality_agent/             # Enhanced AI-powered code review
├── costopt_agent/                 # Cost optimization and resource management
└── agent_orchestrator/            # Central agent coordination and monitoring

core-modules/                       # Reusable Terraform modules for Azure resources
landingzones/                       # Composable landing zones for different environments
.github/workflows/                  # Autonomous DevOps orchestration workflows
├── agentic-devops-orchestration.yml # Main agent coordination workflow
└── ai-code-review.yml             # Enhanced code review workflow

NAMING_CONVENTIONS.md               # Naming and tagging standards
README.md                           # Project overview and getting started
```

---


## ⚡ Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/ajeetchouksey/ajch_agenticdevops.git
cd ajch_agenticdevops
```

### 2. Configure Autonomous Agents
Set up environment variables for your agents:

```bash
# Core AI Configuration
export AI_API_KEY="your-ai-api-key"
export AI_API_URL="your-ai-endpoint"

# Azure Configuration (for infrastructure and monitoring)
export AZURE_CLIENT_ID="your-client-id"
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_SECRET="your-client-secret"
export AZURE_SUBSCRIPTION_ID="your-subscription-id"

# Notification Channels
export SLACK_WEBHOOK_URL="your-slack-webhook"
export TEAMS_WEBHOOK_URL="your-teams-webhook"

# Agent Operation Modes
export AUTO_SCALING_ENABLED="true"
export AUTO_RESOLUTION_ENABLED="true"
export AUTONOMOUS_MODE="monitor"  # Start with monitor mode
```

### 3. Start Agents in Monitor Mode
Begin with human oversight and gradually enable autonomy:

```bash
# Start CI/CD orchestration agent
python ai-agents/cicd_orchestration_agent/cicd_orchestration_agent.py --mode monitor

# Start infrastructure management agent
python ai-agents/infrastructure_management_agent/infrastructure_management_agent.py --mode monitor

# Start incident response agent
python ai-agents/incident_response_agent/incident_response_agent.py --mode monitor
```

### 4. Enable Autonomous Operations
Once confident in agent behavior, enable autonomous mode:

```bash
# Enable autonomous operations with continuous monitoring
python ai-agents/cicd_orchestration_agent/cicd_orchestration_agent.py --mode autonomous --continuous
```

### 5. Monitor Agent Dashboard
Access the human-on-the-sidelines dashboard to monitor all agent activities and intervene only when necessary.

### 6. Provision Infrastructure (Optional)
- Navigate to a landing zone or core module and follow the README for deployment instructions using Terraform.

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
