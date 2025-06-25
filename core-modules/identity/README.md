# Identity Module

This module provides reusable resources for Azure identity management, such as managed identities, service principals, and role assignments.

## Example Resources
- Managed Identities
- Service Principals
- Role Assignments

## Usage Example
```hcl
module "identity" {
  source = "../../core-modules/identity"
  # ...module variables...
}
```
