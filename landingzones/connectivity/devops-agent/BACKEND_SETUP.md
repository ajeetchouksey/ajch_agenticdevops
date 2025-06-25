# Remote Backend Setup for Terraform State

## Why Provision Backend Resources Outside Terraform?
- **Security & Compliance:** You control naming, access, and policies from the start.
- **Stability:** Prevents accidental deletion of state storage if you run `terraform destroy`.
- **Team Collaboration:** Enables safe, shared state for teams and automation.

## Step 1: Provision Storage Account and Key Vault (Azure CLI)

```sh
# Variables (customize these)
RESOURCE_GROUP="tfstate-rg"
LOCATION="eastus"
STORAGE_ACCOUNT="tfstate<unique>" # must be globally unique, lowercase
CONTAINER="tfstate"
KEYVAULT="tfstatekv<unique>"

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create storage account
az storage account create --name $STORAGE_ACCOUNT --resource-group $RESOURCE_GROUP --location $LOCATION --sku Standard_LRS --encryption-services blob

# Create blob container
az storage container create --account-name $STORAGE_ACCOUNT --name $CONTAINER

# (Optional) Create Key Vault for secrets
az keyvault create --name $KEYVAULT --resource-group $RESOURCE_GROUP --location $LOCATION
```

## Step 2: Configure `backend.tf`
Edit `backend.tf` in your Terraform directory:

```
terraform {
  backend "azurerm" {
    resource_group_name  = "dev-agentic-prod-rg"
    storage_account_name = "devagenticprodstg"
    container_name       = "statefiles"
    key                  = "devops-agent.terraform.tfstate"
  }
}
```

## Step 3: Initialize and Import State

```sh
# Initialize backend (will prompt to migrate state if local state exists)
terraform init

# (Optional) Import existing resources to state
terraform import <resource_address> <resource_id>
```

## Step 4: Secure Access
- Restrict access to the storage account and Key Vault using RBAC and firewall rules.
- Enable soft delete and versioning for the storage account.
- Use Key Vault for sensitive outputs or secrets.

## References
- [Terraform Azure Backend Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/azure_backend)
- [Azure CLI Docs](https://docs.microsoft.com/en-us/cli/azure/)
