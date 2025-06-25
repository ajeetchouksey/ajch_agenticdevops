// Private Endpoint module for single responsibility
resource "azurerm_private_endpoint" "this" {
  for_each = var.private_endpoints
  name                = each.value.name
  location            = each.value.location
  resource_group_name = each.value.resource_group_name
  subnet_id           = each.value.subnet_id

  private_service_connection {
    name                           = each.value.connection_name
    private_connection_resource_id = each.value.resource_id
    subresource_names              = each.value.subresource_names
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = each.value.dns_zone_group_name
    private_dns_zone_ids = each.value.private_dns_zone_ids
  }
}

output "private_endpoint_ids" {
  value = { for k, v in azurerm_private_endpoint.this : k => v.id }
}
