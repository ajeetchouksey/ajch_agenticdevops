# Agent Configuration Guide

This guide provides comprehensive configuration instructions for all autonomous DevOps agents in the human-on-the-sidelines framework.

## Global Configuration

### Core Environment Variables

```bash
# AI Model Configuration (Required for all agents)
AI_API_KEY="your-openai-or-azure-openai-key"
AI_API_URL="https://your-ai-endpoint.com/v1"

# GitHub Integration (Required for CI/CD and Code Quality agents)
GITHUB_TOKEN="your-github-personal-access-token"
GITHUB_REPOSITORY="your-org/your-repo"

# Azure Integration (Required for Infrastructure and Cost agents)
AZURE_CLIENT_ID="your-azure-service-principal-client-id"
AZURE_TENANT_ID="your-azure-tenant-id"
AZURE_CLIENT_SECRET="your-azure-service-principal-secret"
AZURE_SUBSCRIPTION_ID="your-azure-subscription-id"

# Notification Channels (Optional but recommended)
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
TEAMS_WEBHOOK_URL="https://your-org.webhook.office.com/webhookb2/your-webhook"
EMAIL_NOTIFICATIONS="devops-team@your-company.com"
```

### Agent Operation Modes

All agents support two operation modes:

- **Monitor Mode**: Agents observe and recommend but don't execute actions
- **Autonomous Mode**: Agents execute actions within configured parameters

Start with monitor mode and gradually enable autonomous operations.

## CI/CD Orchestration Agent Configuration

### Basic Configuration
```bash
# Operation Parameters
MAX_CONCURRENT_PIPELINES=5
FAILURE_THRESHOLD_PERCENT=10
AUTO_ROLLBACK_ENABLED=true

# Workflow Integration
AZURE_DEVOPS_TOKEN="your-ado-token"  # Optional
AZURE_DEVOPS_ORG="your-organization"  # Optional
```

### Advanced Configuration
```bash
# Pipeline Management
PIPELINE_RETRY_ATTEMPTS=3
PIPELINE_TIMEOUT_MINUTES=60
APPROVAL_REQUIRED_FOR_PROD=true

# Rollback Settings
ROLLBACK_ON_FAILURE_RATE=15  # Percentage
ROLLBACK_TIMEOUT_MINUTES=10
```

### Usage Examples
```bash
# Monitor mode (safe to start with)
python cicd_orchestration_agent.py --mode monitor

# Autonomous mode with continuous operation
python cicd_orchestration_agent.py --mode autonomous --continuous --interval 900

# Single run in autonomous mode
python cicd_orchestration_agent.py --mode autonomous
```

## Infrastructure Management Agent Configuration

### Basic Configuration
```bash
# Cost Management
MAX_COST_INCREASE_PERCENT=20
COST_ALERT_THRESHOLD_USD=1000

# Auto-scaling
AUTO_SCALING_ENABLED=true
MIN_INSTANCES=1
MAX_INSTANCES=10

# Compliance
COMPLIANCE_ENFORCEMENT=strict  # Options: strict, moderate, relaxed
```

### Advanced Configuration
```bash
# Resource Management
UNDERUTILIZED_CPU_THRESHOLD=20  # Percentage
OVERUTILIZED_CPU_THRESHOLD=85   # Percentage
MEMORY_THRESHOLD=80             # Percentage

# Cleanup Policies
AUTO_CLEANUP_ENABLED=true
CLEANUP_UNUSED_RESOURCES_DAYS=7
RETAIN_BACKUPS_DAYS=30

# Monitoring Integration
AZURE_MONITOR_WORKSPACE_ID="your-log-analytics-workspace-id"
PROMETHEUS_URL="http://your-prometheus:9090"  # Optional
```

### Usage Examples
```bash
# Monitor mode for infrastructure assessment
python infrastructure_management_agent.py --mode monitor

# Autonomous mode running every 6 hours
python infrastructure_management_agent.py --mode autonomous --continuous --interval 21600

# One-time infrastructure optimization
python infrastructure_management_agent.py --mode autonomous
```

## Incident Response Agent Configuration

