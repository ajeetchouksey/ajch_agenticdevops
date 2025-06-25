variable "tags" {
  description = "A map of tags to assign to the subnet."
  type        = map(string)
  default     = {}
}

// -----------------------------------------------------------------------------
// Input Variables for Subnet Module
// -----------------------------------------------------------------------------

variable "subnets" {
  description = "A map of subnet definitions. Each value is an object with keys: name, resource_group_name, virtual_network_name, address_prefixes, tags."
  type = map(object({
    name                 = string
    resource_group_name  = string
    virtual_network_name = string
    address_prefixes     = list(string)
    tags                 = optional(map(string), {})
  }))
}
