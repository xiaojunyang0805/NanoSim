# NanoSim Documentation

Welcome to **NanoSim**, the open-source multi-scale nanomedicine simulation platform.

## What is NanoSim?

NanoSim integrates three powerful simulation engines to provide comprehensive drug delivery modeling across multiple scales:

- **Macro Scale (CFD)**: OpenFOAM for continuum-level flow dynamics
- **Meso Scale (MD)**: GROMACS for molecular dynamics simulations
- **Micro Scale (Docking)**: AutoDock Vina for protein-ligand interactions

## Key Features

- **Multi-scale Integration**: Seamlessly bridge between macro, meso, and micro scales
- **Open Source**: AGPL-3.0 licensed, fully transparent and extensible
- **Production Ready**: Docker-based deployment, comprehensive testing
- **User Friendly**: Simple CLI and YAML-based configuration

## Quick Example

```yaml
# config.yaml
project:
  name: "liposome_her2"
  description: "Liposome targeting HER2"

scales:
  - macro
  - meso
  - micro

macro:
  engine: openfoam
  parameters:
    particle_diameter: 100e-9
    simulation_time: 10

meso:
  engine: gromacs
  parameters:
    temperature: 310
    simulation_time: 100e-9

micro:
  engine: autodock_vina
  parameters:
    exhaustiveness: 8
```

```bash
# Run simulation
nanosim run --config config.yaml --output results/
```

## Getting Started

1. [Installation](installation.md) - Set up NanoSim on your system
2. [Quick Start](guide/quickstart.md) - Run your first simulation
3. [Architecture Overview](architecture/overview.md) - Understand the design

## Community

- **Website**: [nanosim.seenano.nl](https://nanosim.seenano.nl)
- **GitHub**: [xiaojunyang0805/NanoSim](https://github.com/xiaojunyang0805/NanoSim)
- **Email**: [support@seenano.nl](mailto:support@seenano.nl)

## License

NanoSim is licensed under the [AGPL-3.0 License](https://github.com/xiaojunyang0805/NanoSim/blob/main/LICENSE).
