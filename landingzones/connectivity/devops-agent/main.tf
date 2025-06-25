
// -----------------------------------------------------------------------------
// Main entry for DevOps Agent deployment in Connectivity Landing Zone
// This composition file wires together modular core network and agent modules.
// It demonstrates best practices for modularity, reusability, and compliance.
// -----------------------------------------------------------------------------


// Create Virtual Network (VNet) - map input, single instance example
module "vnet" {
  source = "../../../core-modules/network/vnet"
  vnets = {
    devops = {
      name                = var.vnet_name
      address_space       = var.vnet_address_space
      location            = var.location
      resource_group_name = var.resource_group_name
      tags                = {}
    }
  }
}

// Create Subnet within the VNet - map input, single instance example
module "subnet" {
  source = "../../../core-modules/network/subnet"
  subnets = {
    devops = {
      name                 = var.subnet_name
      resource_group_name  = var.resource_group_name
      virtual_network_name = module.vnet.vnet_names["devops"]
      address_prefixes     = var.subnet_address_prefixes
      tags                 = {}
    }
  }
}

// Create Network Security Group (NSG) - map input, single instance example
module "nsg" {
  source = "../../../core-modules/network/nsg"
  nsgs = {
    devops = {
      name                = var.nsg_name
      location            = var.location
      resource_group_name = var.resource_group_name
      tags                = {}
      rules = [
        // Example: allow SSH from anywhere (customize for security)
        {
          name                       = "Allow-SSH"
          priority                   = 1001
          direction                  = "Inbound"
          access                     = "Allow"
          protocol                   = "Tcp"
          source_port_range          = "*"
          destination_port_range     = "22"
          source_address_prefix      = "0.0.0.0/0"
          destination_address_prefix = "*"
        }
      ]
    }
  }
}

// Associate NSG with Subnet for security best practices
resource "azurerm_subnet_network_security_group_association" "devops_subnet_nsg" {
  subnet_id                 = module.subnet.subnet_ids["devops"]
  network_security_group_id = module.nsg.nsg_ids["devops"]
}

// Deploy the Azure DevOps Agent VM in the created subnet
module "devops_agent" {
  source              = "../../../core-modules/devops-agent"
  agent_name          = var.agent_name
  location            = var.location
  resource_group_name = var.resource_group_name
  vm_size             = var.vm_size
  admin_username      = var.admin_username
  admin_password      = var.admin_password
  subnet_id           = module.subnet.subnet_ids["devops"]
}
