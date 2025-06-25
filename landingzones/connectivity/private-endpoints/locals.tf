// Naming convention: 3-character subscription code prefix (see NAMING_CONVENTIONS.md)
locals {
  storage_pe_name            = "${var.subscription_code}-${var.project}-${var.env}-pe-storage"
  kv_pe_name                 = "${var.subscription_code}-${var.project}-${var.env}-pe-kv"
  storage_pe_connection_name = "${var.subscription_code}-${var.project}-${var.env}-pe-storage-conn"
  kv_pe_connection_name      = "${var.subscription_code}-${var.project}-${var.env}-pe-kv-conn"
  storage_dns_zone_name      = "privatelink.blob.core.windows.net"
  kv_dns_zone_name           = "privatelink.vaultcore.azure.net"
  storage_dns_zone_group_name = "${var.subscription_code}-${var.project}-${var.env}-storage-dns-group"
  kv_dns_zone_group_name      = "${var.subscription_code}-${var.project}-${var.env}-kv-dns-group"
}
