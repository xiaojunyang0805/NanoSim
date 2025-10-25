# Installation

This guide will help you install NanoSim and its dependencies.

## Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerized engines)
- Git

## Installation Methods

### Option 1: pip install (Recommended)

```bash
pip install nanosim
```

### Option 2: From source

```bash
# Clone the repository
git clone https://github.com/xiaojunyang0805/NanoSim.git
cd NanoSim

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Verify Installation

```bash
nanosim version
```

You should see output like:

```
NanoSim v0.1.0

Integrated Simulation Engines:
  • OpenFOAM: 11 (planned)
  • GROMACS: 2024 (planned)
  • AutoDock Vina: 1.2.5 (planned)
```

## Simulation Engine Setup

NanoSim requires external simulation engines to be installed:

### OpenFOAM (Macro Scale)

```bash
# Using Docker (recommended)
docker pull openfoam/openfoam11-paraview510

# Or native installation
# See: https://openfoam.org/download/
```

### GROMACS (Meso Scale)

```bash
# Using Docker (recommended)
docker pull gromacs/gromacs:2024

# Or native installation
# See: https://www.gromacs.org/downloads.html
```

### AutoDock Vina (Micro Scale)

```bash
# Using Docker (recommended)
docker pull ccsb/autodock-vina:1.2.5

# Or native installation
# See: https://github.com/ccsb-scripps/AutoDock-Vina/releases
```

## Configuration

Create a configuration directory:

```bash
mkdir -p ~/.nanosim
nanosim init --output ~/.nanosim/config.yaml
```

Edit `~/.nanosim/config.yaml` to specify engine paths and settings.

## Next Steps

- [Quick Start Guide](guide/quickstart.md) - Run your first simulation
- [Configuration Reference](guide/configuration.md) - Detailed configuration options
