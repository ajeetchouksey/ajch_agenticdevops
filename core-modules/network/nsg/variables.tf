
// -----------------------------------------------------------------------------
// Input Variables for NSG Module
// -----------------------------------------------------------------------------

variable "name" {
  description = "The name of the Azure Network Security Group (NSG)."
  type        = string
}

variable "location" {
  description = "The Azure region where the NSG will be created."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the NSG."
  type        = string
}
