# Architecture Overview

NanoSim is designed as a multi-scale simulation platform that bridges three distinct computational scales relevant to nanomedicine.

## Design Principles

1. **Modularity**: Each simulation engine is encapsulated in its own module
2. **Abstraction**: Common interfaces for all simulation types
3. **Extensibility**: Easy to add new engines or scale bridges
4. **Reproducibility**: Configuration-driven, version-controlled workflows

## System Architecture

```mermaid
flowchart TB
    subgraph Interface["User Interface Layer"]
        CLI[CLI Commands]
        API[REST API]
        Config[YAML Configuration]
    end

    subgraph Orchestrator["Workflow Orchestrator"]
        Parser[Config Parser]
        Validator[Validator]
        Executor[Execution Engine]
        Aggregator[Result Aggregator]
    end

    subgraph Engines["Simulation Engines"]
        direction LR
        Macro[Macro Scale<br/>OpenFOAM<br/>CFD]
        Meso[Meso Scale<br/>GROMACS<br/>MD]
        Micro[Micro Scale<br/>AutoDock Vina<br/>Docking]
    end

    subgraph Bridges["Scale Bridges"]
        B1[Macro→Meso<br/>Bridge]
        B2[Meso→Micro<br/>Bridge]
    end

    Interface --> Orchestrator
    Orchestrator --> Macro
    Macro --> B1
    B1 --> Meso
    Meso --> B2
    B2 --> Micro
    Micro --> Aggregator

    style Macro fill:#e1f5ff,stroke:#0288d1,stroke-width:2px
    style Meso fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Micro fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style B1 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style B2 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style Orchestrator fill:#fce4ec,stroke:#c2185b,stroke-width:2px
```

## Core Components

### Simulation Engines

Each simulation engine implements the `SimulationEngine` abstract base class:

```python
class SimulationEngine(ABC):
    @abstractmethod
    def validate_config(self) -> None:
        """Validate engine configuration."""

    @abstractmethod
    def setup(self) -> None:
        """Set up simulation environment."""

    @abstractmethod
    def run(self) -> SimulationResult:
        """Execute simulation."""

    @abstractmethod
    def cleanup(self) -> None:
        """Clean up resources."""
```

### Scale Bridges

Scale bridges convert outputs from one scale to inputs for the next:

- **MacroToMesoBridge**: Converts CFD results (velocity fields, concentration gradients) to MD initial conditions
- **MesoToMicroBridge**: Converts MD trajectories (conformations, binding sites) to docking inputs

### Workflow Orchestrator

Manages the execution flow:

1. Parse configuration
2. Validate inputs
3. Execute simulations in sequence
4. Bridge data between scales
5. Collect and aggregate results

### CLI and API

- **CLI**: Command-line interface for interactive use
- **API**: REST API for programmatic access and integration

## Data Flow

```mermaid
flowchart TD
    Start[User Config<br/>YAML] --> Validate[Configuration<br/>Validation]
    Validate --> Macro[Macro Scale<br/>OpenFOAM<br/>CFD Simulation]
    Macro --> |"Velocity fields<br/>Concentration"| Bridge1[Macro→Meso<br/>Bridge]
    Bridge1 --> |"Initial positions<br/>Velocities"| Meso[Meso Scale<br/>GROMACS<br/>MD Simulation]
    Meso --> |"Trajectories<br/>Conformations"| Bridge2[Meso→Micro<br/>Bridge]
    Bridge2 --> |"Binding sites<br/>Structures"| Micro[Micro Scale<br/>AutoDock Vina<br/>Docking]
    Micro --> Results[Result<br/>Aggregation]
    Results --> Output[Final Output<br/>JSON/CSV/HDF5]

    style Start fill:#e3f2fd,stroke:#1976d2
    style Validate fill:#fff9c4,stroke:#f57f17
    style Macro fill:#e1f5ff,stroke:#0288d1,stroke-width:2px
    style Meso fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Micro fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style Bridge1 fill:#e8f5e9,stroke:#388e3c
    style Bridge2 fill:#e8f5e9,stroke:#388e3c
    style Results fill:#fce4ec,stroke:#c2185b
    style Output fill:#e0f2f1,stroke:#00695c
```

## Technology Stack

- **Language**: Python 3.11+
- **CLI**: Click
- **API**: FastAPI
- **Testing**: Pytest
- **Documentation**: MkDocs with Material theme
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## Next Steps

- [Multi-scale Approach](multiscale.md) - Deep dive into scale integration
- [Scale Bridging](bridging.md) - Data conversion details
