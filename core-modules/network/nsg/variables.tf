variable "tags" {
  description = "A map of tags to assign to the NSG."
  type        = map(string)
  default     = {}
}

variable "allow_ssh" {
  description = "Whether to allow SSH (port 22) inbound."
  type        = bool
  default     = false
}

variable "allowed_ssh_source" {
  description = "Source IP CIDR(s) allowed for SSH."
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "allow_rdp" {
  description = "Whether to allow RDP (port 3389) inbound."
  type        = bool
  default     = false
}

variable "allowed_rdp_source" {
  description = "Source IP CIDR(s) allowed for RDP."
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

// -----------------------------------------------------------------------------
// Input Variables for NSG Module
// -----------------------------------------------------------------------------

variable "name" {
  description = "The name of the Azure Network Security Group (NSG)."
  type        = string
}

variable "location" {
  description = "The Azure region where the NSG will be created."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the NSG."
  type        = string
}
