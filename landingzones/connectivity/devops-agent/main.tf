// Main entry for DevOps Agent deployment in connectivity landing zone
// Uses industry best practices for naming and modularity

module "devops_agent" {
  source              = "../../../core-modules/devops-agent"
  agent_name          = var.agent_name
  location            = var.location
  resource_group_name = var.resource_group_name
  vm_size             = var.vm_size
  admin_username      = var.admin_username
  admin_password      = var.admin_password
  subnet_id           = var.subnet_id
}
