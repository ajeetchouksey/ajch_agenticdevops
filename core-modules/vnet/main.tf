# VNET Module - CIS Compliant
resource "azurerm_virtual_network" "this" {
  for_each            = { for v in var.vnets : v.name => v }
  name                = each.value.name
  location            = each.value.location
  resource_group_name = each.value.resource_group_name
  address_space       = each.value.address_space
  tags                = var.tags
}
