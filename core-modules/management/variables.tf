variable "log_analytics_name" {}
variable "location" {}
variable "resource_group_name" {}
variable "log_analytics_sku" { default = "PerGB2018" }
variable "retention_in_days" { default = 30 }
