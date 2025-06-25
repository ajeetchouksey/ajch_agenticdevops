// Variables for DevOps Agent deployment in connectivity landing zone

variable "agent_name" {
  description = "The name of the Azure DevOps agent virtual machine."
}

variable "location" {
  description = "The Azure region where the resources will be deployed."
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the resources."
}

variable "vm_size" {
  description = "The size of the virtual machine."
  default     = "Standard_B2ms"
}

variable "admin_username" {
  description = "The admin username for the virtual machine."
}

variable "admin_password" {
  description = "The admin password for the virtual machine."
}

variable "subnet_id" {
  description = "The subnet ID where the network interface will be created."
}