### Basic Configuration
```bash
# Detection Settings
AZURE_MONITOR_WORKSPACE_ID="your-workspace-id"
PROMETHEUS_URL="http://your-prometheus:9090"

# Response Settings
AUTO_RESOLUTION_ENABLED=true
ESCALATION_TIMEOUT_MINUTES=15

# Severity Thresholds (JSON format)
SEVERITY_THRESHOLDS='{"critical": 1, "high": 3, "medium": 5, "low": 10}'
```

### Advanced Configuration
```bash
# Response Capabilities
ENABLE_AUTO_RESTART=true
ENABLE_AUTO_SCALING=true
ENABLE_ROLLBACK=true
ENABLE_TRAFFIC_REROUTING=false  # Use with caution

# Incident Management
MAX_AUTO_ATTEMPTS=3
INCIDENT_CORRELATION_WINDOW_MINUTES=5

# Integration
PAGERDUTY_INTEGRATION_KEY="your-pagerduty-key"  # Optional
SERVICENOW_INSTANCE="your-instance.service-now.com"  # Optional
```

### Usage Examples
```bash
# Continuous monitoring mode (recommended)
python incident_response_agent.py --mode monitor --continuous --interval 300

# Autonomous incident response
python incident_response_agent.py --mode autonomous --continuous --interval 300

# Analyze specific incident
python incident_response_agent.py --incident-id INC-12345 --action analyze
```

## Enhanced Code Quality Agent Configuration

### Basic Configuration
```bash
# GitHub Integration (inherits from global config)
PR_NUMBER=${GITHUB_PR_NUMBER}  # Auto-set in GitHub Actions

# Review Settings
REVIEW_COMPLEXITY_THRESHOLD=high
SECURITY_SCAN_ENABLED=true
COMPLIANCE_CHECK_ENABLED=true
```

### Advanced Configuration
```bash
# AI Review Parameters
MIN_CONFIDENCE_SCORE=0.7
MAX_SUGGESTIONS_PER_PR=20
INCLUDE_STYLE_SUGGESTIONS=true

# Security Settings
BLOCK_CRITICAL_VULNERABILITIES=true
SECURITY_SCAN_TIMEOUT=600  # seconds

# Exception Management
EXCEPTION_LIST_FILE="pr_review_exception_list.txt"
```

### Usage (typically in GitHub Actions)
```yaml
- name: Run Enhanced Code Quality Agent
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    AI_API_KEY: ${{ secrets.AI_API_KEY }}
  run: python ai-agents/codequality_agent/ai_code_review.py
```

## Cost Optimization Agent Configuration

### Basic Configuration
```bash
# Azure Cost Management (inherits Azure config from global)
COST_ANALYSIS_PERIOD_DAYS=30
SAVINGS_THRESHOLD_PERCENT=10

# Optimization Settings
AUTO_OPTIMIZATION_ENABLED=true
CLEANUP_UNUSED_RESOURCES=true
```

### Advanced Configuration
```bash
# Resource Policies
SHUTDOWN_DEV_ENVIRONMENTS=true
SHUTDOWN_SCHEDULE="18:00-08:00"  # Format: HH:MM-HH:MM
WEEKEND_SHUTDOWN_ENABLED=true

# Reserved Instance Management
ANALYZE_RESERVED_INSTANCES=true
RECOMMEND_RESERVED_PURCHASES=true

# Reporting
COST_REPORT_FREQUENCY=weekly  # daily, weekly, monthly
COST_ANOMALY_THRESHOLD=25     # Percentage increase
```

## Agent Orchestrator Configuration

### Basic Configuration
```bash
# Orchestrator Service
ORCHESTRATOR_PORT=8000
AGENT_DISCOVERY_INTERVAL=30  # seconds
HEALTH_CHECK_INTERVAL=60     # seconds

# Dashboard
DASHBOARD_ENABLED=true
DASHBOARD_PORT=3000
DASHBOARD_AUTH_ENABLED=true
```

### Advanced Configuration
```bash
# Database (for persistent state)
DATABASE_URL="postgresql://user:pass@localhost/orchestrator"
REDIS_URL="redis://localhost:6379"

# High Availability
HA_ENABLED=false
CLUSTER_NODE_ID="node-1"
LEADER_ELECTION_ENABLED=false

# Human Intervention Limits
MAX_AUTONOMOUS_ACTIONS_PER_HOUR=50
ESCALATION_THRESHOLD_CRITICAL=1
ESCALATION_THRESHOLD_HIGH=3
```

