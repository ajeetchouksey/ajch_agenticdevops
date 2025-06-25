# Deploying the DevOps Agent in the Connectivity Landing Zone


This guide explains how to deploy a self-hosted Azure DevOps agent as the first task in your connectivity landing zone using the `core-modules/devops-agent` module. It also covers how to provision the required Storage Account for Terraform state and Key Vault for secrets using the Azure CLI or Portal, and then import them into Terraform state for best practice management.

## Prerequisites
- An existing resource group in your target Azure region
- An existing subnet in a virtual network for the agent VM
- Terraform installed and configured for your Azure subscription

## Deployment Workflow: Pre-Deployment, Deployment, and Post-Deployment

This section provides a clear, industry-aligned workflow for deploying the DevOps agent and supporting resources using GitHub Actions, with a focus on security, compliance, and best practices.


### Pre-Deployment (Bootstrap Phase)
1. **Clone the repository and create a new branch for your deployment.**
2. **Provision the following resources using the Azure CLI or Azure Portal:**
   - Storage Account and container for Terraform state
   - Key Vault for secrets
   - (Optional) Resource group if not already present

   Example Azure CLI commands:
   ```sh
   # Create resource group (if needed)
   az group create --name <resource-group> --location <location>

   # Create storage account
   az storage account create --name <storage-account> --resource-group <resource-group> --location <location> --sku Standard_LRS

   # Create storage container
   az storage container create --name tfstate --account-name <storage-account>

   # Create Key Vault
   az keyvault create --name <keyvault-name> --resource-group <resource-group> --location <location>
   ```

3. **Import the manually created resources into Terraform state:**
   - Define the corresponding resources in your Terraform configuration (e.g., `main.tf`).
   - Use `terraform import` to bring the Azure resources under Terraform management:
   ```sh
   terraform import azurerm_storage_account.tfstate "/subscriptions/<sub-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<storage-account>"
   terraform import azurerm_storage_container.tfstate "/subscriptions/<sub-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<storage-account>/blobServices/default/containers/tfstate"
   terraform import azurerm_key_vault.main "/subscriptions/<sub-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<keyvault-name>"
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

2. **Continue with Terraform deployment as usual:**
   - Run `terraform init` to initialize the remote backend.
   - Run `terraform plan` and `terraform apply` to deploy resources.

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


### Post-Deployment: Step-by-Step Operations
After the deployment workflow completes, follow these steps to ensure your environment is secure, compliant, and operational:

1. **Verify Remote State Storage**
   - Confirm that the Terraform state file is present in the Storage Account container.
   - Use the Azure Portal or CLI to check the blob in the container (e.g., `connectivity.terraform.tfstate`).

2. **Validate Key Vault Secrets**
   - Ensure all sensitive values (e.g., VM admin password) are stored as Key Vault secrets.
   - Remove any hardcoded secrets from code, variables, or pipeline definitions.

3. **Enable Diagnostics and Logging**
   - Attach diagnostic settings to the VM and Storage Account to send logs to Log Analytics.
   - Example for VM:
     ```hcl
     resource "azurerm_monitor_diagnostic_setting" "vm_diag" {
       name                       = "vm-diagnostics"
       target_resource_id         = azurerm_linux_virtual_machine.devops_agent.id
       log_analytics_workspace_id = <log_analytics_workspace_id>
       # ...log categories...
     }
     ```

4. **Review Network Security**
   - Confirm that Network Security Groups (NSGs) restrict access to the DevOps agent VM.
   - Only allow required ports and trusted IPs.

5. **Enable and Use Managed Identity (Recommended)**
   - Update the VM to use a managed identity for secure access to Azure resources.
   - Assign necessary roles to the managed identity.

6. **Monitor and Backup the VM**
   - Enable Azure Monitor alerts for VM health and performance.
   - Set up backup policies if the agent VM is stateful or critical.

7. **Review Security Scan Results**
   - Check the results of tfsec and other security tools in the GitHub Actions run.
   - Remediate any high or critical findings.

8. **Document and Communicate**
   - Update internal documentation with resource names, access patterns, and operational procedures.
   - Notify stakeholders that the DevOps agent is ready for use.

---
By following these post-deployment steps, you ensure your environment is not only deployed, but also secure, compliant, and ready for production use.

## GitHub Actions Workflow Example
See `.github/workflows/deploy-connectivity.yml` for a production-ready workflow. Key features:
- OIDC authentication (no long-lived secrets)
- Environment protection rules
- Security scanning (tfsec)
- Artifact upload for traceability

---
By following this workflow, you ensure a secure, compliant, and automated deployment of your DevOps agent and supporting resources, aligned with industry best practices.
