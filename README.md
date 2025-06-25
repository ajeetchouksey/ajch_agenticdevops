

# Azure Landing Zone Terraform Playground

This repository serves as a dedicated learning environment for exploring and experimenting with Azure Landing Zone architectures using Terraform, informed by my professional experience. It is intended solely for educational and demonstration purposes, and is not designed for direct use in production environments.

The structure, patterns, and practices implemented here reflect industry best practices for modularity, compliance, automation, and reusability, as interpreted and applied through hands-on experience. Users are encouraged to adapt and extend these examples to suit their own organizational requirements.

> **Note:**
> For production or enterprise scenarios, it is strongly recommended to separate core modules and landing zone orchestration into distinct repositories. This approach enhances versioning, security, collaboration, and reusability. For learning and experimentation, a single monorepo (as provided here) offers simplicity and flexibility for rapid iteration.


## Repository Structure

The repository is organized for clarity and modularity, making it easy to navigate and extend:

```
core-modules/
  network/      # Networking resources (VNet, subnets, NSG, etc.)
  identity/     # Identity resources (Azure AD, managed identities, etc.)
  management/   # Management/governance resources (policies, monitoring, etc.)

landingzones/
  management/      # Management landing zone (uses core modules)
  connectivity/    # Connectivity landing zone (uses core modules)
  avd/             # Azure Virtual Desktop landing zone (uses core modules)
  application/     # Application (spoke) landing zone (uses core modules)
```

---

### Production-Ready Recommendation

For production or enterprise environments, it is best practice to split core modules and landing zone orchestration into separate repositories. This approach improves versioning, security, collaboration, and reusability. A typical production structure might look like:

**Core Module Repositories:**
- `terraform-modules-network` (networking)
- `terraform-modules-identity` (identity)
- `terraform-modules-management` (management/governance)
- (Add more as needed: e.g., storage, keyvault)

**Landing Zone Repositories:**
- `landingzone-management`
- `landingzone-connectivity`
- `landingzone-avd`
- `landingzone-application`
- (Add more as needed for each environment or scenario)

**Example Directory Layout:**
```
github.com/your-org/
  terraform-modules-network/
  terraform-modules-identity/
  terraform-modules-management/
  landingzone-management/
  landingzone-connectivity/
  landingzone-application/
```

**Module Reference Example (in a landing zone repo):**
```hcl
module "network" {
  source  = "git::https://github.com/your-org/terraform-modules-network.git?ref=v1.0.0"
  # ...module variables...
}
```

This separation enables teams to work independently, reuse modules across projects, and maintain a secure, scalable, and compliant IaC environment.

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

## Core Modules and Resource Placement

This section explains what resources are typically included in each core module and what should be managed outside of them. Use this as a reference when designing or extending your landing zones.

### core-modules/network
- Virtual networks (VNet)
- Subnets
- Network security groups (NSG)
- Route tables
- Network peerings
- Private endpoints

### core-modules/identity
- Azure Active Directory (AAD) applications
- Service principals
- Managed identities (user-assigned/system-assigned)
- Role assignments (for identities)
- Key Vault access policies (if related to identity)

### core-modules/management
- Management groups
- Policy definitions and assignments
- Initiative definitions and assignments
- Resource locks
- Diagnostic settings (for logging/monitoring)
- Log Analytics workspaces
- Automation accounts (for governance tasks)
- Cost management resources

### What goes outside these modules?
- **Resource group creation:** Should be its own module (e.g., `core-modules/resource-group`) for reusability.
- **Application-specific resources:** (e.g., App Service, SQL DB, Storage Account for a specific app) should be defined in the relevant landing zone.
- **Landing zone orchestration:** The `main.tf` in each landing zone folder, which calls the core modules and wires them together.
- **Environment-specific configuration:** Variables, backend, outputs, etc., should be managed in the landing zone folders.

This separation keeps each module focused and reusable, while the landing zone folders orchestrate the deployment for a specific scenario or environment.

---
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