## Security Configuration

### Credential Management
```bash
# Use Azure Key Vault for production (recommended)
AZURE_KEYVAULT_URL="https://your-keyvault.vault.azure.net/"

# Or use environment variables for development
# Ensure these are set securely in production
```

### Network Security
```bash
# API Rate Limiting
RATE_LIMIT_REQUESTS_PER_MINUTE=60
API_TIMEOUT_SECONDS=30

# Encryption
ENCRYPT_COMMUNICATIONS=true
TLS_VERIFY=true
```

## Monitoring and Logging Configuration

### Logging Configuration
```bash
# Log Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL=INFO
LOG_FORMAT=json  # json or text
LOG_RETENTION_DAYS=30

# Log Destinations
LOG_TO_FILE=true
LOG_TO_CONSOLE=true
LOG_TO_AZURE_MONITOR=false  # Optional
```

### Metrics Configuration
```bash
# Metrics Collection
METRICS_ENABLED=true
METRICS_PORT=9090
METRICS_ENDPOINT="/metrics"

# Performance Monitoring
PERFORMANCE_TRACKING=true
RESPONSE_TIME_THRESHOLD_MS=5000
```

## Configuration Templates

### Development Environment
```bash
# Copy this for development setup
export AI_API_KEY="your-dev-api-key"
export GITHUB_TOKEN="your-dev-github-token"
export SLACK_WEBHOOK_URL="your-dev-slack-webhook"

# Start all agents in monitor mode
export AUTONOMOUS_MODE="monitor"
export AUTO_RESOLUTION_ENABLED="false"
export AUTO_SCALING_ENABLED="false"
```

### Production Environment
```bash
# Production configuration (use secure secret management)
export AI_API_KEY="${AZURE_KEYVAULT_AI_API_KEY}"
export GITHUB_TOKEN="${AZURE_KEYVAULT_GITHUB_TOKEN}"

# Enable autonomous operations
export AUTONOMOUS_MODE="autonomous"
export AUTO_RESOLUTION_ENABLED="true"
export AUTO_SCALING_ENABLED="true"

# Production safety settings
export MAX_AUTONOMOUS_ACTIONS_PER_HOUR="100"
export ESCALATION_THRESHOLD_CRITICAL="1"
```

## Troubleshooting Configuration

### Common Issues

1. **Agent fails to start**
   - Check all required environment variables are set
   - Verify API keys and tokens are valid
   - Check network connectivity to external services

2. **Agents escalate too frequently**
   - Review confidence thresholds
   - Adjust severity thresholds
   - Check historical data availability

3. **Poor agent performance**
   - Increase logging level to DEBUG
   - Review agent health metrics
   - Check resource constraints

### Validation Commands

```bash
# Test agent configuration
python agent_name.py --validate-config

# Test connectivity
python agent_name.py --test-connectivity

# Check agent health
curl http://localhost:8000/health
```

## Best Practices

1. **Start with Monitor Mode**: Always begin with monitor mode to build confidence
2. **Gradual Rollout**: Enable autonomous features incrementally
3. **Monitor Closely**: Watch agent performance and adjust thresholds
4. **Secure Credentials**: Use proper secret management in production
5. **Regular Reviews**: Periodically review agent configurations and performance
6. **Backup Configurations**: Version control your configuration files
7. **Test Changes**: Always test configuration changes in non-production first

## Configuration Files

Store configurations in version-controlled files:

```bash
# Create environment-specific config files
config/
├── development.env
├── staging.env
└── production.env
```

Example configuration file:
```bash
# config/production.env
AI_API_KEY=${VAULT_AI_API_KEY}
AUTONOMOUS_MODE=autonomous
AUTO_RESOLUTION_ENABLED=true
MAX_CONCURRENT_PIPELINES=10
ESCALATION_THRESHOLD_CRITICAL=1
```

Load with:
```bash
source config/production.env
```

This configuration guide provides a comprehensive foundation for setting up and managing autonomous DevOps agents in your human-on-the-sidelines implementation.