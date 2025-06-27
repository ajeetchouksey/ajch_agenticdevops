# Cost Optimization Agent for Azure

This guide will help you set up an AI-powered cost optimization agent for your Azure environment. The agent will analyze your Azure resource usage, identify cost-saving opportunities, and send actionable reports or alerts.

## Features
- Scheduled cost analysis (daily/weekly)
- Identifies underutilized or idle resources
- Recommends rightsizing, shutdown, or deletion
- Detects cost spikes or anomalies
- Sends notifications (email, Teams, etc.)
- (Optional) Automates cost-saving actions

---

## Step 1: Prerequisites
- Azure subscription with Cost Management API access
- Service Principal or user credentials with Reader permissions
- Python 3.8+ installed (or use GitHub Actions/Azure Functions)
- (Optional) SMTP/Teams/Slack credentials for notifications

---

## Step 2: Clone the Repository
```sh
git clone https://github.com/ajeetchouksey/ajch_agenticdevops.git
cd ajch_agenticdevops/ai-agents/costopt_agent
```

---

## Step 3: Set Up Python Environment
```sh
python -m venv .venv
.venv\Scripts\activate  # On Windows
# Or
source .venv/bin/activate  # On Linux/Mac
pip install -r requirements.txt
```

---

## Step 4: Configure Azure Credentials
- Create a file named `.env` in this folder with the following content:
```
AZURE_CLIENT_ID=your-client-id
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_SUBSCRIPTION_ID=your-subscription-id
NOTIFY_EMAIL=your@email.com
SMTP_SERVER=smtp.example.com
SMTP_USER=your@email.com
SMTP_PASS=your-smtp-password
```
- Never commit `.env` to source control.

---

## Step 5: Create the Cost Optimization Script
- Implement a Python script (e.g., `costopt_agent.py`) that:
  - Authenticates with Azure
  - Fetches cost and usage data
  - Analyzes for optimization opportunities
  - Sends a report/alert via email or Teams

---

## Step 6: Schedule the Agent
- **Option 1: GitHub Actions**
  - Create a workflow YAML file in `.github/workflows/` to run the script on a schedule (cron).
- **Option 2: Windows Task Scheduler/Linux Cron**
  - Schedule the script to run nightly/weekly.
- **Option 3: Azure Functions**
  - Deploy as a timer-triggered Azure Function (Python).

---

## Step 7: Review Reports & Take Action
- Check your email/Teams/Slack for cost optimization reports.
- Review recommendations and automate actions as needed.

---

## Step 8: (Optional) Automate Remediation
- Extend the script to:
  - Auto-shutdown or deallocate idle VMs
  - Remove unattached disks/public IPs
  - Resize overprovisioned resources
- Always review automation logic and test in non-production first.

---

## References
- [Azure Cost Management Docs](https://learn.microsoft.com/en-us/azure/cost-management-billing/)
- [Azure SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/)
- [dawidd6/action-send-mail](https://github.com/dawidd6/action-send-mail)

---

## Support
For questions or improvements, open an issue or contact the repository maintainer.
