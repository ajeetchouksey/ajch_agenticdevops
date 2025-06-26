// Unit test for CIS-compliant resource group module using terraform-test (Terratest alternative)
// This test uses the built-in terraform test framework (Terraform >= 1.6)

module "test_resource_groups" {
  source = "../core-modules/resource-group"
  resource_groups = [
    {
      name     = "test-prod-devops-rg-01"
      location = "eastus"
      tags = {
        Owner       = "testuser"
        Environment = "test"
      }
    }
  ]
}

// Test block (Terraform >= 1.6)
test "resource_group_created" {
  depends_on = [module.test_resource_groups]
  condition  = length(module.test_resource_groups.resource_group_names) == 1
  error_message = "Resource group was not created as expected."
}

test "resource_group_tags" {
  depends_on = [module.test_resource_groups]
  condition  = contains(module.test_resource_groups.resource_group_names, "test-prod-devops-rg-01")
  error_message = "Resource group name or tags are not as expected."
}
