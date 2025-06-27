module "devops_subnet" {
  source = "../core-modules/subnet"
  subnets = [
    {
      name                 = "${local.env}-${local.service_prefix}-subnet-01"
      resource_group_name  = module.devopsagent_resource_groups.resource_group_names[0]
      virtual_network_name = module.devops_vnet.vnet_ids["${local.env}-${local.service_prefix}-vnet-01"]
      address_prefixes     = ["10.10.1.0/24"]
    }
  ]
}
