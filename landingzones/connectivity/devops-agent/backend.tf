// Remote backend configuration for Terraform state
// Storage account and container should be created outside Terraform (e.g., via Azure CLI)
// See README.md for provisioning and import instructions

terraform {
  backend "azurerm" {
    resource_group_name  = "<storage-rg>"         // Update with your storage RG
    storage_account_name = "<storageaccountname>" // Update with your storage account
    container_name       = "tfstate"              // Update if you use a different container
    key                  = "devops-agent.terraform.tfstate"
  }
}
