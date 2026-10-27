# NOTE: whitespace in front of commands are Tabs!
# Install the package with development dependencies
# alternative to `pip install -r requirements`
install:
	pip install .[dev]

# Clean up build artifacts
clean:
	rm -rf build/ dist/ *.egg-info

# Format the code
format:
	ruff check flattool --fix
	ruff format flattool

# Run code quality checks (used by CI)
check:
	ruff check flattool
	ruff format --check flattool
