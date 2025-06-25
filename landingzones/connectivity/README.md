# Deploying the DevOps Agent in the Connectivity Landing Zone

This guide explains how to deploy a self-hosted Azure DevOps agent as the first task in your connectivity landing zone using the `core-modules/devops-agent` module. It also covers how to bootstrap the required Storage Account for Terraform state and Key Vault for secrets, following best practices for a fresh deployment.

## Prerequisites
- An existing resource group in your target Azure region
- An existing subnet in a virtual network for the agent VM
- Terraform installed and configured for your Azure subscription

## Deployment Workflow: Pre-Deployment, Deployment, and Post-Deployment

This section provides a clear, industry-aligned workflow for deploying the DevOps agent and supporting resources using GitHub Actions, with a focus on security, compliance, and best practices.

### Pre-Deployment (Bootstrap Phase)
1. **Clone the repository and create a new branch for your deployment.**
2. **Create the following resources using the local backend:**
   - Storage Account and container for Terraform state
   - Key Vault for secrets
   - (Optional) Resource group if not already present

   Example `main.tf` for bootstrap:
   ```hcl
   resource "azurerm_storage_account" "tfstate" { ... }
   resource "azurerm_storage_container" "tfstate" { ... }
   resource "azurerm_key_vault" "main" { ... }
   resource "azurerm_key_vault_secret" "admin_password" { ... }
   ```
   Use local backend (do not configure remote backend yet).

3. **Run locally:**
   ```sh
   terraform init
   terraform apply
   ```

### Deployment (Remote Backend & GitHub Actions)
1. **Configure the remote backend** in `backend.tf` after the Storage Account is created:
   ```hcl
   terraform {
     backend "azurerm" {
       resource_group_name  = "<resource-group>"
       storage_account_name = "<storage-account>"
       container_name       = "tfstate"
       key                  = "connectivity.terraform.tfstate"
     }
   }
   ```
2. **Migrate state to remote backend:**
   ```sh
   terraform init -migrate-state
   ```
3. **Update your `main.tf` to deploy the DevOps agent using the module and Key Vault secret:**
   ```hcl
   module "devops_agent" {
     source              = "../../core-modules/devops-agent"
     agent_name          = "devops-agent-01"
     location            = var.location
     resource_group_name = var.resource_group_name
     vm_size             = "Standard_B2ms"
     admin_username      = var.admin_username
     admin_password      = azurerm_key_vault_secret.admin_password.value
     subnet_id           = var.subnet_id
   }
   ```
4. **Commit and push your changes to GitHub.**
5. **Trigger the GitHub Actions workflow** (`.github/workflows/deploy-connectivity.yml`) to automate deployment:
   - Uses OIDC for secure authentication (no secrets in code)
   - Runs `terraform init`, `plan`, and `apply`
   - Uploads plan as artifact
   - Runs post-apply security scan (tfsec)

### Post-Deployment (Best Practices & Compliance)
After deployment, ensure:
- **State file is stored in the remote backend (Storage Account).**
- **Secrets are stored in Key Vault, not in code or variables.**
- **Diagnostics and logging are enabled for the VM and Storage Account (send to Log Analytics if possible).**
- **NSGs restrict access to the DevOps agent VM.**
- **VM uses managed identity if possible.**
- **Monitor and backup the VM as required.**
- **Review and remediate any issues found by tfsec or other security tools.**

## GitHub Actions Workflow Example
See `.github/workflows/deploy-connectivity.yml` for a production-ready workflow. Key features:
- OIDC authentication (no long-lived secrets)
- Environment protection rules
- Security scanning (tfsec)
- Artifact upload for traceability

---
By following this workflow, you ensure a secure, compliant, and automated deployment of your DevOps agent and supporting resources, aligned with industry best practices.
