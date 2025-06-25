// Remote backend configuration for Terraform state
// Storage account and container should be created outside Terraform (e.g., via Azure CLI)
// See README.md for provisioning and import instructions

terraform {
  backend "azurerm" {
    resource_group_name  = "dev-agentic-prod-rg"         // Updated for statefiles backend
    storage_account_name = "devagenticprodstg"           // Updated for statefiles backend
    container_name       = "statefiles"                  // Updated for statefiles backend
    key                  = "devops-agent.terraform.tfstate"
  }
}
