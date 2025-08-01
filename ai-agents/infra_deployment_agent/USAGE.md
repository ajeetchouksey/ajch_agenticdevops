# Azure Infrastructure Deployment Workflow

This GitHub Actions workflow automates the deployment of Azure infrastructure using AI-driven decision making, implementing the requirements described in `AI_Agent_Infra_Build.md`.

## Features

✅ **Automated Azure Infrastructure Deployment**
- Resource group creation
- Virtual machine deployment (template ready)
- Network interface and public IP setup

✅ **AI-Driven Decision Logic**
- Integration with LangChain framework
- OpenAI-powered deployment decisions
- Fallback to default logic when AI is unavailable

✅ **Flexible Configuration**
- Manual workflow dispatch with input parameters
- Automatic trigger on code changes
- Environment variable configuration

✅ **Comprehensive Error Handling**
- Detailed logging and error reporting
- Deployment verification steps
- Artifact collection for troubleshooting

## Workflow Triggers

### Manual Trigger
The workflow can be triggered manually via GitHub Actions UI with the following parameters:

- **Resource Group Name**: Name for the Azure resource group (default: `AI_Agent_RG`)
- **Location**: Azure region for deployment (default: `eastus`)
- **VM Name**: Virtual machine name (default: `MyAIInfraVM`)
- **VM Size**: Virtual machine size (default: `Standard_DS1_v2`)
- **Admin Username**: VM administrator username (default: `azureuser`)
- **Enable AI Decisions**: Whether to use AI for deployment decisions (default: `true`)

### Automatic Trigger
The workflow automatically triggers on:
- Push to `main` branch
- Changes to workflow file or agent code in `ai-agents/infra_deployment_agent/`

## Prerequisites

### Required Secrets
Configure the following secrets in your GitHub repository:

1. **`AZURE_CREDENTIALS`** - Azure service principal credentials in JSON format:
   ```json
   {
     "clientId": "your-client-id",
     "clientSecret": "your-client-secret",
     "subscriptionId": "your-subscription-id",
     "tenantId": "your-tenant-id"
   }
   ```

2. **`AZURE_SUBSCRIPTION_ID`** - Your Azure subscription ID

3. **`VM_ADMIN_PASSWORD`** - Secure password for VM administrator account

4. **`OPENAI_API_KEY`** - OpenAI API key for AI decision logic (optional)

### Azure Service Principal Setup
Create a service principal with contributor access:

```bash
# Create service principal
az ad sp create-for-rbac --name "github-actions-sp" \
  --role contributor \
  --scopes /subscriptions/{subscription-id} \
  --sdk-auth

# The output should be stored as AZURE_CREDENTIALS secret
```

## Usage

### 1. Manual Deployment
1. Go to Actions tab in your GitHub repository
2. Select "Deploy Azure Infrastructure" workflow
3. Click "Run workflow"
4. Configure parameters as needed
5. Click "Run workflow" to start deployment

### 2. Automatic Deployment
Push changes to the `ai-agents/infra_deployment_agent/` directory or the main branch to trigger automatic deployment.

### 3. Local Testing
To test the deployment script locally:

```bash
# Clone the repository
git clone <repository-url>
cd ajch_agenticdevops/ai-agents/infra_deployment_agent

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export AZURE_SUBSCRIPTION_ID="your-subscription-id"
export RESOURCE_GROUP_NAME="test-rg"
export LOCATION="eastus"
export VM_NAME="test-vm"

# Authenticate with Azure
az login

# Run the deployment script
python azure_infra_deploy.py
```

## Configuration

### Environment Variables
The deployment script uses the following environment variables:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `AZURE_SUBSCRIPTION_ID` | Azure subscription ID | - | Yes |
| `RESOURCE_GROUP_NAME` | Resource group name | `AI_Agent_RG` | No |
| `LOCATION` | Azure region | `eastus` | No |
| `VM_NAME` | Virtual machine name | `MyAIInfraVM` | No |
| `VM_SIZE` | VM size | `Standard_DS1_v2` | No |
| `ADMIN_USERNAME` | VM admin username | `azureuser` | No |
| `VM_ADMIN_PASSWORD` | VM admin password | - | Yes |
| `OPENAI_API_KEY` | OpenAI API key | - | No |

### AI Decision Logic
When `OPENAI_API_KEY` is configured, the system uses AI to make intelligent decisions about:
- Whether to create resource groups
- Whether to deploy virtual machines
- Resource optimization recommendations

Without the API key, the system uses conservative default decisions.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Actions Workflow                  │
├─────────────────────────────────────────────────────────────┤
│ 1. Setup Python Environment                                │
│ 2. Install Azure SDK + LangChain Dependencies              │
│ 3. Authenticate with Azure                                 │
│ 4. Run Azure Infrastructure Deployment Agent               │
│ 5. Verify Deployment                                       │
│ 6. Collect Logs and Artifacts                              │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│           Azure Infrastructure Deployment Agent             │
├─────────────────────────────────────────────────────────────┤
│ • AI Decision Logic (LangChain + OpenAI)                   │
│ • Azure Resource Management                                │
│ • Error Handling & Logging                                 │
│ • Configuration Management                                 │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      Azure Resources                        │
├─────────────────────────────────────────────────────────────┤
│ • Resource Groups                                           │
│ • Virtual Machines                                          │
│ • Network Interfaces                                        │
│ • Public IP Addresses                                       │
└─────────────────────────────────────────────────────────────┘
```

## Troubleshooting

### Common Issues

1. **Authentication Failures**
   - Verify `AZURE_CREDENTIALS` secret is correctly formatted
   - Ensure service principal has sufficient permissions
   - Check subscription ID is correct

2. **Deployment Failures**
   - Review deployment logs in workflow artifacts
   - Check Azure resource quotas and limits
   - Verify location supports selected VM sizes

3. **AI Decision Logic Issues**
   - Verify `OPENAI_API_KEY` is valid
   - Check OpenAI API rate limits
   - Review AI decision prompts in logs

### Debugging
1. Download workflow artifacts containing deployment logs
2. Enable debug logging by setting environment variable `AZURE_CORE_LOGGING_ENABLE=1`
3. Use Azure CLI to check resource states manually

## Security Considerations

- Store all sensitive information in GitHub Secrets
- Use least-privilege service principal permissions
- Regularly rotate service principal credentials
- Monitor Azure resource usage and costs
- Review AI decision logs for unexpected behavior

## Limitations

- Current VM deployment is template-based (requires network setup completion)
- AI decisions are currently demonstration-level (can be enhanced)
- Single VM deployment (can be extended for multiple resources)
- Basic error recovery (can be enhanced with rollback logic)

## Extension Points

The workflow is designed to be extensible:

1. **Additional Azure Resources**: Extend the Python script to deploy databases, storage accounts, etc.
2. **Enhanced AI Logic**: Improve AI decision-making with more sophisticated prompts
3. **Multi-Environment Support**: Add staging/production environment configurations
4. **Cost Optimization**: Add cost analysis and optimization recommendations
5. **Compliance Checks**: Integrate policy compliance validation

## Contributing

To contribute improvements:

1. Fork the repository
2. Create a feature branch
3. Test changes locally using the test script
4. Submit a pull request with detailed description

For questions or issues, please create a GitHub issue with:
- Workflow run ID
- Error messages or logs
- Configuration details (sanitized)