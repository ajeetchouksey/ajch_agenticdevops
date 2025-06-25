variable "dns_zones" {
  description = "Map of private DNS zone definitions."
  type = map(object({
    name                = string
    resource_group_name = string
  }))
}
