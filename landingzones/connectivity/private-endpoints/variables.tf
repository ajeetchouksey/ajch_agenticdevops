variable "resource_group_name" {
  description = "Resource group for private endpoints and DNS zones."
  type        = string
}

variable "location" {
  description = "Azure region."
  type        = string
}

variable "subnet_id" {
  description = "Subnet ID for private endpoints."
  type        = string
}

variable "storage_account_id" {
  description = "Resource ID of the storage account."
  type        = string
}

variable "keyvault_id" {
  description = "Resource ID of the Key Vault."
  type        = string
}

variable "subscription_code" {
  description = "3-character code for the subscription (see NAMING_CONVENTIONS.md)."
  type        = string
}

variable "project" {
  description = "Project or workload name."
  type        = string
}

variable "env" {
  description = "Environment name."
  type        = string
}
