# Contributing to NanoSim

Thank you for your interest in contributing to NanoSim! We welcome contributions from the community.

## Getting Started

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/NanoSim.git
   cd NanoSim
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements-dev.txt
   pre-commit install
   ```

4. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Reporting Bugs

- Use the GitHub issue tracker
- Include system information (OS, Python version, Docker version)
- Provide a minimal reproducible example
- Attach relevant logs or error messages

### Suggesting Features

- Open an issue with the `enhancement` label
- Describe the use case and benefits
- Discuss implementation approach if you have ideas

### Submitting Code

1. **Write Tests**
   - Add tests for new features
   - Ensure existing tests pass
   - Aim for >80% code coverage

2. **Follow Code Style**
   - Use `black` for formatting
   - Use `ruff` for linting
   - Add type hints
   - Write docstrings (Google style)

3. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add feature description"
   ```

   **Commit Message Format:**
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `test:` Test additions or changes
   - `refactor:` Code refactoring
   - `chore:` Maintenance tasks

4. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub

### Code Review Process

- All PRs require at least one approval
- CI checks must pass (tests, linting, type checks)
- Maintainers may request changes
- Be responsive to feedback

## Development Guidelines

### Python Code Style

```python
"""Module docstring explaining purpose."""

from typing import Dict, List, Optional


def calculate_binding_affinity(
    receptor: str,
    ligand: str,
    exhaustiveness: int = 8
) -> Dict[str, float]:
    """Calculate binding affinity using AutoDock Vina.

    Args:
        receptor: Path to receptor PDB file
        ligand: Path to ligand PDB file
        exhaustiveness: Search exhaustiveness (default: 8)

    Returns:
        Dictionary containing binding affinity and best pose

    Raises:
        FileNotFoundError: If receptor or ligand file not found
    """
    # Implementation
    pass
```

### Testing

```python
"""Tests for binding affinity calculations."""

import pytest
from nanosim.engines.autodock import calculate_binding_affinity


def test_binding_affinity_calculation(tmp_path):
    """Test binding affinity calculation with sample data."""
    # Test implementation
    pass
```

### Documentation

- Update relevant documentation when adding features
- Add docstrings to all public functions/classes
- Update README.md if needed
- Add examples for new features

## Community

### Communication

- **GitHub Discussions**: General questions and ideas
- **GitHub Issues**: Bug reports and feature requests
- **Email**: support@seenano.nl for sensitive topics

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Maintain professional communication

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

## Questions?

If you have questions about contributing, please:
1. Check existing documentation
2. Search closed issues
3. Open a new discussion on GitHub
4. Contact us at support@seenano.nl

Thank you for contributing to NanoSim!
