"""
Generate molecular structure images using PyMOL.

Requirements:
    pip install pymol-open-source
    or download PyMOL from https://pymol.org/

Usage:
    python generate_pymol_images.py
"""

import os
import sys

# Configuration
OUTPUT_DIR = "use-cases"
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 800
DPI = 300


def generate_her2_antibody_docking():
    """Generate HER2-antibody complex visualization."""
    try:
        import pymol
        from pymol import cmd
    except ImportError:
        print("ERROR: PyMOL not installed.")
        print("Install with: pip install pymol-open-source")
        print("Or download from: https://pymol.org/")
        return False

    print("Generating HER2-antibody docking image...")

    # Start PyMOL
    pymol.finish_launching()

    # Fetch HER2-trastuzumab complex structure
    cmd.fetch("3pp0")  # HER2 receptor with trastuzumab antibody

    # Clean up
    cmd.remove("solvent")
    cmd.remove("resn HOH")

    # Style the receptor (chain A)
    cmd.hide("everything", "chain A")
    cmd.show("cartoon", "chain A")
    cmd.show("surface", "chain A")
    cmd.color("cyan", "chain A")
    cmd.set("transparency", 0.4, "chain A")

    # Style the antibody (chains H and L)
    cmd.hide("everything", "chain H+L")
    cmd.show("cartoon", "chain H+L")
    cmd.color("magenta", "chain H")
    cmd.color("pink", "chain L")

    # Highlight binding interface
    cmd.select("interface", "chain A within 4 of chain H+L")
    cmd.show("sticks", "interface")
    cmd.color("yellow", "interface")

    # Set background and view
    cmd.bg_color("white")
    cmd.set("ray_shadow", 0)
    cmd.set("antialias", 2)
    cmd.orient()

    # Render high-quality image
    output_path = os.path.join(OUTPUT_DIR, "her2-antibody-docking.png")
    cmd.ray(IMAGE_WIDTH, IMAGE_HEIGHT)
    cmd.png(output_path, dpi=DPI)

    print(f"✓ Saved: {output_path}")

    # Generate alternative view (rotated)
    cmd.turn("y", 90)
    output_path_2 = os.path.join(OUTPUT_DIR, "her2-antibody-side-view.png")
    cmd.ray(IMAGE_WIDTH, IMAGE_HEIGHT)
    cmd.png(output_path_2, dpi=DPI)

    print(f"✓ Saved: {output_path_2}")

    # Close PyMOL
    cmd.quit()
    return True


def generate_protein_ligand_complex():
    """Generate generic protein-ligand docking example."""
    try:
        import pymol
        from pymol import cmd
    except ImportError:
        return False

    print("Generating protein-ligand complex...")

    pymol.finish_launching()

    # Fetch a well-known protein-ligand complex
    cmd.fetch("1hsg")  # HIV protease with inhibitor

    # Style
    cmd.remove("solvent")
    cmd.hide("everything")
    cmd.show("surface", "polymer")
    cmd.color("lightteal", "polymer")
    cmd.set("transparency", 0.3, "polymer")

    # Show ligand
    cmd.select("ligand", "organic")
    cmd.show("sticks", "ligand")
    cmd.color("yellow", "ligand")
    cmd.util.cbag("ligand")  # Color by atom type

    # Show binding site
    cmd.select("binding_site", "polymer within 5 of ligand")
    cmd.show("sticks", "binding_site")
    cmd.color("cyan", "binding_site")

    # View
    cmd.bg_color("white")
    cmd.orient("ligand")
    cmd.zoom("ligand", 8)

    # Render
    output_path = os.path.join(OUTPUT_DIR, "protein-ligand-docking.png")
    cmd.ray(IMAGE_WIDTH, IMAGE_HEIGHT)
    cmd.png(output_path, dpi=DPI)

    print(f"✓ Saved: {output_path}")

    cmd.quit()
    return True


def generate_membrane_protein():
    """Generate membrane protein visualization."""
    try:
        import pymol
        from pymol import cmd
    except ImportError:
        return False

    print("Generating membrane protein...")

    pymol.finish_launching()

    # Fetch membrane protein
    cmd.fetch("1okc")  # Potassium channel

    # Clean
    cmd.remove("solvent")

    # Style protein
    cmd.hide("everything")
    cmd.show("cartoon", "polymer")
    cmd.color("purple", "polymer")

    # Add pseudo-membrane planes
    cmd.pseudoatom("membrane_upper", pos=[0, 0, 15])
    cmd.pseudoatom("membrane_lower", pos=[0, 0, -15])

    # View
    cmd.bg_color("white")
    cmd.orient()

    # Render
    output_path = os.path.join(OUTPUT_DIR, "membrane-protein.png")
    cmd.ray(IMAGE_WIDTH, IMAGE_HEIGHT)
    cmd.png(output_path, dpi=DPI)

    print(f"✓ Saved: {output_path}")

    cmd.quit()
    return True


def main():
    """Generate all PyMOL images."""
    print("=" * 60)
    print("NanoSim Image Generator - PyMOL Module")
    print("=" * 60)
    print()

    # Create output directory if needed
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Check if PyMOL is available
    try:
        import importlib.util

        if importlib.util.find_spec("pymol") is None:
            raise ImportError("PyMOL not found")
        print("[OK] PyMOL found")
    except ImportError:
        print("[ERROR] PyMOL not found")
        print()
        print("Please install PyMOL:")
        print("  Option 1: pip install pymol-open-source")
        print("  Option 2: Download from https://pymol.org/")
        print()
        sys.exit(1)

    print()
    print("Generating images...")
    print("-" * 60)

    # Generate images
    success_count = 0

    if generate_her2_antibody_docking():
        success_count += 1

    if generate_protein_ligand_complex():
        success_count += 1

    if generate_membrane_protein():
        success_count += 1

    print("-" * 60)
    print(f"✓ Generated {success_count} images successfully")
    print()
    print("Next steps:")
    print("  1. Check the 'use-cases' folder for generated images")
    print("  2. Convert to WebP: python convert_to_webp.py")
    print("  3. Add to landing page HTML")
    print()


if __name__ == "__main__":
    main()
