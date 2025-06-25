variable "private_endpoints" {
  description = "Map of private endpoint definitions."
  type = map(object({
    name                   = string
    location               = string
    resource_group_name    = string
    subnet_id              = string
    connection_name        = string
    resource_id            = string
    subresource_names      = list(string)
    dns_zone_group_name    = string
    private_dns_zone_ids   = list(string)
  }))
}
