
// -----------------------------------------------------------------------------
// Private DNS Zone Module
// This module provisions one or more Azure Private DNS Zones based on the input map.
// Each DNS zone is uniquely named and placed in the specified resource group.
// -----------------------------------------------------------------------------

resource "azurerm_private_dns_zone" "this" {
  for_each = var.dns_zones
  name                = each.value.name              // The name of the private DNS zone (e.g., 'privatelink.blob.core.windows.net')
  resource_group_name = each.value.resource_group_name // The resource group in which to create the DNS zone
}

// Output a map of DNS zone keys to their resource IDs for downstream use
output "private_dns_zone_ids" {
  description = "Map of DNS zone keys to their Azure resource IDs."
  value = { for k, v in azurerm_private_dns_zone.this : k => v.id }
}
