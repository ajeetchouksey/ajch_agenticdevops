
// -----------------------------------------------------------------------------
// Network Security Group (NSG) Module
// This module creates an Azure NSG for controlling network traffic.
// Designed for modularity and reusability in landing zones and core modules.
// -----------------------------------------------------------------------------

resource "azurerm_network_security_group" "this" {
  for_each            = var.nsgs
  name                = each.value.name
  location            = each.value.location
  resource_group_name = each.value.resource_group_name
  tags                = try(each.value.tags, {})
}

resource "azurerm_network_security_rule" "rule" {
  for_each = { for nsg_key, nsg in var.nsgs : nsg_key => nsg if length(try(nsg.rules, [])) > 0 }
  count    = length(try(var.nsgs[each.key].rules, []))
  name                        = var.nsgs[each.key].rules[count.index].name
  priority                    = var.nsgs[each.key].rules[count.index].priority
  direction                   = var.nsgs[each.key].rules[count.index].direction
  access                      = var.nsgs[each.key].rules[count.index].access
  protocol                    = var.nsgs[each.key].rules[count.index].protocol
  source_port_range           = var.nsgs[each.key].rules[count.index].source_port_range
  destination_port_range      = var.nsgs[each.key].rules[count.index].destination_port_range
  source_address_prefix       = var.nsgs[each.key].rules[count.index].source_address_prefix
  destination_address_prefix  = var.nsgs[each.key].rules[count.index].destination_address_prefix
  network_security_group_name = azurerm_network_security_group.this[each.key].name
  resource_group_name         = azurerm_network_security_group.this[each.key].resource_group_name
}

// Output: Map of NSG resource IDs
output "nsg_ids" {
  description = "A map of NSG resource IDs, keyed by NSG key."
  value       = { for k, v in azurerm_network_security_group.this : k => v.id }
}

// Output: Map of NSG names
output "nsg_names" {
  description = "A map of NSG names, keyed by NSG key."
  value       = { for k, v in azurerm_network_security_group.this : k => v.name }
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
