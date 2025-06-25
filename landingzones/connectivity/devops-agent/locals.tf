// Locals for naming convention (with subscription code)
locals {
  subscription_code = var.subscription_code
  project = var.project
  env     = var.env
  vnet_name   = "${local.subscription_code}-${local.project}-${local.env}-vnet"
  subnet_name = "${local.subscription_code}-${local.project}-${local.env}-snet-agent"
  nsg_name    = "${local.subscription_code}-${local.project}-${local.env}-nsg-agent"
  agent_name  = "${local.subscription_code}-${local.project}-${local.env}-vm-agent01"
  rg_name     = "${local.subscription_code}-${local.project}-${local.env}-rg"
}
