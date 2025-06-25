# Azure Resource Naming Conventions

## Purpose
Consistent naming conventions improve clarity, automation, and compliance across all Azure resources and Terraform modules.


## General Pattern (with Subscription Prefix)
```
<sub>-<project/purpose>-<env>-<resource-type>-<optional-unique>
```
- **sub**: 3-character subscription code prefix (see mapping table below)
- **project/purpose**: Short name for the workload, app, or landing zone (e.g., `devops`, `mgmt`, `app`, `avd`)
- **env**: Environment (e.g., `dev`, `test`, `prod`, `shared`)
- **resource-type**: Abbreviation for the Azure resource (see below)
- **optional-unique**: Optional unique string or number for disambiguation


## Examples
| Resource Type   | Pattern Example                | Description                       |
|----------------|-------------------------------|-----------------------------------|
| VNet           | d01-devops-dev-vnet            | DevOps VNet in dev subscription   |
| Subnet         | d01-devops-dev-snet-agent      | Agent subnet in dev VNet          |
| NSG            | d01-devops-dev-nsg-agent       | NSG for agent subnet              |
| VM             | d01-devops-dev-vm-agent01      | DevOps agent VM                   |
| Storage        | d01devopsprodsa                | Storage account for prod          |
| Key Vault      | d01-devops-prod-kv             | Key Vault for prod                |
| Resource Group | d01-devops-dev-rg              | Resource group for dev            |

## Subscription Code Mapping (Prefix Limit: 3 Characters)
| Code | Subscription Name         | Subscription ID (partial) |
|------|--------------------------|---------------------------|
| d01  | DevOps Dev Subscription  | 1234-5678-...             |
| p01  | DevOps Prod Subscription | abcd-efgh-...             |
| t01  | DevOps Test Subscription | 9876-5432-...             |

> **Note:** Always use a unique, memorable 3-character code for each subscription. Document the mapping in this table and use the code as the prefix in all resource names.

## Resource Type Abbreviations
- vnet: Virtual Network
- snet: Subnet
- nsg: Network Security Group
- vm: Virtual Machine
- sa: Storage Account
- kv: Key Vault
- rg: Resource Group
- pip: Public IP
- nic: Network Interface
- app: Application

## Best Practices
- Use only lowercase letters, numbers, and hyphens
- Avoid Azure reserved words and special characters
- Keep names under Azure’s length limits for each resource type
- Use tags for additional metadata (owner, cost center, etc.)

## References
- [Microsoft Azure Naming Tool](https://namingsamples.azurewebsites.net/)
- [Azure Naming Rules and Restrictions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules)
