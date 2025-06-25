// Deploy private DNS zones for storage and Key Vault
module "privatedns" {
  source = "../../../core-modules/network/privatedns"
  dns_zones = {
    storage = {
      name                = local.storage_dns_zone_name
      resource_group_name = var.resource_group_name
    }
    keyvault = {
      name                = local.kv_dns_zone_name
      resource_group_name = var.resource_group_name
    }
  }
}

// Deploy private endpoints for storage and Key Vault
module "private_endpoint" {
  source = "../../../core-modules/network/private-endpoint"
  private_endpoints = {
    storage = {
      name                 = local.storage_pe_name
      location             = var.location
      resource_group_name  = var.resource_group_name
      subnet_id            = var.subnet_id
      connection_name      = local.storage_pe_connection_name
      resource_id          = var.storage_account_id
      subresource_names    = ["blob"]
      dns_zone_group_name  = local.storage_dns_zone_group_name
      private_dns_zone_ids = [module.privatedns.private_dns_zone_ids["storage"]]
    }
    keyvault = {
      name                 = local.kv_pe_name
      location             = var.location
      resource_group_name  = var.resource_group_name
      subnet_id            = var.subnet_id
      connection_name      = local.kv_pe_connection_name
      resource_id          = var.keyvault_id
      subresource_names    = ["vault"]
      dns_zone_group_name  = local.kv_dns_zone_group_name
      private_dns_zone_ids = [module.privatedns.private_dns_zone_ids["keyvault"]]
    }
  }
}
