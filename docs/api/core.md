# Core API Reference

Core classes and interfaces for NanoSim.

## SimulationConfig

::: nanosim.core.simulation.SimulationConfig

Configuration object for simulations.

**Attributes:**

- `name` (str): Simulation name
- `input_dir` (Path): Input directory path
- `output_dir` (Path): Output directory path
- `parameters` (Dict[str, Any]): Engine-specific parameters

**Example:**

```python
from nanosim.core.simulation import SimulationConfig
from pathlib import Path

config = SimulationConfig(
    name="test_simulation",
    input_dir=Path("./input"),
    output_dir=Path("./output"),
    parameters={
        "temperature": 310,
        "simulation_time": 100e-9
    }
)
```

## SimulationResult

::: nanosim.core.simulation.SimulationResult

Result object from a simulation run.

**Attributes:**

- `success` (bool): Whether simulation succeeded
- `output_files` (List[Path]): List of output file paths
- `metadata` (Dict[str, Any]): Additional metadata
- `error_message` (Optional[str]): Error message if failed

**Example:**

```python
from nanosim.core.simulation import SimulationResult
from pathlib import Path

result = SimulationResult(
    success=True,
    output_files=[
        Path("output/trajectory.xtc"),
        Path("output/energy.edr")
    ],
    metadata={
        "runtime": 3600.5,
        "steps": 1000000
    }
)

if result.success:
    print(f"Simulation completed with {len(result.output_files)} output files")
else:
    print(f"Simulation failed: {result.error_message}")
```

## SimulationEngine

::: nanosim.core.simulation.SimulationEngine

Abstract base class for all simulation engines.

All engine implementations must inherit from this class and implement its abstract methods.

**Abstract Methods:**

- `validate_config()`: Validate engine configuration
- `setup()`: Set up simulation environment
- `run()`: Execute simulation and return result
- `cleanup()`: Clean up resources after execution

**Example Implementation:**

```python
from nanosim.core.simulation import SimulationEngine, SimulationConfig, SimulationResult

class MyEngine(SimulationEngine):
    def __init__(self, config: SimulationConfig):
        self.config = config
        self.logger = setup_logger(__name__)

    def validate_config(self) -> None:
        required = ["temperature", "pressure"]
        validate_parameters(self.config.parameters, required)

    def setup(self) -> None:
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger.info("Environment set up")

    def run(self) -> SimulationResult:
        try:
            # Run simulation logic here
            output_files = [self.config.output_dir / "result.dat"]
            return SimulationResult(
                success=True,
                output_files=output_files,
                metadata={"steps": 1000}
            )
        except Exception as e:
            return SimulationResult(
                success=False,
                output_files=[],
                metadata={},
                error_message=str(e)
            )

    def cleanup(self) -> None:
        self.logger.info("Cleanup completed")
```

## ScaleBridge

::: nanosim.core.bridge.ScaleBridge

Abstract base class for scale conversion bridges.

**Abstract Methods:**

- `convert(input_data)`: Convert data from one scale to another
- `validate(input_data, output_data)`: Validate conversion consistency

**Example Implementation:**

```python
from nanosim.core.bridge import ScaleBridge
from typing import Dict, Any

class MyBridge(ScaleBridge):
    def convert(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # Conversion logic
        output_data = {
            "positions": self._extract_positions(input_data),
            "velocities": self._extract_velocities(input_data)
        }
        return output_data

    def validate(self, input_data: Dict[str, Any],
                 output_data: Dict[str, Any]) -> bool:
        # Validation logic
        return len(output_data["positions"]) > 0
```

## See Also

- [Engines API](engines.md) - Engine-specific implementations
- [Bridges API](bridges.md) - Scale bridge implementations
- [Utilities API](utils.md) - Helper functions
