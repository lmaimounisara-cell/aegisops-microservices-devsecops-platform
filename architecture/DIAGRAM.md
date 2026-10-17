# AegisOps Architecture

This diagram represents the components currently implemented and verified in this repository. Cloud deployment components are not included because their operation has not yet been verified.

```mermaid
flowchart TD
    Dev["Developer"] --> Repo["GitHub Repository"]
    Repo --> CI["GitHub Actions CI"]
    CI --> Tests["Run Pytest"]
    Tests -->|Pass| Build["Build Docker Image"]
    Tests -->|Fail| Stop["Fail Workflow"]
    Build --> CIResult["Successful CI Result"]
    Build --> Local["Run Container Locally"]
    Local --> API["FastAPI Catalog API"]
    API --> Health["GET /health"]
    API --> Products["GET /api/v1/products"]
    API --> Product["GET /api/v1/products/{id}"]

    classDef verified fill:#dcfce7,stroke:#15803d,color:#14532d
    class Repo,CI,Tests,Build,API,Health,Products,Product verified
```

## Verified components

- **GitHub:** Source code and workflow version control.
- **GitHub Actions:** Automated API tests and Docker image build.
- **FastAPI:** Catalog API and health endpoint.
- **Pytest:** Automated API tests.
- **Docker:** Containerized application.

## Not yet verified

Terraform-managed Azure infrastructure, AKS deployment, Argo CD reconciliation, and production monitoring remain outside the verified current implementation.

These components should only be added to the implemented architecture after their configuration and operation have been confirmed.
