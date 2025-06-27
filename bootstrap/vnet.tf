module "devops_vnet" {
  source = "../core-modules/vnet"
  vnets = [
    {
      name                = "${local.env}-${local.service_prefix}-vnet-01"
      location            = "westeurope"
      resource_group_name = module.devopsagent_resource_groups.resource_group_names[0]
      address_space       = ["10.10.0.0/16"]
    }
  ]
  tags = local.tags
}
