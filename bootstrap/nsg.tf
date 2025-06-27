module "devops_nsg" {
  source = "../core-modules/nsg"
  nsgs = [
    {
      name                = "${local.env}-${local.service_prefix}-nsg-01"
      location            = "westeurope"
      resource_group_name = module.devopsagent_resource_groups.resource_group_names[0]
    }
  ]
  tags = local.tags
}

# Example NSG rules for Azure DevOps agent VMSS
resource "azurerm_network_security_rule" "devops_agent_allow_outbound" {
  name                        = "AllowDevOpsOutbound"
  priority                    = 100
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = module.devopsagent_resource_groups.resource_group_names[0]
  network_security_group_name = module.devops_nsg.nsg_ids["${local.env}-${local.service_prefix}-nsg-01"]
}
