"""Base classes for simulation components."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class SimulationConfig:
    """Base configuration for simulations.

    Attributes:
        name: Simulation name
        input_dir: Directory containing input files
        output_dir: Directory for output files
        parameters: Dictionary of simulation parameters
    """

    name: str
    input_dir: Path
    output_dir: Path
    parameters: dict[str, Any]

    def __post_init__(self) -> None:
        """Validate and convert paths."""
        self.input_dir = Path(self.input_dir)
        self.output_dir = Path(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class SimulationResult:
    """Result from a simulation.

    Attributes:
        success: Whether simulation completed successfully
        output_files: List of generated output files
        metadata: Additional information about the simulation
        error_message: Error message if simulation failed
    """

    success: bool
    output_files: list[Path]
    metadata: dict[str, Any]
    error_message: str | None = None


class SimulationEngine(ABC):
    """Abstract base class for simulation engines.

    All simulation engine wrappers (OpenFOAM, GROMACS, AutoDock) should inherit
    from this class and implement the required methods.
    """

    def __init__(self, config: SimulationConfig) -> None:
        """Initialize simulation engine.

        Args:
            config: Simulation configuration
        """
        self.config = config
        self.validate_config()

    @abstractmethod
    def validate_config(self) -> None:
        """Validate configuration parameters.

        Raises:
            ValueError: If configuration is invalid
        """
        pass

    @abstractmethod
    def setup(self) -> None:
        """Prepare simulation environment.

        This may include creating directories, generating input files,
        or initializing the simulation engine.
        """
        pass

    @abstractmethod
    def run(self) -> SimulationResult:
        """Execute the simulation.

        Returns:
            SimulationResult containing output files and metadata
        """
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Clean up temporary files and resources."""
        pass

    def execute(self) -> SimulationResult:
        """Execute complete simulation workflow.

        This is a convenience method that calls setup(), run(), and cleanup()
        in sequence.

        Returns:
            SimulationResult from the simulation
        """
        try:
            self.setup()
            result = self.run()
            return result
        finally:
            self.cleanup()
