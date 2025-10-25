"""Tests for core functionality."""
from pathlib import Path

from nanosim.core.simulation import SimulationConfig, SimulationResult


def test_simulation_config_creation(temp_dir):
    """Test SimulationConfig initialization."""
    config = SimulationConfig(
        name="test",
        input_dir=temp_dir / "input",
        output_dir=temp_dir / "output",
        parameters={"param1": 1.0},
    )

    assert config.name == "test"
    assert config.parameters["param1"] == 1.0
    assert config.output_dir.exists()  # Should be created automatically


def test_simulation_config_path_conversion(temp_dir):
    """Test that paths are converted to Path objects."""
    config = SimulationConfig(
        name="test",
        input_dir=str(temp_dir / "input"),  # Pass as string
        output_dir=str(temp_dir / "output"),
        parameters={},
    )

    assert isinstance(config.input_dir, Path)
    assert isinstance(config.output_dir, Path)


def test_simulation_result_success():
    """Test SimulationResult for successful simulation."""
    result = SimulationResult(
        success=True,
        output_files=[Path("output1.txt"), Path("output2.txt")],
        metadata={"runtime": 10.5},
    )

    assert result.success
    assert len(result.output_files) == 2
    assert result.error_message is None


def test_simulation_result_failure():
    """Test SimulationResult for failed simulation."""
    result = SimulationResult(
        success=False, output_files=[], metadata={}, error_message="Simulation failed"
    )

    assert not result.success
    assert result.error_message == "Simulation failed"
