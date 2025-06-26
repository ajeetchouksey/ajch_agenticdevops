variable "resource_groups" {
  description = "List of resource groups to create. Each item is an object with name, location, and tags."
  type = list(object({
    name     = string
    location = string
    tags     = map(string)
  }))
}
