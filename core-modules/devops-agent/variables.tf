// Name of the DevOps agent VM
variable "agent_name" {
  description = "The name of the Azure DevOps agent virtual machine."
}

// Azure region for deployment
variable "location" {
  description = "The Azure region where the resources will be deployed."
}

// Resource group for the VM and NIC
variable "resource_group_name" {
  description = "The name of the resource group in which to create the resources."
}

// VM size (SKU)
variable "vm_size" {
  description = "The size of the virtual machine."
  default     = "Standard_B2ms"
}

// Admin username for the VM
variable "admin_username" {
  description = "The admin username for the virtual machine."
}

// Admin password for the VM
variable "admin_password" {
  description = "The admin password for the virtual machine."
}

// Subnet ID for the NIC
variable "subnet_id" {
  description = "The subnet ID where the network interface will be created."
}
