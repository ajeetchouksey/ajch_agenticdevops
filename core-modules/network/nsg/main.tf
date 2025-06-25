
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

locals {
  nsg_rules_flat = merge([
    for nsg_key, nsg in var.nsgs :
      length(try(nsg.rules, [])) > 0 ? {
        for rule_idx, rule in nsg.rules :
          "${nsg_key}.${rule_idx}" => {
            nsg_key = nsg_key
            rule    = rule
          }
      } : {}
  ]...)
}

resource "azurerm_network_security_rule" "rule" {
  for_each = local.nsg_rules_flat
  name                        = each.value.rule.name
  priority                    = each.value.rule.priority
  direction                   = each.value.rule.direction
  access                      = each.value.rule.access
  protocol                    = each.value.rule.protocol
  source_port_range           = each.value.rule.source_port_range
  destination_port_range      = each.value.rule.destination_port_range
  source_address_prefix       = each.value.rule.source_address_prefix
  destination_address_prefix  = each.value.rule.destination_address_prefix
  network_security_group_name = azurerm_network_security_group.this[each.value.nsg_key].name
  resource_group_name         = azurerm_network_security_group.this[each.value.nsg_key].resource_group_name
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
