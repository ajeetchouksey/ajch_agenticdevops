// CIS Compliant Resource Group Module
// Supports one or multiple resource group creation

resource "azurerm_resource_group" "this" {
  for_each = { for rg in var.resource_groups : rg.name => rg }
  name     = each.value.name
  location = each.value.location
  tags     = merge({
    "CIS_Compliance" = "true"
  }, each.value.tags)
}

