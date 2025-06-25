// Variables for core network module

variable "vnet_name" {
  description = "The name of the virtual network."
}

variable "vnet_address_space" {
  description = "The address space for the virtual network."
  type        = list(string)
}

variable "subnet_name" {
  description = "The name of the subnet."
}

variable "subnet_address_prefixes" {
  description = "The address prefixes for the subnet."
  type        = list(string)
}

variable "nsg_name" {
  description = "The name of the network security group."
}

variable "location" {
  description = "The Azure region for the resources."
}

variable "resource_group_name" {
  description = "The name of the resource group for the network resources."
}
