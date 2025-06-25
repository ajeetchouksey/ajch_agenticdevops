
// -----------------------------------------------------------------------------
// Network Security Group (NSG) Module
// This module creates an Azure NSG for controlling network traffic.
// Designed for modularity and reusability in landing zones and core modules.
// -----------------------------------------------------------------------------

resource "azurerm_network_security_group" "this" {
  name                = var.name                 // Name of the NSG
  location            = var.location             // Azure region
  resource_group_name = var.resource_group_name  // Resource group for the NSG
  tags                = var.tags                 // Tags for governance/compliance
}

// Allow SSH if enabled
resource "azurerm_network_security_rule" "allow_ssh" {
  count                       = var.allow_ssh ? 1 : 0
  name                        = "Allow-SSH"
  priority                    = 1001
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefixes     = var.allowed_ssh_source
  destination_address_prefix  = "*"
  network_security_group_name = azurerm_network_security_group.this.name
  resource_group_name         = var.resource_group_name
}

// Allow RDP if enabled
resource "azurerm_network_security_rule" "allow_rdp" {
  count                       = var.allow_rdp ? 1 : 0
  name                        = "Allow-RDP"
  priority                    = 1002
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "3389"
  source_address_prefixes     = var.allowed_rdp_source
  destination_address_prefix  = "*"
  network_security_group_name = azurerm_network_security_group.this.name
  resource_group_name         = var.resource_group_name
}

// Deny all inbound by default (Azure default, but explicit for clarity)
resource "azurerm_network_security_rule" "deny_all_inbound" {
  name                        = "Deny-All-Inbound"
  priority                    = 4096
  direction                   = "Inbound"
  access                      = "Deny"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  network_security_group_name = azurerm_network_security_group.this.name
  resource_group_name         = var.resource_group_name
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
