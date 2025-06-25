
// -----------------------------------------------------------------------------
// Virtual Network (VNet) Module
// This module creates an Azure Virtual Network using best practices for modularity,
// reusability, and single responsibility. Outputs are provided for cross-module use.
// -----------------------------------------------------------------------------

resource "azurerm_virtual_network" "this" {
  name                = var.name                 // Name of the VNet
  address_space       = var.address_space        // List of address spaces (CIDR blocks)
  location            = var.location             // Azure region
  resource_group_name = var.resource_group_name  // Resource group for the VNet
  tags                = var.tags                 // Tags for governance/compliance
}

// Output: VNet resource ID for referencing in other modules
output "vnet_id" {
  description = "The resource ID of the created Virtual Network."
  value       = azurerm_virtual_network.this.id
}

// Output: VNet name for downstream modules
output "vnet_name" {
  description = "The name of the created Virtual Network."
  value       = azurerm_virtual_network.this.name
}
