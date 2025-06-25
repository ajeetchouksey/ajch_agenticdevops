
// -----------------------------------------------------------------------------
// Main entry for DevOps Agent deployment in Connectivity Landing Zone
// This composition file wires together modular core network and agent modules.
// It demonstrates best practices for modularity, reusability, and compliance.
// -----------------------------------------------------------------------------



// Create Virtual Network(s)
module "vnet" {
  source = "../../../core-modules/network/vnet"
  vnets  = var.vnets
}

// Create Subnet(s)
module "subnet" {
  source  = "../../../core-modules/network/subnet"
  subnets = var.subnets
}

// Create Network Security Group(s)
module "nsg" {
  source = "../../../core-modules/network/nsg"
  nsgs   = var.nsgs
}

// Associate NSG with Subnet for security best practices
resource "azurerm_subnet_network_security_group_association" "agent" {
  subnet_id                 = module.subnet.subnet_ids["agent"]
  network_security_group_id = module.nsg.nsg_ids["agent"]
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
  subnet_id           = module.subnet.subnet_ids["agent"]
}
