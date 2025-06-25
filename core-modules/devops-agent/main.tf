
// -----------------------------------------------------------------------------
// Azure DevOps Self-hosted Agent Module
// This module deploys a Linux VM to be used as a self-hosted Azure DevOps agent.
// It creates a network interface in the specified subnet and provisions a VM with
// secure credentials and best practices for modularity and reusability.
// -----------------------------------------------------------------------------

// Network Interface for the DevOps agent VM
resource "azurerm_network_interface" "devops_agent_nic" {
  name                = "${var.agent_name}-nic"         // NIC name
  location            = var.location                    // Azure region
  resource_group_name = var.resource_group_name         // Resource group

  ip_configuration {
    name                          = "internal"          // IP config name
    subnet_id                     = var.subnet_id       // Subnet for NIC
    private_ip_address_allocation = "Dynamic"           // Dynamic IP
  }
}

// Linux Virtual Machine for the DevOps agent
resource "azurerm_linux_virtual_machine" "devops_agent" {
  name                = var.agent_name                  // VM name
  location            = var.location                    // Azure region
  resource_group_name = var.resource_group_name         // Resource group
  size                = var.vm_size                     // VM size (SKU)
  admin_username      = var.admin_username              // Admin username
  admin_password      = var.admin_password              // Admin password (sensitive)
  network_interface_ids = [azurerm_network_interface.devops_agent_nic.id] // Attach NIC

  os_disk {
    caching              = "ReadWrite"                  // Disk caching
    storage_account_type = "Standard_LRS"               // Storage type
  }

  source_image_reference {
    publisher = "Canonical"                             // Ubuntu publisher
    offer     = "0001-com-ubuntu-server-focal"          // Ubuntu offer
    sku       = "20_04-lts"                             // Ubuntu SKU
    version   = "latest"                                // Latest version
  }
}
