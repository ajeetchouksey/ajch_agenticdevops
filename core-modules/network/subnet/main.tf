
// -----------------------------------------------------------------------------
// Subnet Module
// This module creates a subnet within a specified Virtual Network (VNet).
// Designed for modularity and reusability in landing zones and core modules.
// -----------------------------------------------------------------------------

resource "azurerm_subnet" "this" {
  name                 = var.name                 // Name of the subnet
  resource_group_name  = var.resource_group_name  // Resource group for the subnet
  virtual_network_name = var.virtual_network_name // Name of the parent VNet
  address_prefixes     = var.address_prefixes     // List of address prefixes (CIDR blocks)
}

// Output: Subnet resource ID for referencing in other modules
output "subnet_id" {
  description = "The resource ID of the created subnet."
  value       = azurerm_subnet.this.id
}

// Output: Subnet name for downstream modules
output "subnet_name" {
  description = "The name of the created subnet."
  value       = azurerm_subnet.this.name
}
