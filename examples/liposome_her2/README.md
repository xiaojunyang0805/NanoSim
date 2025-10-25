# Liposome-HER2 Targeting Example

This example demonstrates a complete multi-scale simulation workflow for a PEGylated liposome targeting HER2 receptors in breast cancer.

## Overview

**Objective**: Model the behavior of a 100nm liposome functionalized with anti-HER2 antibodies (trastuzumab) as it:
1. Travels through blood flow (macro scale)
2. Interacts with cell membranes (meso scale)
3. Binds to HER2 receptors (micro scale)

## Scientific Background

### HER2 (Human Epidermal Growth Receptor 2)
- Overexpressed in ~20% of breast cancers
- Target for antibody-based therapies (e.g., Herceptin/trastuzumab)
- Transmembrane receptor protein

### Liposomal Drug Delivery
- **Size**: 100 nm (optimal for EPR effect)
- **Composition**: DPPC lipid bilayer
- **Surface modification**: PEGylation for increased circulation time
- **Targeting**: Anti-HER2 antibodies for specific binding

## Simulation Scales

### Macro Scale (OpenFOAM)
**Timescale**: Seconds
**Length scale**: Micrometers to millimeters
**Physics**: Continuum fluid dynamics

Simulates:
- Liposome transport in blood flow
- Margination towards vessel walls
- Shear stress effects
- Concentration gradients

**Key output**: Particle trajectories near cell surface

### Meso Scale (GROMACS)
**Timescale**: Nanoseconds
**Length scale**: Nanometers
**Physics**: Molecular dynamics

Simulates:
- Liposome structure and stability
- PEG corona dynamics
- Antibody flexibility
- Initial membrane contact
- Receptor accessibility

**Key output**: Antibody conformations and binding site geometry

### Micro Scale (AutoDock Vina)
**Timescale**: Static (energy minimization)
**Length scale**: Angstroms
**Physics**: Molecular interactions

Simulates:
- Antibody-HER2 binding
- Binding affinity prediction
- Optimal binding modes
- Interaction energy landscape

**Key output**: Binding affinity (ΔG) and bound complex structure

## Running the Simulation

### Prerequisites

1. Install NanoSim:
```bash
pip install nanosim
```

2. Ensure simulation engines are available:
```bash
# Check Docker images (recommended)
docker images | grep -E 'openfoam|gromacs|autodock'

# Or check native installations
which blockMesh  # OpenFOAM
which gmx        # GROMACS
which vina       # AutoDock Vina
```

### Execution

```bash
# From the NanoSim root directory
nanosim run \
  --config examples/liposome_her2/config.yaml \
  --output ./results/liposome_her2 \
  --verbose
```

### Expected Runtime

- **Macro scale**: ~5-10 minutes
- **Meso scale**: ~2-4 hours (depends on GPU availability)
- **Micro scale**: ~10-30 minutes
- **Total**: ~2.5-5 hours

## Input Files

### Required Files

These files should be placed in `examples/liposome_her2/input/`:

1. **HER2_extracellular_domain.pdbqt**
   - HER2 receptor structure
   - Can be obtained from PDB: 1N8Z, 3PP0
   - Must be prepared with hydrogens and charges

2. **trastuzumab_fab.pdbqt**
   - Trastuzumab Fab fragment structure
   - Can be obtained from PDB: 1N8Z
   - Must be prepared for docking

### Generating Input Files

```bash
# Download structures
wget https://files.rcsb.org/download/1N8Z.pdb

# Prepare receptor (requires MGLTools or Open Babel)
prepare_receptor4.py -r 1N8Z.pdb -o HER2_extracellular_domain.pdbqt

# Prepare ligand
prepare_ligand4.py -l trastuzumab_fab.pdb -o trastuzumab_fab.pdbqt
```

## Expected Results

### Macro Scale Outputs

- `velocity_field.vtk`: 3D velocity field visualization
- `particle_trajectories.csv`: Nanoparticle positions over time
- `wall_shear_stress.csv`: Shear stress at vessel walls

### Meso Scale Outputs

- `trajectory.xtc`: MD trajectory (all atomic positions)
- `energies.edr`: Energy components (potential, kinetic, etc.)
- `lipid_order.dat`: Lipid bilayer order parameters
- `antibody_conformations.pdb`: Representative antibody structures

### Micro Scale Outputs

- `docked_poses.pdbqt`: Top 20 binding modes
- `binding_affinities.csv`: ΔG for each mode
- `best_pose.pdb`: Lowest energy bound complex

### Aggregated Results

The workflow will produce an integrated analysis:

```json
{
  "workflow_id": "liposome_her2_20250127_143022",
  "status": "completed",
  "scales": {
    "macro": {
      "mean_velocity": 0.00098,
      "max_shear_stress": 12.3,
      "deposition_probability": 0.15
    },
    "meso": {
      "liposome_stability": "stable",
      "peg_corona_thickness": 8.2,
      "antibody_flexibility": "high"
    },
    "micro": {
      "best_affinity_kcal_mol": -12.4,
      "binding_probability": 0.82,
      "key_interactions": ["H-bonds: 6", "salt bridges: 2"]
    }
  },
  "integrated_metrics": {
    "targeting_efficiency": 0.73,
    "expected_binding_events_per_hour": 42.3
  }
}
```

## Interpreting Results

### Good Targeting Indicators

✓ **Macro**: High margination (close to walls)
✓ **Meso**: Stable liposome structure, accessible antibodies
✓ **Micro**: Strong binding affinity (ΔG < -10 kcal/mol)

### Warning Signs

✗ **Macro**: High shear stress causing aggregation
✗ **Meso**: Liposome instability, PEG entanglement
✗ **Micro**: Weak binding (ΔG > -6 kcal/mol), unfavorable orientation

## Customization

### Modify Liposome Size

Edit `config.yaml`:
```yaml
macro:
  parameters:
    particle_diameter: 150e-9  # Change to 150 nm
```

### Change Temperature

```yaml
meso:
  parameters:
    temperature: 298  # Change to 25°C
```

### Increase Docking Accuracy

```yaml
micro:
  parameters:
    exhaustiveness: 64  # Double the search effort
```

## Validation

Compare your results with experimental data:

- **Liposome size**: Should match DLS measurements (~100 nm)
- **Binding affinity**: Compare with SPR/ITC data for trastuzumab-HER2 (Kd ~5 nM)
- **Circulation time**: Validate PEG effect against literature (hours)

## References

1. Trastuzumab structure: Cho et al., Nature 2003 (PDB: 1N8Z)
2. Liposome parameters: Allen & Cullis, Science 2004
3. HER2 in breast cancer: Slamon et al., Science 1987

## Troubleshooting

### Issue: "Receptor file not found"
**Solution**: Make sure input files are in `examples/liposome_her2/input/`

### Issue: "GROMACS simulation unstable"
**Solution**: Increase equilibration time or reduce time step

### Issue: "Weak binding affinity"
**Solution**: Check antibody orientation, verify PDB structure quality

## Next Steps

After running this example:

1. Modify parameters to test different conditions
2. Try different targeting ligands
3. Explore sensitivity to flow conditions
4. Validate against your experimental data

## Support

Questions? Contact us:
- GitHub Issues: https://github.com/xiaojunyang0805/NanoSim/issues
- Email: support@seenano.nl
