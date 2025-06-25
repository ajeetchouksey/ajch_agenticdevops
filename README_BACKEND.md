# Terraform Remote Backend Best Practices

## Why Use a Remote Backend?
- Ensures state is shared and protected for teams and automation
- Enables state locking and versioning
- Supports secure, compliant, and auditable infrastructure

## Recommended Approach
1. **Provision backend resources (Storage Account, Container, Key Vault) using Azure CLI or secure IaC.**
2. **Configure your Terraform `backend.tf` to use these resources.**
3. **Initialize Terraform and migrate state if needed.**
4. **Import any pre-existing resources to state as required.**

## Example CLI Script
See `landingzones/connectivity/devops-agent/BACKEND_SETUP.md` for a full script and step-by-step instructions.

## Example `backend.tf`
```
terraform {
  backend "azurerm" {
    resource_group_name  = "<storage-rg>"
    storage_account_name = "<storageaccountname>"
    container_name       = "tfstate"
    key                  = "devops-agent.terraform.tfstate"
  }
}
```

## Security Tips
- Restrict access to the storage account and Key Vault
- Enable soft delete and versioning
- Use Key Vault for secrets, not plain outputs

## References
- [Terraform Azure Backend Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/azure_backend)
- [Azure CLI Docs](https://docs.microsoft.com/en-us/cli/azure/)
