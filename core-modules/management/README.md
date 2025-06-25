# Management Module

This module contains reusable resources for Azure management and governance, such as Log Analytics workspaces, policy assignments, and monitoring resources.

## Example Resources
- Log Analytics Workspace
- Policy definitions and assignments
- Resource locks
- Diagnostic settings

## Usage Example
```hcl
module "management" {
  source                = "../../core-modules/management"
  log_analytics_name    = var.log_analytics_name
  location              = var.location
  resource_group_name   = var.resource_group_name
  log_analytics_sku     = var.log_analytics_sku
  retention_in_days     = var.retention_in_days
}
```
