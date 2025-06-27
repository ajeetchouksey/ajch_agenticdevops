variable "vmss_list" {
  description = "List of VMSS definitions."
  type = list(object({
    name                    = string
    location                = string
    resource_group_name     = string
    sku                     = string
    instances               = number
    admin_username          = string
    admin_password          = string
    zones                   = list(string)
    disk_encryption_set_id  = string
    boot_diag_storage_uri   = string
    nic_name                = string
    ip_config_name          = string
    subnet_id               = string
    nsg_id                  = string
    # public_ip_address_id  = string (optional)
  }))
}

variable "tags" {
  description = "Tags to apply to resources."
  type        = map(string)
  default     = {}
}
