variable "tags" {
  description = "A map of tags to assign to the VNet."
  type        = map(string)
  default     = {}
}

// -----------------------------------------------------------------------------
// Input Variables for VNet Module
// -----------------------------------------------------------------------------

variable "name" {
  description = "The name of the Azure Virtual Network (VNet)."
  type        = string
}

variable "address_space" {
  description = "A list of address spaces (CIDR blocks) for the VNet."
  type        = list(string)
}

variable "location" {
  description = "The Azure region where the VNet will be created."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the VNet."
  type        = string
}
