output "resource_group_ids" {
  description = "IDs of the created resource groups."
  value       = [for rg in azurerm_resource_group.this : rg.id]
}

output "resource_group_names" {
  description = "Names of the created resource groups."
  value       = [for rg in azurerm_resource_group.this : rg.name]
}
