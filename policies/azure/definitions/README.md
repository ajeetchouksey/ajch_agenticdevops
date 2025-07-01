# Azure Policy Definitions

This folder contains custom and built-in Azure Policy definitions for your organization.

## Structure
- Each policy is defined as a JSON file (e.g., `allowed-locations-management.json`).
- Policy rules are extracted into a separate `.rules.json` file for Azure CLI compatibility.

## Deployment Pipeline
- Policy definitions are created or updated on any branch push.
- Policy assignments are only made from the `main` branch.
- `.rules.json` files are skipped in the deployment loop.

## How to Add or Update a Policy
1. Add or update the main policy JSON file in this folder.
2. Add or update the corresponding `.rules.json` file with the policy rule.
3. Commit and push your changes.
4. The pipeline will deploy the policy definition. Assignment will only occur from `main`.

## Example
- `allowed-locations-management.json`: Metadata and parameters for the policy.
- `allowed-locations-management.rules.json`: The policy rule logic.

## Notes
- Ensure your service principal has the correct permissions at the management group level.
- Only valid policy definition files (not `.rules.json`) are processed for deployment.
