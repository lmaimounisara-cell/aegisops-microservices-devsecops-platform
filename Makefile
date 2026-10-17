.PHONY: help validate

help:
	@echo "Available targets:"
	@echo "  help      Show available targets"
	@echo "  validate  Check repository files"

validate:
	@test -f README.md
	@test -f .gitignore
	@test -f .github/workflows/security.yml
	@test -f architecture/ARCHITECTURE.md
	@test -f architecture/DIAGRAM.md
	@echo "Repository file checks passed."
