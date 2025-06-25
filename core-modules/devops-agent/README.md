# DevOps Agent Module

This module deploys a Linux virtual machine to be used as a self-hosted Azure DevOps agent. It creates a network interface and a VM in a specified subnet and resource group.

## Resources Created
- `azurerm_network_interface.devops_agent_nic`: Network interface for the DevOps agent VM
- `azurerm_linux_virtual_machine.devops_agent`: Linux VM for the DevOps agent

## Variables
| Name                | Description                                         | Default            |
|---------------------|-----------------------------------------------------|--------------------|
| agent_name          | The name of the Azure DevOps agent VM               | -                  |
| location            | The Azure region for deployment                     | -                  |
| resource_group_name | The resource group in which to create the resources | -                  |
| vm_size             | The size of the virtual machine                     | Standard_B2ms      |
| admin_username      | The admin username for the VM                       | -                  |
| admin_password      | The admin password for the VM                       | -                  |
| subnet_id           | The subnet ID for the network interface             | -                  |

## Usage Example
```hcl
module "devops_agent" {
  source              = "../../core-modules/devops-agent"
  agent_name          = "devops-agent-01"
  location            = var.location
  resource_group_name = var.resource_group_name
  vm_size             = "Standard_B2ms"
  admin_username      = var.admin_username
  admin_password      = var.admin_password
  subnet_id           = var.subnet_id
}
```

## Notes
- The VM is provisioned with Ubuntu 20.04 LTS.
- Ensure the subnet and resource group exist before using this module.
