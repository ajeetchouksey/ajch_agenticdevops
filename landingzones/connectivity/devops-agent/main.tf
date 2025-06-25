// -----------------------------------------------------------------------------
// Main entry for DevOps Agent deployment in Connectivity Landing Zone
// This composition file wires together modular core network and agent modules.
// It demonstrates best practices for modularity, reusability, and compliance.
// -----------------------------------------------------------------------------

// Create Virtual Network(s) using naming convention from locals
module "vnet" {
  source = "../../../core-modules/network/vnet"
  vnets = {
    agent = {
      name                = local.vnet_name
      address_space       = var.vnet_address_space
      location            = var.location
      resource_group_name = var.resource_group_name
    }
  }
}

// Create Subnet(s) using naming convention from locals
module "subnet" {
  source  = "../../../core-modules/network/subnet"
  subnets = {
    agent = {
      name                 = local.subnet_name
      resource_group_name  = var.resource_group_name
      virtual_network_name = local.vnet_name
      address_prefixes     = var.subnet_address_prefixes
    }
  }
}

// Create Network Security Group(s) using naming convention from locals
module "nsg" {
  source = "../../../core-modules/network/nsg"
  nsgs = {
    agent = {
      name                = local.nsg_name
      location            = var.location
      resource_group_name = var.resource_group_name
      // tags and rules if needed
    }
  }
}

// Associate NSG with Subnet for security best practices
resource "azurerm_subnet_network_security_group_association" "agent" {
  subnet_id                 = module.subnet.subnet_ids["agent"]
  network_security_group_id = module.nsg.nsg_ids["agent"]
}

// Deploy the Azure DevOps Agent VM in the created subnet using naming convention from locals
module "devops_agent" {
  source              = "../../../core-modules/devops-agent"
  agent_name          = local.agent_name
  subscription_code   = var.subscription_code
  project             = var.project
  env                 = var.env
  location            = var.location
  resource_group_name = var.resource_group_name
  vm_size             = var.vm_size
  admin_username      = var.admin_username
  admin_password      = var.admin_password
  subnet_id           = module.subnet.subnet_ids["agent"]
}
