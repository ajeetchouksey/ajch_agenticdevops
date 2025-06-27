module "devops_vmss" {
  source = "../core-modules/vmss"
  vmss_list = [
    {
      name                    = "${local.env}-${local.service_prefix}-vmss-01"
      location                = "westeurope"
      resource_group_name     = module.devopsagent_resource_groups.resource_group_names[0]
      sku                     = "Standard_DS2_v2"
      instances               = 2
      admin_username          = var.vmss_admin_username
      admin_password          = var.vmss_admin_password
      zones                   = ["1"]
      disk_encryption_set_id  = var.disk_encryption_set_id
      boot_diag_storage_uri   = var.boot_diag_storage_uri
      nic_name                = "${local.env}-${local.service_prefix}-nic-01"
      ip_config_name          = "${local.env}-${local.service_prefix}-ipconfig-01"
      subnet_id               = module.devops_subnet.subnet_ids["${local.env}-${local.service_prefix}-subnet-01"]
      nsg_id                  = module.devops_nsg.nsg_ids["${local.env}-${local.service_prefix}-nsg-01"]
    }
  ]
  tags = local.tags
}
