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

2. **Move State File from Local Backend to Remote Storage (Step-by-Step):**

   To safely migrate your Terraform state from the local backend to remote Azure Storage, follow these steps:

   **Step 1: Complete Initial Deployment with Local Backend**
   - Run `terraform init` and `terraform apply` as usual. Your state file (`terraform.tfstate`) will be stored locally.

   **Step 2: Add Remote Backend Configuration**
   - Create or update a file named `backend.tf` in your working directory with the following content (replace placeholders):
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

   **Step 3: Migrate State to Remote Backend**
   - In your terminal, run:
     ```sh
     terraform init -migrate-state
     ```
   - Terraform will detect the backend change and prompt you to migrate your state.
   - Type `yes` when prompted. Terraform will upload your local `terraform.tfstate` to the specified Azure Storage container.

   **Step 4: Verify Migration**
   - Check your Azure Storage Account container for the `.tfstate` file.
   - Run:
     ```sh
     terraform state list
     ```
     to ensure all resources are still tracked.

   **Step 5: Clean Up Local State Files**
   - Delete any local `terraform.tfstate` and `terraform.tfstate.backup` files to avoid confusion.

   **Step 6: Commit and Push Backend Changes**
   - Commit your new/updated `backend.tf` to version control and push to your remote repository.

   **Step 7: For All Future Deployments**
   - Always keep the `backend.tf` file with the remote backend configuration in your repo.
   - When running `terraform init`, Terraform will automatically use the remote backend.
   - All state changes will be stored in Azure Storage, supporting collaboration, locking, and security.
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
