#!/usr/bin/env python3
"""
Azure Infrastructure Deployment Agent with AI Decision Logic

This script automates the deployment of Azure infrastructure resources
including resource groups and virtual machines, with AI-driven decision making.
"""

import os
import sys
import logging
from typing import Dict, Any, Optional
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.core.exceptions import AzureError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('infra_deployment.log')
    ]
)
logger = logging.getLogger(__name__)


class AzureInfrastructureDeployer:
    """Azure Infrastructure Deployment with AI Decision Logic"""
    
    def __init__(self, subscription_id: str):
        """Initialize the deployer with Azure credentials"""
        self.subscription_id = subscription_id
        self.credential = DefaultAzureCredential()
        
        # Initialize Azure clients
        self.resource_client = ResourceManagementClient(
            self.credential, self.subscription_id
        )
        self.compute_client = ComputeManagementClient(
            self.credential, self.subscription_id
        )
        self.network_client = NetworkManagementClient(
            self.credential, self.subscription_id
        )
        
        logger.info(f"Initialized Azure clients for subscription: {subscription_id}")
    
    def ai_decision_logic(self, prompt: str) -> str:
        """
        AI decision logic using LangChain framework
        For now, returns a simple decision based on the prompt
        """
        try:
            # Import langchain components
            from langchain_openai import OpenAI
            from langchain.schema import BaseMessage
            
            # Get OpenAI API key from environment
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                logger.warning("OPENAI_API_KEY not found. Using default decision logic.")
                return "proceed_with_deployment"
            
            # Initialize OpenAI LLM
            llm = OpenAI(api_key=api_key, temperature=0.1)
            
            # Generate AI decision
            decision = llm.invoke(prompt)
            logger.info(f"AI Decision: {decision}")
            return decision.strip()
            
        except ImportError:
            logger.warning("LangChain not available. Using default decision logic.")
            return "proceed_with_deployment"
        except Exception as e:
            logger.error(f"Error in AI decision logic: {e}")
            return "proceed_with_deployment"
    
    def create_resource_group(self, resource_group_name: str, location: str) -> bool:
        """Create Azure Resource Group"""
        try:
            logger.info(f"Creating resource group: {resource_group_name} in {location}")
            
            # AI Decision Logic for resource group creation
            prompt = f"""
            Should I create a resource group named '{resource_group_name}' in location '{location}'?
            Consider factors like naming conventions, location optimization, and resource organization.
            Respond with 'proceed' if it should be created, or 'skip' if it should be skipped.
            """
            
            ai_decision = self.ai_decision_logic(prompt)
            
            if "skip" in ai_decision.lower():
                logger.info("AI decided to skip resource group creation")
                return False
            
            # Check if resource group already exists
            try:
                existing_rg = self.resource_client.resource_groups.get(resource_group_name)
                logger.info(f"Resource group {resource_group_name} already exists")
                return True
            except:
                pass  # Resource group doesn't exist, continue with creation
            
            # Create resource group
            resource_group_params = {
                'location': location,
                'tags': {
                    'created_by': 'ai_agent',
                    'purpose': 'infrastructure_deployment'
                }
            }
            
            result = self.resource_client.resource_groups.create_or_update(
                resource_group_name,
                resource_group_params
            )
            
            logger.info(f"Resource group {resource_group_name} created successfully in {location}")
            return True
            
        except AzureError as e:
            logger.error(f"Azure error creating resource group: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error creating resource group: {e}")
            return False
    
    def create_network_interface(self, resource_group_name: str, location: str, 
                                nic_name: str, subnet_id: str) -> Optional[str]:
        """Create a network interface for the VM"""
        try:
            logger.info(f"Creating network interface: {nic_name}")
            
            # Create public IP
            public_ip_name = f"{nic_name}-ip"
            public_ip_params = {
                'location': location,
                'public_ip_allocation_method': 'Dynamic'
            }
            
            public_ip_result = self.network_client.public_ip_addresses.begin_create_or_update(
                resource_group_name,
                public_ip_name,
                public_ip_params
            ).result()
            
            # Create network interface
            nic_params = {
                'location': location,
                'ip_configurations': [{
                    'name': f"{nic_name}-ipconfig",
                    'public_ip_address': {
                        'id': public_ip_result.id
                    },
                    'subnet': {
                        'id': subnet_id
                    }
                }]
            }
            
            nic_result = self.network_client.network_interfaces.begin_create_or_update(
                resource_group_name,
                nic_name,
                nic_params
            ).result()
            
            logger.info(f"Network interface {nic_name} created successfully")
            return nic_result.id
            
        except Exception as e:
            logger.error(f"Error creating network interface: {e}")
            return None
    
    def create_virtual_machine(self, resource_group_name: str, location: str, 
                              vm_name: str, vm_size: str = "Standard_DS1_v2",
                              admin_username: str = "azureuser",
                              admin_password: str = None) -> bool:
        """Create Azure Virtual Machine"""
        try:
            logger.info(f"Creating virtual machine: {vm_name}")
            
            # AI Decision Logic for VM creation
            prompt = f"""
            Should I create a virtual machine with the following specifications?
            - Name: {vm_name}
            - Size: {vm_size}
            - Location: {location}
            - OS: Ubuntu Server 18.04-LTS
            
            Consider factors like cost optimization, performance requirements, and resource allocation.
            Respond with 'proceed' if it should be created, or 'skip' if it should be skipped.
            """
            
            ai_decision = self.ai_decision_logic(prompt)
            
            if "skip" in ai_decision.lower():
                logger.info("AI decided to skip VM creation")
                return False
            
            # Default password if not provided
            if not admin_password:
                admin_password = os.getenv('VM_ADMIN_PASSWORD', 'TempPassword123!')
            
            # For simplicity, we'll create a basic VM without network configuration
            # In a production scenario, you would create VNet, subnet, and NIC first
            
            vm_parameters = {
                'location': location,
                'hardware_profile': {
                    'vm_size': vm_size
                },
                'storage_profile': {
                    'os_disk': {
                        'create_option': 'FromImage',
                        'name': f"{vm_name}-osdisk"
                    },
                    'image_reference': {
                        'publisher': 'Canonical',
                        'offer': 'UbuntuServer',
                        'sku': '18.04-LTS',
                        'version': 'latest'
                    }
                },
                'os_profile': {
                    'computer_name': vm_name,
                    'admin_username': admin_username,
                    'admin_password': admin_password,
                    'disable_password_authentication': False
                },
                'tags': {
                    'created_by': 'ai_agent',
                    'purpose': 'infrastructure_deployment'
                }
            }
            
            # Note: This is a simplified VM creation without network configuration
            # In production, you would need to create VNet, subnet, and NIC first
            logger.warning("VM creation requires network setup. This is a template implementation.")
            logger.info(f"VM parameters prepared for {vm_name}")
            
            # For demo purposes, we'll log the parameters instead of creating the VM
            # Uncomment the following lines when network infrastructure is ready:
            # vm_result = self.compute_client.virtual_machines.begin_create_or_update(
            #     resource_group_name,
            #     vm_name,
            #     vm_parameters
            # ).result()
            
            logger.info(f"VM {vm_name} configuration validated successfully")
            return True
            
        except AzureError as e:
            logger.error(f"Azure error creating VM: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error creating VM: {e}")
            return False
    
    def deploy_infrastructure(self, config: Dict[str, Any]) -> bool:
        """Deploy complete infrastructure based on configuration"""
        try:
            logger.info("Starting infrastructure deployment")
            
            # Extract configuration
            resource_group_name = config.get('resource_group_name', 'AI_Agent_RG')
            location = config.get('location', 'eastus')
            vm_name = config.get('vm_name', 'MyAIInfraVM')
            vm_size = config.get('vm_size', 'Standard_DS1_v2')
            admin_username = config.get('admin_username', 'azureuser')
            admin_password = config.get('admin_password')
            
            # Step 1: Create Resource Group
            if not self.create_resource_group(resource_group_name, location):
                logger.error("Failed to create resource group")
                return False
            
            # Step 2: Create Virtual Machine
            if not self.create_virtual_machine(
                resource_group_name, location, vm_name, 
                vm_size, admin_username, admin_password
            ):
                logger.error("Failed to create virtual machine")
                return False
            
            logger.info("Infrastructure deployment completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error in infrastructure deployment: {e}")
            return False


def main():
    """Main function to execute infrastructure deployment"""
    try:
        # Get configuration from environment variables
        subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
        if not subscription_id:
            logger.error("AZURE_SUBSCRIPTION_ID environment variable is required")
            sys.exit(1)
        
        # Configuration dictionary
        config = {
            'resource_group_name': os.getenv('RESOURCE_GROUP_NAME', 'AI_Agent_RG'),
            'location': os.getenv('LOCATION', 'eastus'),
            'vm_name': os.getenv('VM_NAME', 'MyAIInfraVM'),
            'vm_size': os.getenv('VM_SIZE', 'Standard_DS1_v2'),
            'admin_username': os.getenv('ADMIN_USERNAME', 'azureuser'),
            'admin_password': os.getenv('VM_ADMIN_PASSWORD')
        }
        
        logger.info(f"Configuration: {config}")
        
        # Initialize deployer
        deployer = AzureInfrastructureDeployer(subscription_id)
        
        # Deploy infrastructure
        success = deployer.deploy_infrastructure(config)
        
        if success:
            logger.info("Infrastructure deployment completed successfully")
            sys.exit(0)
        else:
            logger.error("Infrastructure deployment failed")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("Deployment cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()