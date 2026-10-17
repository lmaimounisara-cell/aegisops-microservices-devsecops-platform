# Project Status — AegisOps

## Overview

AegisOps is a personal DevSecOps portfolio project focused on automated testing, containerization, and security checks for a cloud-native application.

This document distinguishes verified implementation from future plans.

## Implemented and verified

### Catalog API
- FastAPI application with health and product endpoints.
- Unit tests covering successful requests and a missing product.
- Pinned Python dependencies.
- Dockerfile configured to run the application as a non-root user.

### Continuous integration
- GitHub Actions workflow runs the Catalog API tests.
- A separate job builds the Docker image after the tests pass.
- The workflow has completed successfully on GitHub Actions.

### Container validation
- The Catalog API Docker image was built locally.
- Health and product endpoints were tested against the running container.
- Trivy is used in the original project pipeline for image vulnerability scanning.

## Planned or not yet verified in this repository

The following are goals, not claims of a completed deployment:
- Terraform-managed Azure infrastructure.
- Azure Kubernetes Service deployment.
- Argo CD GitOps reconciliation.
- Production-ready monitoring and logging.
- Automated deployment and recovery procedures.

These components will be marked implemented only when their configuration and operation have been verified in this repository.

## Verification commands

From the `services/catalog` directory:

```bash
python -m pytest tests -v
```

Build the image from the repository root:

```bash
docker build -t aegisops-catalog:1.0.0 ./services/catalog
```

Run the container:

```bash
docker run --rm -p 8000:8000 aegisops-catalog:1.0.0
```

In another terminal, check the health endpoint:

```bash
curl http://localhost:8000/health
```

## Evidence

The repository's GitHub Actions history provides evidence of automated tests and Docker image builds. Test and deployment claims should be supported by reproducible results.

## Maintenance

Update this document when implementation status changes. Do not publish credentials, tokens, private keys, or sensitive environment configuration.
