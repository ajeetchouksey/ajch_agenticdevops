
// -----------------------------------------------------------------------------
// Network Security Group (NSG) Module
// This module creates an Azure NSG for controlling network traffic.
// Designed for modularity and reusability in landing zones and core modules.
// -----------------------------------------------------------------------------

resource "azurerm_network_security_group" "this" {
  name                = var.name                 // Name of the NSG
  location            = var.location             // Azure region
  resource_group_name = var.resource_group_name  // Resource group for the NSG
}

// Output: NSG resource ID for referencing in other modules
output "nsg_id" {
  description = "The resource ID of the created Network Security Group."
  value       = azurerm_network_security_group.this.id
}

// Output: NSG name for downstream modules
output "nsg_name" {
  description = "The name of the created Network Security Group."
  value       = azurerm_network_security_group.this.name
}
