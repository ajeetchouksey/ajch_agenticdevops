
variable "environment" {
  description = "The environment for deployment (e.g., dev, prod, p)"
  type        = string
}

variable "subscription_id" {
  description = "The Azure Subscription ID"
  type        = string
}

variable "tenant_id" {
  description = "The Azure Tenant ID"
  type        = string
}
