





module "devopsagent_resource_groups" {
  source         = "../core-modules/resource-group"
  resource_groups = local.resource_groups
  
}