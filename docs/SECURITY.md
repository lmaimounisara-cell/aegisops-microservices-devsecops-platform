# Security Practices — AegisOps

## Purpose

This document describes the security practices used in the AegisOps Catalog API project and identifies controls that remain future work.

## Implemented controls

### Container security
- The Catalog API Dockerfile runs the application as a non-root user.
- Python dependencies are explicitly version-pinned.
- The image is built using a slim Python base image.

### Automated validation
- GitHub Actions runs the Catalog API test suite.
- A separate CI job builds the Docker image after the tests pass.
- The repository includes a security workflow for automated repository checks.

## Security checks and limitations

Automated checks do not guarantee that an application is free of vulnerabilities.

The project should record the results of dependency and image scans, review relevant findings, and document remediation decisions. A passing workflow must not be described as proof that no vulnerabilities exist.

## Planned improvements

- Add a dependency vulnerability scan to the Catalog API CI workflow.
- Define failure policies for high- and critical-severity findings.
- Pin third-party GitHub Actions to reviewed commit SHAs.
- Add automated secret scanning and prevent accidental credential commits.
- Document image provenance and safe registry publishing.
- Review the application’s authentication, authorization, and input validation requirements before exposing it publicly.

## Secrets and configuration

- Never commit passwords, access tokens, private keys, or kubeconfig files.
- Use GitHub Actions secrets for credentials required by workflows.
- Avoid placing secrets in Docker images, logs, or documentation.
- Rotate any credential that is accidentally exposed.

## Reporting issues

Report security issues privately to the repository owner rather than publishing exploit details or secrets in a public issue.

## Maintenance

Update this document as controls are implemented and verified. Keep implemented controls separate from planned improvements.
