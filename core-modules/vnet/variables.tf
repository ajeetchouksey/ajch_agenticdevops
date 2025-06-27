variable "vnets" {
  description = "List of VNETs to create."
  type = list(object({
    name                = string
    location            = string
    resource_group_name = string
    address_space       = list(string)
  }))
}

variable "tags" {
  description = "Tags to apply to resources."
  type        = map(string)
  default     = {}
}
