# Subnet Module - CIS Compliant
#
# This module creates one or more Azure subnets as defined in the 'subnets' variable.
# Each subnet is created in the specified resource group and virtual network, with the given address prefixes.
#
# Inputs:
#   - var.subnets: List of subnet objects with 'name', 'resource_group_name', 'virtual_network_name', and 'address_prefixes'.
#
# Example subnet object:
#   {
#     name                 = "subnet1"
#     resource_group_name  = "my-rg"
#     virtual_network_name = "my-vnet"
#     address_prefixes     = ["10.0.1.0/24"]
#   }
#
# Output:
#   - azurerm_subnet.this: Map of created subnet resources, keyed by subnet name.

resource "azurerm_subnet" "this" {
  for_each             = { for s in var.subnets : s.name => s } # Create a subnet for each entry in the subnets list
  name                 = each.value.name                        # Subnet name
  resource_group_name  = each.value.resource_group_name         # Resource group where the subnet will be created
  virtual_network_name = each.value.virtual_network_name        # Virtual network to which the subnet belongs
  address_prefixes     = each.value.address_prefixes            # List of address prefixes for the subnet
}