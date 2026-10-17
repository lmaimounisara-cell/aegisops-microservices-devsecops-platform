# AegisOps — Microservices DevSecOps Platform

A personal DevSecOps engineering project demonstrating automated testing, containerization, and security checks for a cloud-native application.

**Repository:** [AegisOps on GitHub](https://github.com/lmaimounisara-cell/aegisops-microservices-devsecops-platform)

## Project overview

AegisOps currently includes a FastAPI Catalog API, automated tests, a Docker image build, and GitHub Actions workflows. The project is being developed incrementally, with implementation status documented transparently.

## Verified capabilities

- **API:** FastAPI endpoints for health checks and product queries.
- **Testing:** Pytest tests for successful requests and missing products.
- **Containerization:** Dockerfile using a slim Python image and a non-root application user.
- **Continuous integration:** GitHub Actions runs tests and builds the Docker image.
- **Repository security:** A workflow is configured for repository security checks.
- **Documentation:** Architecture and project status documentation are maintained in the repository.

## Architecture

The current verified workflow is:

1. Source code is committed to GitHub.
2. GitHub Actions installs dependencies and runs tests.
3. The pipeline builds the Catalog API Docker image after tests pass.
4. The workflow reports the results in GitHub Actions.

Terraform, Azure Kubernetes Service, Argo CD, and production observability are longer-term goals and should not be considered deployed until their implementation is verified.

## Technology stack

| Area | Technology |
|---|---|
| API | Python, FastAPI |
| Testing | Pytest |
| Containers | Docker |
| CI/CD | GitHub Actions |
| Security tooling | Repository security checks; Trivy is used in the original microservices project pipeline |
| Planned infrastructure | Terraform, Azure Kubernetes Service, Argo CD |

## Repository structure

- `services/catalog/` — Catalog API source, tests, dependencies, and Dockerfile.
- `.github/workflows/` — CI and repository security workflows.
- `architecture/` — Architecture notes and diagram source.
- `docs/PROJECT_STATUS.md` — Implemented capabilities and outstanding work.
- `docs/SECURITY.md` — Security practices and planned improvements.
- `CONTRIBUTING.md` — Contribution guidance.
- `Makefile` — Common development commands.

## Run locally

Requirements: Python 3.12 or compatible, and Docker if you want to run the container.

Run the tests from the Catalog API directory:

```bash
cd services/catalog
python -m pytest tests -v
```

Build the Docker image from the repository root:

```bash
docker build -t aegisops-catalog:1.0.0 ./services/catalog
```

Run the container:

```bash
docker run --rm -p 8000:8000 aegisops-catalog:1.0.0
```

In another terminal, test the health endpoint:

```bash
curl http://localhost:8000/health
```

## Documentation

- [Project status](docs/PROJECT_STATUS.md)
- [Security practices](docs/SECURITY.md)
- [Architecture overview](architecture/ARCHITECTURE.md)
- [Architecture diagram source](architecture/DIAGRAM.md)

## Project status

This is an evolving portfolio project. The repository documents implemented features separately from planned work. Successful tests and workflow runs provide evidence of the capabilities currently available; they do not imply that the planned cloud infrastructure has been deployed.

## Security

Never commit credentials, access tokens, private keys, or kubeconfig files. Review security findings before publishing images or deploying workloads.

## License and third-party components

Review third-party dependency and upstream license obligations before redistribution. Any retained upstream code should be attributed appropriately.

## Author

**Sara** — personal engineering portfolio project.
