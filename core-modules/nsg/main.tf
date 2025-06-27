# NSG Module - CIS Compliant
resource "azurerm_network_security_group" "this" {
  for_each            = { for n in var.nsgs : n.name => n }
  name                = each.value.name
  location            = each.value.location
  resource_group_name = each.value.resource_group_name
  tags                = var.tags
}
