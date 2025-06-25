
// -----------------------------------------------------------------------------
// Input Variables for Subnet Module
// -----------------------------------------------------------------------------

variable "name" {
  description = "The name of the Azure subnet."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the subnet."
  type        = string
}

variable "virtual_network_name" {
  description = "The name of the parent Virtual Network (VNet) for the subnet."
  type        = string
}

variable "address_prefixes" {
  description = "A list of address prefixes (CIDR blocks) for the subnet."
  type        = list(string)
}
