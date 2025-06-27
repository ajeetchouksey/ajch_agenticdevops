variable "nsgs" {
  description = "List of NSGs to create."
  type = list(object({
    name                = string
    location            = string
    resource_group_name = string
  }))
}

variable "tags" {
  description = "Tags to apply to resources."
  type        = map(string)
  default     = {}
}
