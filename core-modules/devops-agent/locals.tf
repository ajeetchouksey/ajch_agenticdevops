// Locals for naming convention (can be overridden by input variable if needed)
locals {
  agent_name_final = var.agent_name != null && var.agent_name != "" ? var.agent_name : "${var.subscription_code}-${var.project}-${var.env}-vm-agent01"
  nic_name        = "${local.agent_name_final}-nic"
}
