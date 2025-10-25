# Contributing to NanoSim

Thank you for your interest in contributing to NanoSim! This guide will help you get started.

For the complete contributing guidelines, please see [CONTRIBUTING.md](https://github.com/xiaojunyang0805/NanoSim/blob/main/CONTRIBUTING.md) in the repository root.

## Quick Start

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Run tests
6. Submit a pull request

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/NanoSim.git
cd NanoSim
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_core.py
```

## Code Style

We use:

- **black** for code formatting
- **ruff** for linting
- **mypy** for type checking

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/
```

## Commit Messages

Follow the Conventional Commits specification:

```
feat: add new feature
fix: bug fix
docs: documentation changes
test: add tests
refactor: code refactoring
```

## Pull Request Process

1. Update documentation for any new features
2. Add tests for new functionality
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow

## Questions?

- Open a GitHub issue
- Email: support@seenano.nl
