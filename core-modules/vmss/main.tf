# VMSS Module - CIS Compliant
resource "azurerm_linux_virtual_machine_scale_set" "this" {
  for_each            = { for v in var.vmss_list : v.name => v }
  name                = each.value.name
  location            = each.value.location
  resource_group_name = each.value.resource_group_name
  sku                 = each.value.sku
  instances           = each.value.instances
  admin_username      = each.value.admin_username
  admin_password      = each.value.admin_password
  disable_password_authentication = false
  upgrade_mode        = "Manual"
  zones               = each.value.zones
  tags                = var.tags

  # CIS: Enable encryption at host
  encryption_at_host_enabled = true

  # CIS: Enable secure boot and vTPM
  security_profile {
    secure_boot_enabled = true
    vtpm_enabled        = true
  }

  # CIS: Enable OS disk encryption
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
    disk_encryption_set_id = each.value.disk_encryption_set_id
  }

  # CIS: Enable boot diagnostics
  boot_diagnostics {
    storage_account_uri = each.value.boot_diag_storage_uri
  }

  # CIS: Restrict public IP
  public_ip_address_configuration {
    name = ""
    idle_timeout_in_minutes = 4
    # Do not assign unless required
    # public_ip_address_id = each.value.public_ip_address_id
  }

  # CIS: Network profile
  network_interface {
    name    = each.value.nic_name
    primary = true
    ip_configuration {
      name      = each.value.ip_config_name
      subnet_id = each.value.subnet_id
      # No public IP by default
    }
    network_security_group_id = each.value.nsg_id
  }
}
