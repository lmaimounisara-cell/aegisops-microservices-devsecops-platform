# AegisOps Microservices DevSecOps Platform

A personal cloud-native engineering project focused on securing and automating
the delivery of microservices using Azure Kubernetes Service, GitHub Actions,
Docker, GitOps, and observability.

## Project goals

- Automate application build and delivery workflows.
- Apply security scanning to application images and dependencies.
- Manage Kubernetes deployments declaratively with GitOps.
- Provision and operate cloud infrastructure using infrastructure as code.
- Improve workload reliability through health checks, autoscaling, and monitoring.
- Document security decisions, operational procedures, and recovery workflows.

## Architecture

The intended delivery flow is:

1. A change is pushed to GitHub.
2. CI validates the change and builds the relevant container image.
3. Security tools scan the image and dependencies.
4. The approved image is published to a container registry.
5. Argo CD reconciles the desired Kubernetes configuration.
6. Kubernetes runs the workloads and exposes application endpoints.
7. Prometheus and Grafana provide metrics and operational visibility.

The final implementation details will be documented as each component is
verified. This flow describes the target architecture, not a claim that every
step is currently active.

## Technology areas

| Area | Technology |
|---|---|
| Cloud | Microsoft Azure |
| Container orchestration | Azure Kubernetes Service (AKS) |
| Infrastructure as code | Terraform |
| CI/CD | GitHub Actions |
| Containers | Docker |
| GitOps | Argo CD |
| Security scanning | Trivy |
| Observability | Prometheus and Grafana |

## Repository structure

- `architecture/` — diagrams and architecture decisions.
- `argocd/` — GitOps application definitions.
- `docs/` — setup, implementation, and operations documentation.
- `helm/` — Helm charts and values.
- `kubernetes/` — Kubernetes workload configuration.
- `observability/` — monitoring and logging configuration.
- `scripts/` — automation scripts.
- `security/` — security policies and scanning configuration.
- `terraform/azure/` — Azure infrastructure code.

## Implementation status

This repository is being rebuilt as a clean, personal engineering portfolio.
Components will be marked implemented only after their configuration and
operation have been verified.

## Security

- Never commit credentials, access tokens, private keys, or kubeconfig files.
- Keep environment-specific values outside source control when appropriate.
- Review infrastructure plans before applying changes.
- Document security findings and their remediation.

## License and third-party components

Third-party software and dependencies remain subject to their respective
licenses. Attribution and license requirements will be documented for any
upstream components retained in this project.

## Author

Personal engineering portfolio project by Sara.
