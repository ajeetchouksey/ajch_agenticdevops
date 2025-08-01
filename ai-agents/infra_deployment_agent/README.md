# Infrastructure Deployment Agent

This agent automates Azure infrastructure deployment using AI-driven decision making.

## Features

- **Automated Resource Deployment**: Creates Azure resource groups and virtual machines
- **AI Decision Logic**: Uses LangChain framework for intelligent infrastructure decisions
- **Parameterized Configuration**: Flexible configuration through environment variables
- **Error Handling**: Comprehensive error handling and logging for debugging

## Dependencies

- Azure SDK for Python (azure-mgmt-resource, azure-mgmt-compute, azure-identity)
- LangChain framework for AI decision logic
- Additional utilities for logging and configuration

## Usage

This agent is designed to be executed within GitHub Actions workflows but can also be run locally with proper Azure credentials configured.