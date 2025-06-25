variable "tags" {
  description = "A map of tags to assign to the VNet."
  type        = map(string)
  default     = {}
}

// -----------------------------------------------------------------------------
// Input Variables for VNet Module
// -----------------------------------------------------------------------------

variable "vnets" {
  description = "A map of VNet definitions. Each value is an object with keys: name, address_space, location, resource_group_name, tags."
  type = map(object({
    name                = string
    address_space       = list(string)
    location            = string
    resource_group_name = string
    tags                = optional(map(string), {})
  }))
}
