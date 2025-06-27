variable "location" {
  description = "The Azure region for resource deployment."
  type        = string
  default     = "eastus"
}

variable "owner" {
  description = "The owner of the resources."
  type        = string
  default     = "admin"
}

variable "tags" {
  description = "A map of tags to apply to resources."
  type        = map(string)
  default = {
    Owner       = "admin"
    Environment = "prod"
  }
}

variable "vmss_admin_username" {
  description = "Admin username for VMSS VMs."
  type        = string
}

variable "vmss_admin_password" {
  description = "Admin password for VMSS VMs."
  type        = string
  sensitive   = true
}

variable "disk_encryption_set_id" {
  description = "Disk Encryption Set ID for OS disk encryption."
  type        = string
}

variable "boot_diag_storage_uri" {
  description = "Storage account URI for boot diagnostics."
  type        = string
}

