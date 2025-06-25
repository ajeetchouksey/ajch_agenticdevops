
// -----------------------------------------------------------------------------
// Input Variables for Private Endpoint Module
// -----------------------------------------------------------------------------

variable "private_endpoints" {
  description = "A map of private endpoint definitions. Each key represents a logical private endpoint, with values specifying all required properties."
  type = map(object({
    name                   = string        // Name of the private endpoint
    location               = string        // Azure region
    resource_group_name    = string        // Resource group for the endpoint
    subnet_id              = string        // Subnet to associate the endpoint with
    connection_name        = string        // Name of the private service connection
    resource_id            = string        // Resource ID of the target service
    subresource_names      = list(string)  // List of subresource names (e.g., ["blob"])
    dns_zone_group_name    = string        // Name for the DNS zone group
    private_dns_zone_ids   = list(string)  // List of DNS zone IDs to associate
  }))
}
