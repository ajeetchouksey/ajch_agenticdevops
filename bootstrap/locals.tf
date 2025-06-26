
# Naming convention locals for bootstrap
locals {
  rg_prefix  = "rg"
  law_prefix = "log"

  # Use variables for environment and owner
  env   = var.environment
  owner = var.owner
  tags  = var.tags

  # Resource group naming
  rg_name = "${local.rg_prefix}-${local.env}-01"

  # Add more resource naming conventions as needed
}
