
// -----------------------------------------------------------------------------
// Input Variables for Azure DevOps Agent Module
// -----------------------------------------------------------------------------

variable "agent_name" {
  description = "The name of the Azure DevOps agent virtual machine."
  type        = string
}

variable "location" {
  description = "The Azure region where the resources will be deployed."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the resources."
  type        = string
}

variable "vm_size" {
  description = "The size (SKU) of the virtual machine."
  type        = string
  default     = "Standard_B2ms"
}

variable "admin_username" {
  description = "The admin username for the virtual machine."
  type        = string
}

variable "admin_password" {
  description = "The admin password for the virtual machine."
  type        = string
  sensitive   = true
}

variable "subnet_id" {
  description = "The subnet ID where the network interface will be created."
  type        = string
}
