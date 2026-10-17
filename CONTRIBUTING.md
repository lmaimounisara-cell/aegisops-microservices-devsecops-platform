# Contributing

## Development workflow

1. Create a focused branch for each change.
2. Explain the purpose and operational impact in the pull request.
3. Validate configuration and run relevant tests before merging.
4. Review security implications, including permissions and secret handling.
5. Update documentation when behavior, architecture, or operations change.

## Security requirements

- Never submit credentials, tokens, private keys, or state files.
- Use least-privilege permissions.
- Prefer pinned, reviewed dependencies and actions.
- Record important architectural decisions.
- Do not claim a feature is operational without verification.

## Infrastructure changes

Review Terraform plans before applying them. Never apply changes to shared or
cloud infrastructure without explicitly checking the target environment.
