# Azure Landing Zone Terraform Playground

This repository is designed as a playground for learning and deploying Azure Landing Zones using Terraform and agentic DevOps practices. It follows industry best practices for modularity, compliance, and environment separation.

## Repository Structure

```
core-modules/
  network/         # Reusable network module (vnet, subnets, etc.)
  identity/        # Reusable identity module (Azure AD, managed identities, etc.)
  management/      # Reusable management module (policies, monitoring, etc.)

landingzones/
  management/      # Management landing zone, uses core modules
  connectivity/    # Connectivity landing zone, uses core modules
  avd/             # Azure Virtual Desktop landing zone, uses core modules
  application/     # Application (spoke) landing zone, uses core modules
```


## Design Considerations

### Architectural Design Principles

**Single Responsibility Principle (SRP):**
Each module and landing zone has a focused responsibility, making code easier to maintain, test, and reuse.

**Separation of Concerns:**
Core modules encapsulate reusable logic, while landing zones manage environment-specific configuration and orchestration. This reduces coupling and increases clarity.

**Modularity:**
The structure enables you to add, update, or remove modules and landing zones independently, supporting rapid iteration and experimentation.

**Scalability:**
You can scale your environment by simply adding new landing zones or modules without impacting existing deployments.

**Reusability:**
Core modules are designed to be used across multiple landing zones, reducing duplication and enforcing standards.

**Compliance & Security:**
The structure supports policy-as-code, RBAC, and secure state management, making it easier to meet organizational and regulatory requirements.

**Collaboration:**
Clear boundaries between modules and landing zones make it easier for teams to collaborate, review, and contribute.

**Purpose in Terms of Infrastructure as Code (IaC):**
- Promote best practices for IaC by enforcing modular, reusable, and testable code.
- Enable safe experimentation and learning in a playground environment.
- Support real-world landing zone patterns for Azure, making it easier to transition to production-ready architectures.

## Best Practices
- **Modular Design:** All core infrastructure logic is in `core-modules` for reuse and compliance.
- **Separation of Concerns:** Each landing zone is isolated and can have its own state file and backend configuration.
- **Scalability:** Add new landing zones or applications by creating new folders under `landingzones/`.
- **Compliance:** Structure supports policy-as-code, RBAC, and secure state management.

## Getting Started
1. Clone the repository.
2. Navigate to a landing zone folder (e.g., `landingzones/management`).
3. Configure your backend (e.g., `backend.tf`) and variables as needed.
4. Run Terraform commands as usual (`init`, `plan`, `apply`).

## Example Usage
Each landing zone's `main.tf` can use modules like this:

```hcl
module "network" {
  source = "../../core-modules/network"
  # ...module variables...
}
```

---