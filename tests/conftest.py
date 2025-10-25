"""Pytest configuration and fixtures."""
import tempfile
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_config() -> dict[str, Any]:
    """Sample configuration for testing."""
    return {
        "project": {"name": "test_simulation", "description": "Test simulation"},
        "scales": ["macro", "meso"],
        "macro": {
            "engine": "openfoam",
            "parameters": {"particle_diameter": 100e-9, "simulation_time": 10},
        },
        "meso": {
            "engine": "gromacs",
            "parameters": {"temperature": 310, "simulation_time": 100e-9},
        },
    }


@pytest.fixture
def sample_simulation_config(temp_dir):
    """Create a sample SimulationConfig object."""
    from nanosim.core.simulation import SimulationConfig

    return SimulationConfig(
        name="test_sim",
        input_dir=temp_dir / "input",
        output_dir=temp_dir / "output",
        parameters={"test_param": 1.0},
    )
