
// -----------------------------------------------------------------------------
// Input Variables for Private DNS Zone Module
// -----------------------------------------------------------------------------

variable "dns_zones" {
  description = "A map of private DNS zone definitions. Each key represents a logical DNS zone, with values specifying the zone name and resource group."
  type = map(object({
    name                = string   // The name of the private DNS zone (e.g., 'privatelink.file.core.windows.net')
    resource_group_name = string   // The resource group in which to create the DNS zone
  }))
}
