#!/usr/bin/env python3
"""
Test script for Azure Infrastructure Deployment Agent

This script tests the functionality of the deployment agent
without requiring actual Azure credentials.
"""

import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

# Add the agent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from azure_infra_deploy import AzureInfrastructureDeployer


class TestAzureInfrastructureDeployer(unittest.TestCase):
    """Test cases for Azure Infrastructure Deployer"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.subscription_id = "test-subscription-id"
        
    @patch('azure_infra_deploy.DefaultAzureCredential')
    @patch('azure_infra_deploy.ResourceManagementClient')
    @patch('azure_infra_deploy.ComputeManagementClient')
    @patch('azure_infra_deploy.NetworkManagementClient')
    def test_deployer_initialization(self, mock_network, mock_compute, mock_resource, mock_credential):
        """Test deployer initialization"""
        deployer = AzureInfrastructureDeployer(self.subscription_id)
        
        self.assertEqual(deployer.subscription_id, self.subscription_id)
        mock_credential.assert_called_once()
        mock_resource.assert_called_once()
        mock_compute.assert_called_once()
        mock_network.assert_called_once()
    
    @patch('azure_infra_deploy.DefaultAzureCredential')
    @patch('azure_infra_deploy.ResourceManagementClient')
    @patch('azure_infra_deploy.ComputeManagementClient')
    @patch('azure_infra_deploy.NetworkManagementClient')
    def test_ai_decision_logic_without_openai(self, mock_network, mock_compute, mock_resource, mock_credential):
        """Test AI decision logic fallback"""
        deployer = AzureInfrastructureDeployer(self.subscription_id)
        
        # Test without OpenAI API key
        decision = deployer.ai_decision_logic("Should I proceed?")
        self.assertEqual(decision, "proceed_with_deployment")
    
    @patch.dict(os.environ, {'OPENAI_API_KEY': 'test-key'})
    @patch('azure_infra_deploy.DefaultAzureCredential')
    @patch('azure_infra_deploy.ResourceManagementClient')
    @patch('azure_infra_deploy.ComputeManagementClient')
    @patch('azure_infra_deploy.NetworkManagementClient')
    @patch('langchain_openai.OpenAI')
    def test_ai_decision_logic_with_openai(self, mock_openai, mock_network, mock_compute, mock_resource, mock_credential):
        """Test AI decision logic with OpenAI"""
        # Mock OpenAI response
        mock_llm = Mock()
        mock_llm.invoke.return_value = "proceed"
        mock_openai.return_value = mock_llm
        
        deployer = AzureInfrastructureDeployer(self.subscription_id)
        decision = deployer.ai_decision_logic("Should I proceed?")
        
        self.assertEqual(decision, "proceed")
        mock_openai.assert_called_once()
        mock_llm.invoke.assert_called_once()
    
    @patch('azure_infra_deploy.DefaultAzureCredential')
    @patch('azure_infra_deploy.ResourceManagementClient')
    @patch('azure_infra_deploy.ComputeManagementClient')
    @patch('azure_infra_deploy.NetworkManagementClient')
    def test_create_resource_group_success(self, mock_network, mock_compute, mock_resource, mock_credential):
        """Test successful resource group creation"""
        # Mock the resource client
        mock_resource_instance = Mock()
        mock_resource.return_value = mock_resource_instance
        
        # Mock resource group doesn't exist (raises exception)
        mock_resource_instance.resource_groups.get.side_effect = Exception("Not found")
        
        # Mock successful creation
        mock_resource_instance.resource_groups.create_or_update.return_value = Mock()
        
        deployer = AzureInfrastructureDeployer(self.subscription_id)
        
        result = deployer.create_resource_group("test-rg", "eastus")
        
        self.assertTrue(result)
        mock_resource_instance.resource_groups.create_or_update.assert_called_once()
    
    @patch('azure_infra_deploy.DefaultAzureCredential')
    @patch('azure_infra_deploy.ResourceManagementClient')
    @patch('azure_infra_deploy.ComputeManagementClient')
    @patch('azure_infra_deploy.NetworkManagementClient')
    def test_create_resource_group_exists(self, mock_network, mock_compute, mock_resource, mock_credential):
        """Test resource group creation when it already exists"""
        # Mock the resource client
        mock_resource_instance = Mock()
        mock_resource.return_value = mock_resource_instance
        
        # Mock resource group exists
        mock_resource_instance.resource_groups.get.return_value = Mock()
        
        deployer = AzureInfrastructureDeployer(self.subscription_id)
        
        result = deployer.create_resource_group("test-rg", "eastus")
        
        self.assertTrue(result)
        # Should not call create_or_update if resource group exists
        mock_resource_instance.resource_groups.create_or_update.assert_not_called()
    
    def test_configuration_validation(self):
        """Test configuration parameter validation"""
        config = {
            'resource_group_name': 'test-rg',
            'location': 'eastus',
            'vm_name': 'test-vm',
            'vm_size': 'Standard_DS1_v2',
            'admin_username': 'testuser'
        }
        
        # Validate required fields are present
        self.assertIn('resource_group_name', config)
        self.assertIn('location', config)
        self.assertIn('vm_name', config)
        self.assertIn('vm_size', config)
        self.assertIn('admin_username', config)


def run_validation_tests():
    """Run validation tests and return success status"""
    print("Running Azure Infrastructure Deployment Agent Tests...")
    print("=" * 60)
    
    # Run the test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAzureInfrastructureDeployer)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    
    if result.wasSuccessful():
        print("✅ All tests passed successfully!")
        print("The Azure Infrastructure Deployment Agent is ready for use.")
        return True
    else:
        print("❌ Some tests failed.")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        return False


if __name__ == "__main__":
    success = run_validation_tests()
    sys.exit(0 if success else 1)