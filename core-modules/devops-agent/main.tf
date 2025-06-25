// Azure DevOps Self-hosted Agent Module
// This module deploys a Linux VM to be used as a self-hosted Azure DevOps agent.

// Network Interface for the DevOps agent VM
resource "azurerm_network_interface" "devops_agent_nic" {
  name                = "${var.agent_name}-nic"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
  }
}

// Linux Virtual Machine for the DevOps agent
resource "azurerm_linux_virtual_machine" "devops_agent" {
  name                = var.agent_name
  location            = var.location
  resource_group_name = var.resource_group_name
  size                = var.vm_size
  admin_username      = var.admin_username
  admin_password      = var.admin_password
  network_interface_ids = [azurerm_network_interface.devops_agent_nic.id]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-focal"
    sku       = "20_04-lts"
    version   = "latest"
  }
}
