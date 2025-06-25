variable "nsgs" {
  description = "A map of NSG definitions. Each value is an object with keys: name, location, resource_group_name, tags, rules (list of rule objects)."
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
