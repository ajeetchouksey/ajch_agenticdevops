
// -----------------------------------------------------------------------------
// Virtual Network (VNet) Module
// This module creates an Azure Virtual Network using best practices for modularity,
// reusability, and single responsibility. Outputs are provided for cross-module use.
// -----------------------------------------------------------------------------

resource "azurerm_virtual_network" "this" {
  for_each            = var.vnets
  name                = each.value.name
  address_space       = each.value.address_space
  location            = each.value.location
  resource_group_name = each.value.resource_group_name
  tags                = try(each.value.tags, {})
}

// Output: Map of VNet resource IDs
output "vnet_ids" {
  description = "A map of VNet resource IDs, keyed by VNet key."
  value       = { for k, v in azurerm_virtual_network.this : k => v.id }
}

// Output: Map of VNet names
output "vnet_names" {
  description = "A map of VNet names, keyed by VNet key."
  value       = { for k, v in azurerm_virtual_network.this : k => v.name }
}
