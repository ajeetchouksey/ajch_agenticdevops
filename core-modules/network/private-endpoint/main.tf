
// -----------------------------------------------------------------------------
// Private Endpoint Module
// This module provisions one or more Azure Private Endpoints based on the input map.
// Each endpoint connects a resource to a subnet and integrates with Private DNS Zones.
// -----------------------------------------------------------------------------

resource "azurerm_private_endpoint" "this" {
  for_each = var.private_endpoints
  name                = each.value.name                // Name of the private endpoint
  location            = each.value.location            // Azure region
  resource_group_name = each.value.resource_group_name // Resource group for the endpoint
  subnet_id           = each.value.subnet_id           // Subnet to associate the endpoint with

  private_service_connection {
    name                           = each.value.connection_name        // Name of the private service connection
    private_connection_resource_id = each.value.resource_id            // Resource ID of the target service (e.g., storage account)
    subresource_names              = each.value.subresource_names      // List of subresource names (e.g., ["blob"])
    is_manual_connection           = false                             // Automatic approval
  }

  private_dns_zone_group {
    name                 = each.value.dns_zone_group_name // Name for the DNS zone group
    private_dns_zone_ids = each.value.private_dns_zone_ids // List of DNS zone IDs to associate
  }
}

// Output a map of private endpoint keys to their resource IDs for downstream use
output "private_endpoint_ids" {
  description = "Map of private endpoint keys to their Azure resource IDs."
  value = { for k, v in azurerm_private_endpoint.this : k => v.id }
}
