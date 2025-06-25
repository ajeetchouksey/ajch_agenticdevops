variable "subscription_code" {
  description = "Short code or abbreviation for the Azure subscription (e.g., dev01, prod02)."
  type        = string
}
variable "vnets" {
  description = "A map of VNet definitions for the vnet module."
  type = map(object({
    name                = string
    address_space       = list(string)
    location            = string
    resource_group_name = string
    tags                = optional(map(string), {})
  }))
}

variable "subnets" {
  description = "A map of subnet definitions for the subnet module."
  type = map(object({
    name                 = string
    resource_group_name  = string
    virtual_network_name = string
    address_prefixes     = list(string)
    tags                 = optional(map(string), {})
  }))
}

variable "nsgs" {
  description = "A map of NSG definitions for the nsg module."
  type = map(object({
    name                = string
    location            = string
    resource_group_name = string
    tags                = optional(map(string), {})
    rules = optional(list(object({
      name                       = string
      priority                   = number
      direction                  = string
      access                     = string
      protocol                   = string
      source_port_range          = string
      destination_port_range     = string
      source_address_prefix      = string
      destination_address_prefix = string
    })), [])
  }))
}
variable "project" {
  description = "Short name for the workload, app, or landing zone (e.g., devops, mgmt, app, avd)"
  type        = string
}

variable "env" {
  description = "Environment (e.g., dev, test, prod, shared)"
  type        = string
}

// -----------------------------------------------------------------------------
// Input Variables for DevOps Agent Deployment in Connectivity Landing Zone
// These variables are passed to the modular core network and agent modules.
// -----------------------------------------------------------------------------

variable "vnet_name" {
  description = "The name of the Azure Virtual Network (VNet) to create."
  type        = string
}

variable "vnet_address_space" {
  description = "A list of address spaces (CIDR blocks) for the VNet."
  type        = list(string)
}

variable "subnet_name" {
  description = "The name of the subnet to create within the VNet."
  type        = string
}

variable "subnet_address_prefixes" {
  description = "A list of address prefixes (CIDR blocks) for the subnet."
  type        = list(string)
}

variable "nsg_name" {
  description = "The name of the Network Security Group (NSG) to create."
  type        = string
}

variable "agent_name" {
  description = "The name of the Azure DevOps agent virtual machine."
  type        = string
}

variable "location" {
  description = "The Azure region where all resources will be deployed."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create all resources."
  type        = string
}

variable "vm_size" {
  description = "The size (SKU) of the virtual machine."
  type        = string
  default     = "Standard_B2ms"
}

variable "admin_username" {
  description = "The admin username for the DevOps agent VM."
  type        = string
}

variable "admin_password" {
  description = "The admin password for the DevOps agent VM."
  type        = string
  sensitive   = true
}

variable "admin_username" {
  description = "The admin username for the virtual machine."
}

variable "admin_password" {
  description = "The admin password for the virtual machine."
}


