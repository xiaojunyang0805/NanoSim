# Quick Start Guide

Get started with NanoSim in 30 minutes or less.

## Step 1: Installation

```bash
pip install nanosim
```

Verify installation:

```bash
nanosim version
```

## Step 2: Create a Configuration File

Generate a template configuration:

```bash
nanosim init --output my_simulation.yaml
```

This creates a file like:

```yaml
# my_simulation.yaml
project:
  name: "My Simulation"
  description: "Description of your simulation"

scales:
  - macro
  - meso
  - micro

macro:
  engine: openfoam
  parameters:
    particle_diameter: 100e-9  # meters
    simulation_time: 10  # seconds

meso:
  engine: gromacs
  parameters:
    temperature: 310  # Kelvin
    simulation_time: 100e-9  # seconds

micro:
  engine: autodock_vina
  parameters:
    exhaustiveness: 8

output:
  format: [json, csv]
  visualization: true
```

## Step 3: Run Your First Simulation

```bash
nanosim run --config my_simulation.yaml --output results/
```

Expected output:

```
Loading configuration from my_simulation.yaml
Output directory: results/
✓ Configuration validated
✓ Macro scale simulation completed
✓ Meso scale simulation completed
✓ Micro scale simulation completed
Results saved to: results/
```

## Step 4: Check Status

```bash
nanosim status <workflow_id>
```

## Step 5: View Results

```bash
# View as text
nanosim results <workflow_id>

# View as JSON
nanosim results <workflow_id> --format json

# Generate visualization
nanosim results <workflow_id> --visualize
```

## Example: Liposome-HER2 Targeting

Here's a complete example simulating a liposome targeting HER2 receptors:

```yaml
project:
  name: "liposome_her2_targeting"
  description: "100nm liposome targeting HER2 in blood flow"

scales:
  - macro
  - meso
  - micro

macro:
  engine: openfoam
  parameters:
    particle_diameter: 100e-9  # 100 nm
    flow_velocity: 0.001  # m/s (capillary flow)
    simulation_time: 10  # seconds
    geometry: "blood_vessel"

meso:
  engine: gromacs
  parameters:
    temperature: 310  # 37°C in Kelvin
    pressure: 1.0  # bar
    simulation_time: 100e-9  # 100 ns
    force_field: "charmm36"
    water_model: "tip3p"

micro:
  engine: autodock_vina
  parameters:
    receptor: "HER2_extracellular_domain.pdbqt"
    ligand: "targeting_antibody.pdbqt"
    center_x: 0.0
    center_y: 0.0
    center_z: 0.0
    size_x: 20.0
    size_y: 20.0
    size_z: 20.0
    exhaustiveness: 8
    num_modes: 9

output:
  format: [json, csv, hdf5]
  visualization: true
  save_trajectories: true
```

Run it:

```bash
nanosim run --config liposome_her2.yaml --output results/ --verbose
```

## What's Happening?

1. **Macro Scale**: OpenFOAM simulates the liposome moving through blood flow
2. **Scale Bridging**: Converts flow data to molecular positions
3. **Meso Scale**: GROMACS simulates the liposome-cell membrane interaction
4. **Scale Bridging**: Extracts binding site conformations
5. **Micro Scale**: AutoDock Vina predicts antibody-HER2 binding affinity

## Next Steps

- [Configuration Guide](configuration.md) - Detailed configuration options
- [OpenFOAM Integration](openfoam.md) - Macro scale setup
- [GROMACS Integration](gromacs.md) - Meso scale setup
- [AutoDock Integration](autodock.md) - Micro scale setup

## Troubleshooting

### Issue: "Engine not found"

Make sure simulation engines are installed:

```bash
# Check Docker images
docker images | grep -E 'openfoam|gromacs|autodock'
```

### Issue: "Configuration validation failed"

Check your YAML syntax:

```bash
# Validate YAML
python -c "import yaml; yaml.safe_load(open('my_simulation.yaml'))"
```

### Issue: "Permission denied"

Make sure output directory is writable:

```bash
mkdir -p results/
chmod 755 results/
```

## Getting Help

- **Documentation**: [Full docs](../index.md)
- **GitHub Issues**: [Report bugs](https://github.com/xiaojunyang0805/NanoSim/issues)
- **Email**: support@seenano.nl
