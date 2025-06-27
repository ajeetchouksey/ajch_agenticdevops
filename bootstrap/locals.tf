
# Naming convention locals for bootstrap
locals {
  # Naming convention prefixes
  rg_prefix      = "rg"
  law_prefix     = "log"
  service_prefix = "devops"

  # Environment and owner from variables
  env   = var.environment
  owner = var.owner
  // resource_type = "Microsoft.Resources/resourceGroups"
  tags = var.tags

  # List of resource groups for module input
  resource_groups = [
    {
      name     = "${local.env}-${local.service_prefix}-${local.rg_prefix}-01"
      location = "westeurope"
      tags     = local.tags
    },
    # Example for additional resource group:
    # {
    #   name     = "${local.env}-${local.service_prefix}-${local.rg_prefix}-02"
    #   location = "westeurope"
    #   tags     = local.tags
    # }
  ]
}
