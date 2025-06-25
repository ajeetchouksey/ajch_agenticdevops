# Network Module

This module provides reusable resources for Azure networking, such as virtual networks, subnets, and network security groups.

## Example Resources
- Virtual Network (VNet)
- Subnets
- Network Security Groups (NSG)
- Route Tables
- Peerings

## Usage Example
```hcl
module "network" {
  source = "../../core-modules/network"
  # ...module variables...
}
```
