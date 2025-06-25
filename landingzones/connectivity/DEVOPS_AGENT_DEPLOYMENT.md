# DevOps Agent Deployment Guide

This guide provides detailed, step-by-step instructions for deploying a self-hosted Azure DevOps agent in the connectivity landing zone, including secure state management, secret handling, and post-deployment best practices.

---

## Prerequisites
- An existing resource group in your target Azure region
- An existing subnet in a virtual network for the agent VM
- Terraform installed and configured for your Azure subscription

---

## 1. Bootstrap Phase (Local Backend)
1. Clone the repository and create a new branch for your deployment.
2. Create the following resources using the local backend:
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

3. Run locally:
   ```sh
   terraform init
   terraform apply
   ```

---

## 2. Move State File from Local Backend to Remote Storage
1. Add remote backend configuration in `backend.tf`:
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
2. Migrate state:
   ```sh
   terraform init -migrate-state
   ```
   - Type `yes` when prompted.
3. Verify migration:
   - Check Azure Storage for the `.tfstate` file.
   - Run `terraform state list` to confirm resources are tracked.
4. Clean up local `.tfstate` files.
5. Commit and push backend changes.

---

## 3. Deploy the DevOps Agent (Remote Backend)
1. Update your `main.tf` to use the DevOps agent module and reference the Key Vault secret:
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
2. Commit and push your changes to GitHub.
3. Trigger the GitHub Actions workflow (`.github/workflows/deploy-connectivity.yml`) to automate deployment.

---

## 4. Post-Deployment: Best Practices & Operations
1. **Verify Remote State Storage**
   - Confirm the state file is present in Azure Storage.
2. **Validate Key Vault Secrets**
   - Ensure all sensitive values are stored in Key Vault.
3. **Enable Diagnostics and Logging**
   - Attach diagnostic settings to the VM and Storage Account (send to Log Analytics).
4. **Review Network Security**
   - Confirm NSGs restrict access to the DevOps agent VM.
5. **Enable and Use Managed Identity**
   - Update the VM to use a managed identity and assign necessary roles.
6. **Monitor and Backup the VM**
   - Enable Azure Monitor alerts and set up backup policies if needed.
7. **Review Security Scan Results**
   - Check tfsec and other security tool results in GitHub Actions.
8. **Document and Communicate**
   - Update internal docs and notify stakeholders.

---

## 5. For All Future Deployments
- Always keep the `backend.tf` file with remote backend configuration in your repo.
- All state changes will be stored in Azure Storage, supporting collaboration, locking, and security.
- Use GitHub Actions for automated, secure, and compliant deployments.

---

By following this guide, you ensure a secure, compliant, and automated deployment of your DevOps agent and supporting resources, aligned with industry best practices.
