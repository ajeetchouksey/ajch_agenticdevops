#!/usr/bin/env python3
"""
Example script demonstrating how to use the Azure Infrastructure Deployment Agent
This script shows the basic configuration and usage patterns.
"""

import os
import sys
from azure_infra_deploy import AzureInfrastructureDeployer


def main():
    """Example usage of the Azure Infrastructure Deployment Agent"""
    print("Azure Infrastructure Deployment Agent - Example Usage")
    print("=" * 60)
    
    # Example configuration
    config = {
        'resource_group_name': 'Example_AI_Agent_RG',
        'location': 'eastus',
        'vm_name': 'ExampleVM',
        'vm_size': 'Standard_B1s',  # Smaller size for testing
        'admin_username': 'exampleuser',
        'admin_password': 'ExamplePassword123!'  # Use secure password in production
    }
    
    print("Example Configuration:")
    for key, value in config.items():
        if 'password' in key.lower():
            print(f"  {key}: {'*' * len(str(value))}")
        else:
            print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("NOTE: This is a demonstration script.")
    print("To run actual deployment, you need:")
    print("1. Valid Azure subscription and credentials")
    print("2. Proper environment variables set")
    print("3. Azure CLI authentication or service principal")
    print("=" * 60)
    
    # Check if we have Azure credentials
    subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
    if not subscription_id:
        print("\n⚠️  AZURE_SUBSCRIPTION_ID not set.")
        print("   This is required for actual deployment.")
        print("   Set environment variables using config.env.template")
        return
    
    try:
        print(f"\n✅ Found Azure subscription ID: {subscription_id[:8]}...")
        print("   Initializing deployment agent...")
        
        # Initialize the deployer
        deployer = AzureInfrastructureDeployer(subscription_id)
        
        print("✅ Azure Infrastructure Deployment Agent initialized successfully!")
        print("\nTo run actual deployment:")
        print("1. Set all required environment variables")
        print("2. Authenticate with Azure (az login)")
        print("3. Run: python azure_infra_deploy.py")
        
    except Exception as e:
        print(f"\n❌ Error initializing deployer: {e}")
        print("   Make sure you have Azure credentials configured.")


if __name__ == "__main__":
    main()