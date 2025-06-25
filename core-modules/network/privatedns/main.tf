// Private DNS Zone module for single responsibility
resource "azurerm_private_dns_zone" "this" {
  for_each = var.dns_zones
  name                = each.value.name
  resource_group_name = each.value.resource_group_name
}

output "private_dns_zone_ids" {
  value = { for k, v in azurerm_private_dns_zone.this : k => v.id }
}
