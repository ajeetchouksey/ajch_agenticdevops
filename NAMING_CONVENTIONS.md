# Naming Conventions for ajch_agenticdevops

This document defines the naming conventions for all resources, files, and automation in the ajch_agenticdevops repository. Following these conventions ensures consistency, clarity, and compliance with best practices (including Azure and Terraform standards).

---

## 1. Azure Resource Naming
- Use lowercase letters, numbers, and hyphens only.
- Prefix resource names with the environment (e.g., `dev-`, `test-`, `prod-`).
- Use short, descriptive names for resource types (e.g., `rg` for resource group, `vnet` for virtual network).
- Example: `prod-core-vnet-01`, `dev-app-rg`
- Avoid special characters and spaces.
- Keep names within Azure length limits (see [Azure naming rules](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules)).

## 2. Terraform Modules & Files
- Module directories: `core-modules/<module-name>`
- File names: use lowercase and hyphens (e.g., `main.tf`, `variables.tf`, `outputs.tf`)
- Use descriptive variable and output names (e.g., `resource_group_name`, `vnet_address_space`)

## 3. Automation & Pipelines
- Workflow files: `.github/workflows/<purpose>.yml` (e.g., `deploy-devops-agent.yml`)
- Job and step names: Use clear, action-oriented names (e.g., `Terraform Init`, `Checkov Security Scan`)

## 4. AI Agents
- Folder: `ai-agents/<agent-purpose>` (e.g., `costopt_agent`, `codequality_agent`)
- Scripts: Use snake_case (e.g., `ai_code_review.py`)
- Requirements: `requirements.txt`

## 5. Tags & Labels
- Use consistent tags for Azure resources (e.g., `Environment`, `Owner`, `ResourceType`)
- Tag values should match naming conventions (e.g., `environment=prod`)

## 6. General Guidelines
- Be concise but descriptive.
- Use hyphens for separation, not underscores or spaces.
- Document any exceptions in this file.

---

For questions or updates, please open a pull request or contact the repository maintainer.
