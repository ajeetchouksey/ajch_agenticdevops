


module "cis_resource_groups" {
  source = "../core-modules/resource-group"
  resource_groups = [
    {
      name     = local.rg_name
      location = "eastus"
      tags = {
        Owner       = local.owner
        Environment = local.env
      }
    },
    # Add more resource groups as needed
    # {
    #   name     = local.rg_name
    #   location = "westeurope"
    #   tags = {
    #     Owner       = local.owner
    #     Environment = local.env
    #   }
    # }
  ]
}