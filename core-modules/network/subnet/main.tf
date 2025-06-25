
// -----------------------------------------------------------------------------
// Subnet Module
// This module creates a subnet within a specified Virtual Network (VNet).
// Designed for modularity and reusability in landing zones and core modules.
// -----------------------------------------------------------------------------

resource "azurerm_subnet" "this" {
  for_each             = var.subnets
  name                 = each.value.name
  resource_group_name  = each.value.resource_group_name
  virtual_network_name = each.value.virtual_network_name
  address_prefixes     = each.value.address_prefixes
  # tags not supported by azurerm_subnet as of now
}

// Output: Map of Subnet resource IDs
output "subnet_ids" {
  description = "A map of Subnet resource IDs, keyed by subnet key."
  value       = { for k, v in azurerm_subnet.this : k => v.id }
}

// Output: Map of Subnet names
output "subnet_names" {
  description = "A map of Subnet names, keyed by subnet key."
  value       = { for k, v in azurerm_subnet.this : k => v.name }
}
