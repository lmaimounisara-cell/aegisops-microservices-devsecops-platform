# Testing and Validation — AegisOps

## Purpose

This guide explains how to reproduce the Catalog API tests and container build locally.

## Prerequisites

- Git
- Python 3.12 or a compatible Python version
- Docker Engine or Docker Desktop

## 1. Get the source code

```bash
git clone https://github.com/lmaimounisara-cell/aegisops-microservices-devsecops-platform.git
cd aegisops-microservices-devsecops-platform
```

## 2. Run the API tests

Change to the service directory:

```bash
cd services/catalog
```

Install the declared dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the test suite:

```bash
python -m pytest tests -v
```

A successful run should report that all tests passed. The exact result depends on the current source and environment.

## 3. Build the Docker image

Return to the repository root:

```bash
cd ../..
```

Build the image:

```bash
docker build -t aegisops-catalog:1.0.0 ./services/catalog
```

## 4. Run the container

```bash
docker run --rm -p 8000:8000 aegisops-catalog:1.0.0
```

Keep this terminal open while testing the service.

## 5. Verify the health endpoint

In a second terminal:

```bash
curl -i http://localhost:8000/health
```

The expected response is HTTP 200 with a JSON status indicating that the service is healthy.

## 6. Verify product endpoints

List products:

```bash
curl -i http://localhost:8000/api/v1/products
```

Retrieve an existing product:

```bash
curl -i http://localhost:8000/api/v1/products/1
```

Try a product ID that does not exist:

```bash
curl -i http://localhost:8000/api/v1/products/999
```

The last request should return HTTP 404.

## 7. Continuous integration

The GitHub Actions workflow in `.github/workflows/catalog-ci.yml` runs the API tests and builds the Docker image. Review the Actions tab for the result of a particular commit.

## Troubleshooting

- If port 8000 is already occupied, stop the conflicting process or use another host port.
- If Docker cannot connect to its daemon, start Docker Desktop or the relevant Docker service.
- If a test fails, read the assertion and application output before changing dependencies.
- Do not include credentials or private configuration in logs or screenshots.

## Scope

This guide covers the Catalog API tests and container workflow. It does not claim that cloud deployment or production monitoring has been configured.
