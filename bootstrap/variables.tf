
variable "environment" {
  description = "The environment for deployment (e.g., dev, prod, test)"
  type        = string
  default     = "prod"
}

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
  default     = {
    Owner       = "admin"
    Environment = "prod"
  }
}
