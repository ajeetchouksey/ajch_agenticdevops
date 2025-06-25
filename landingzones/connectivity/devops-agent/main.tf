
// -----------------------------------------------------------------------------
// Main entry for DevOps Agent deployment in Connectivity Landing Zone
// This composition file wires together modular core network and agent modules.
// It demonstrates best practices for modularity, reusability, and compliance.
// -----------------------------------------------------------------------------

// Create Virtual Network (VNet)
module "vnet" {
  source              = "../../../core-modules/network/vnet"
  name                = var.vnet_name
  address_space       = var.vnet_address_space
  location            = var.location
  resource_group_name = var.resource_group_name
}

// Create Subnet within the VNet
module "subnet" {
  source               = "../../../core-modules/network/subnet"
  name                 = var.subnet_name
  resource_group_name  = var.resource_group_name
  virtual_network_name = module.vnet.vnet_name
  address_prefixes     = var.subnet_address_prefixes
}

// Create Network Security Group (NSG)
module "nsg" {
  source              = "../../../core-modules/network/nsg"
  name                = var.nsg_name
  location            = var.location
  resource_group_name = var.resource_group_name
}

// Associate NSG with Subnet for security best practices
resource "azurerm_subnet_network_security_group_association" "devops_subnet_nsg" {
  subnet_id                 = module.subnet.subnet_id
  network_security_group_id = module.nsg.nsg_id
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
  subnet_id           = module.subnet.subnet_id
}
