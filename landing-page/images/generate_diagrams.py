"""
Generate scientific diagrams and visualizations using Python.

Requirements:
    pip install matplotlib numpy pillow

Usage:
    python generate_diagrams.py
"""

import os

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

# Configuration
DPI = 300
FIGSIZE_WIDE = (12, 4)
FIGSIZE_SQUARE = (8, 8)

# NanoSim brand colors
COLOR_MACRO = "#3b82f6"
COLOR_MESO = "#8b5cf6"
COLOR_MICRO = "#ec4899"
COLOR_PRIMARY = "#2563eb"


def generate_three_scale_comparison():
    """Generate three-scale comparison image."""
    print("Generating three-scale comparison...")

    fig, axes = plt.subplots(1, 3, figsize=FIGSIZE_WIDE)
    fig.suptitle("Multi-Scale Simulation in NanoSim", fontsize=16, fontweight="bold", y=1.02)

    # Macro Scale
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")

    # Draw blood vessels
    vessel = FancyBboxPatch(
        (1, 2),
        8,
        6,
        boxstyle="round,pad=0.3",
        facecolor=COLOR_MACRO,
        alpha=0.3,
        edgecolor=COLOR_MACRO,
        linewidth=3,
    )
    ax.add_patch(vessel)

    # Add flowing particles
    np.random.seed(42)
    for _ in range(30):
        x = np.random.uniform(1.5, 8.5)
        y = np.random.uniform(2.5, 7.5)
        circle = Circle((x, y), 0.15, color=COLOR_MACRO, alpha=0.6)
        ax.add_patch(circle)

    ax.set_title(
        "MACRO SCALE\nBlood Flow & Transport", fontsize=12, fontweight="bold", color=COLOR_MACRO
    )
    ax.text(5, 0.5, "μm - mm scale\nCFD / OpenFOAM", ha="center", fontsize=9, style="italic")
    ax.axis("off")

    # Meso Scale
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")

    # Draw cell membrane (lipid bilayer)
    membrane_y = 5
    ax.axhline(y=membrane_y, color=COLOR_MESO, linewidth=8, alpha=0.4)
    ax.axhline(y=membrane_y + 0.3, color=COLOR_MESO, linewidth=3, alpha=0.6)
    ax.axhline(y=membrane_y - 0.3, color=COLOR_MESO, linewidth=3, alpha=0.6)

    # Add nanoparticle
    particle = Circle((3, 7), 0.8, color=COLOR_MESO, alpha=0.7, edgecolor="darkviolet", linewidth=2)
    ax.add_patch(particle)

    # Add receptors on membrane
    for x in [2, 4, 6, 8]:
        receptor = FancyBboxPatch(
            (x - 0.2, membrane_y - 0.5), 0.4, 1, facecolor=COLOR_MESO, alpha=0.8
        )
        ax.add_patch(receptor)

    ax.set_title(
        "MESO SCALE\nNP-Cell Interaction", fontsize=12, fontweight="bold", color=COLOR_MESO
    )
    ax.text(5, 0.5, "nm - μm scale\nMD / GROMACS", ha="center", fontsize=9, style="italic")
    ax.axis("off")

    # Micro Scale
    ax = axes[2]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")

    # Draw protein (receptor)
    protein_shape = mpatches.Ellipse(
        (5, 5), 3, 4, color=COLOR_MICRO, alpha=0.3, edgecolor=COLOR_MICRO, linewidth=3
    )
    ax.add_patch(protein_shape)

    # Draw binding pocket
    pocket = Circle((5, 5), 0.8, color="white", edgecolor=COLOR_MICRO, linewidth=2)
    ax.add_patch(pocket)

    # Draw ligand/antibody
    ligand_points = np.array([[3, 6], [4, 7], [5, 6.5], [6, 7], [7, 6]])
    for point in ligand_points:
        circle = Circle(point, 0.25, color=COLOR_MICRO, alpha=0.8)
        ax.add_patch(circle)

    # Draw bonds
    for i in range(len(ligand_points) - 1):
        ax.plot(
            [ligand_points[i][0], ligand_points[i + 1][0]],
            [ligand_points[i][1], ligand_points[i + 1][1]],
            color=COLOR_MICRO,
            linewidth=2,
            alpha=0.6,
        )

    ax.set_title(
        "MICRO SCALE\nMolecular Binding", fontsize=12, fontweight="bold", color=COLOR_MICRO
    )
    ax.text(
        5, 0.5, "Å - nm scale\nDocking / AutoDock Vina", ha="center", fontsize=9, style="italic"
    )
    ax.axis("off")

    plt.tight_layout()
    output_path = os.path.join("scales", "three-scale-comparison.png")
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"[OK] Saved: {output_path}")


def generate_workflow_diagram():
    """Generate bidirectional workflow diagram."""
    print("Generating workflow diagram...")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Standard Workflow (Docking First)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 3)
    ax1.axis("off")
    ax1.set_title("Standard Drug Discovery Workflow", fontsize=14, fontweight="bold", pad=20)

    # Macro box
    macro_box = FancyBboxPatch(
        (0.5, 1),
        2,
        1,
        boxstyle="round,pad=0.1",
        facecolor=COLOR_MACRO,
        alpha=0.3,
        edgecolor=COLOR_MACRO,
        linewidth=3,
    )
    ax1.add_patch(macro_box)
    ax1.text(1.5, 1.5, "MACRO\nTransport", ha="center", va="center", fontsize=10, fontweight="bold")

    # Arrow to Micro
    arrow1 = FancyArrowPatch(
        (2.7, 1.5), (3.8, 1.5), arrowstyle="->", mutation_scale=30, linewidth=3, color="#666666"
    )
    ax1.add_patch(arrow1)

    # Micro box (highlighted)
    micro_box = FancyBboxPatch(
        (4, 1),
        2,
        1,
        boxstyle="round,pad=0.1",
        facecolor=COLOR_MICRO,
        alpha=0.3,
        edgecolor=COLOR_MICRO,
        linewidth=3,
    )
    ax1.add_patch(micro_box)
    ax1.text(
        5, 1.5, "MICRO\nDocking First", ha="center", va="center", fontsize=10, fontweight="bold"
    )

    # Arrow to Meso
    arrow2 = FancyArrowPatch(
        (6.2, 1.5), (7.3, 1.5), arrowstyle="->", mutation_scale=30, linewidth=3, color="#666666"
    )
    ax1.add_patch(arrow2)

    # Meso box
    meso_box = FancyBboxPatch(
        (7.5, 1),
        2,
        1,
        boxstyle="round,pad=0.1",
        facecolor=COLOR_MESO,
        alpha=0.3,
        edgecolor=COLOR_MESO,
        linewidth=3,
    )
    ax1.add_patch(meso_box)
    ax1.text(
        8.5, 1.5, "MESO\nMD Validation", ha="center", va="center", fontsize=10, fontweight="bold"
    )

    ax1.text(
        5,
        0.3,
        "Fast docking screens thousands → MD validates top candidates",
        ha="center",
        fontsize=9,
        style="italic",
    )

    # Membrane Targeting Workflow (MD First)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 3)
    ax2.axis("off")
    ax2.set_title("Membrane Targeting Workflow", fontsize=14, fontweight="bold", pad=20)

    # Macro - same width layout, 4 boxes total
    macro_box2 = FancyBboxPatch(
        (0.5, 1),
        1.5,
        1,
        boxstyle="round,pad=0.1",
        facecolor=COLOR_MACRO,
        alpha=0.3,
        edgecolor=COLOR_MACRO,
        linewidth=3,
    )
    ax2.add_patch(macro_box2)
    ax2.text(
        1.25, 1.5, "MACRO\nTransport", ha="center", va="center", fontsize=10, fontweight="bold"
    )

    arrow1 = FancyArrowPatch(
        (2.15, 1.5), (2.85, 1.5), arrowstyle="->", mutation_scale=30, linewidth=3, color="#666666"
    )
    ax2.add_patch(arrow1)

    # Meso (highlighted first)
    meso_box2 = FancyBboxPatch(
        (3.0, 1),
        1.5,
        1,
        boxstyle="round,pad=0.1",
        facecolor=COLOR_MESO,
        alpha=0.3,
        edgecolor=COLOR_MESO,
        linewidth=3,
    )
    ax2.add_patch(meso_box2)
    ax2.text(
        3.75, 1.5, "MESO\nMembrane MD", ha="center", va="center", fontsize=10, fontweight="bold"
    )

    arrow2 = FancyArrowPatch(
        (4.65, 1.5), (5.35, 1.5), arrowstyle="->", mutation_scale=30, linewidth=3, color="#666666"
    )
    ax2.add_patch(arrow2)

    # Micro
    micro_box2 = FancyBboxPatch(
        (5.5, 1),
        1.5,
        1,
        boxstyle="round,pad=0.1",
        facecolor=COLOR_MICRO,
        alpha=0.3,
        edgecolor=COLOR_MICRO,
        linewidth=3,
    )
    ax2.add_patch(micro_box2)
    ax2.text(6.25, 1.5, "MICRO\nDocking", ha="center", va="center", fontsize=10, fontweight="bold")

    arrow3 = FancyArrowPatch(
        (7.15, 1.5), (7.85, 1.5), arrowstyle="->", mutation_scale=30, linewidth=3, color="#666666"
    )
    ax2.add_patch(arrow3)

    # Meso validation
    meso_box3 = FancyBboxPatch(
        (8.0, 1),
        1.5,
        1,
        boxstyle="round,pad=0.1",
        facecolor=COLOR_MESO,
        alpha=0.3,
        edgecolor=COLOR_MESO,
        linewidth=3,
    )
    ax2.add_patch(meso_box3)
    ax2.text(
        8.75, 1.5, "MESO\nValidation", ha="center", va="center", fontsize=10, fontweight="bold"
    )

    ax2.text(
        5,
        0.3,
        "MD explores membrane → Docking targets receptors → MD validates",
        ha="center",
        fontsize=9,
        style="italic",
    )

    plt.tight_layout()
    output_path = os.path.join("features", "bidirectional-workflow.png")
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"[OK] Saved: {output_path}")


def generate_particle_flow():
    """Generate particle flow visualization for hero background with transparent center."""
    print("Generating particle flow background...")

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.set_facecolor("none")  # Transparent background

    # Generate flowing particles/bubbles on LEFT and RIGHT sides only
    # Avoid center area (x: 5-11) where text will be
    np.random.seed(42)
    n_particles_per_side = 30

    # LEFT side particles (x: 0-4)
    for _ in range(n_particles_per_side):
        x = np.random.uniform(0, 4)
        y = np.random.uniform(0, 9)
        size = np.random.uniform(0.15, 0.6)

        # Mix of blue, purple, pink with low alpha for subtlety
        color_choice = np.random.choice([COLOR_MACRO, COLOR_MESO, COLOR_MICRO])
        alpha = np.random.uniform(0.15, 0.35)

        circle = Circle((x, y), size, color=color_choice, alpha=alpha, zorder=1)
        ax.add_patch(circle)

        # Add subtle glow/outline for bubble effect
        glow = Circle((x, y), size + 0.05, color="white", alpha=0.1, zorder=0)
        ax.add_patch(glow)

    # RIGHT side particles (x: 12-16)
    for _ in range(n_particles_per_side):
        x = np.random.uniform(12, 16)
        y = np.random.uniform(0, 9)
        size = np.random.uniform(0.15, 0.6)

        color_choice = np.random.choice([COLOR_MACRO, COLOR_MESO, COLOR_MICRO])
        alpha = np.random.uniform(0.15, 0.35)

        circle = Circle((x, y), size, color=color_choice, alpha=alpha, zorder=1)
        ax.add_patch(circle)

        # Add glow
        glow = Circle((x, y), size + 0.05, color="white", alpha=0.1, zorder=0)
        ax.add_patch(glow)

    # Add a few very subtle particles in the center for transition
    for _ in range(10):
        x = np.random.uniform(4.5, 11.5)
        y = np.random.uniform(0, 9)
        size = np.random.uniform(0.1, 0.3)

        color_choice = np.random.choice([COLOR_MACRO, COLOR_MESO, COLOR_MICRO])
        alpha = np.random.uniform(0.05, 0.15)  # Very subtle

        circle = Circle((x, y), size, color=color_choice, alpha=alpha)
        ax.add_patch(circle)

    ax.axis("off")

    output_path = os.path.join("hero", "particle-flow-background.png")
    # Save with transparent background
    plt.savefig(
        output_path,
        dpi=150,
        bbox_inches="tight",
        facecolor="none",
        edgecolor="none",
        transparent=True,
    )
    plt.close()

    print(f"[OK] Saved: {output_path}")


def generate_scale_icons():
    """Generate simple icons for each scale."""
    print("Generating scale icons...")

    scales = [
        ("macro", COLOR_MACRO, "Macro\nμm-mm"),
        ("meso", COLOR_MESO, "Meso\nnm-μm"),
        ("micro", COLOR_MICRO, "Micro\nÅ-nm"),
    ]

    for name, color, label in scales:
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect("equal")
        ax.axis("off")

        # Create circle icon
        circle = Circle((5, 5), 3, color=color, alpha=0.7, edgecolor=color, linewidth=3)
        ax.add_patch(circle)

        # Add nested circles for multi-scale effect
        circle2 = Circle((5, 5), 2, color=color, alpha=0.4)
        ax.add_patch(circle2)
        circle3 = Circle((5, 5), 1, color=color, alpha=0.2)
        ax.add_patch(circle3)

        # Add label
        ax.text(
            5, 5, label, ha="center", va="center", fontsize=12, fontweight="bold", color="white"
        )

        output_path = os.path.join("scales", f"{name}-icon.png")
        plt.savefig(
            output_path,
            dpi=DPI,
            bbox_inches="tight",
            facecolor="none",
            edgecolor="none",
            transparent=True,
        )
        plt.close()

        print(f"[OK] Saved: {output_path}")


def main():
    """Generate all diagram images."""
    print("=" * 60)
    print("NanoSim Image Generator - Diagrams Module")
    print("=" * 60)
    print()

    # Check dependencies
    try:
        import importlib.util

        if (
            importlib.util.find_spec("matplotlib") is None
            or importlib.util.find_spec("numpy") is None
        ):
            raise ImportError("matplotlib or numpy not found")
        print("[OK] Dependencies found (matplotlib, numpy)")
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print()
        print("Please install: pip install matplotlib numpy")
        print()
        return

    # Create output directories
    for dir_name in ["scales", "features", "hero"]:
        os.makedirs(dir_name, exist_ok=True)

    print()
    print("Generating diagrams...")
    print("-" * 60)

    # Generate all diagrams
    try:
        generate_three_scale_comparison()
        generate_workflow_diagram()
        generate_particle_flow()
        generate_scale_icons()
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback

        traceback.print_exc()
        return

    print("-" * 60)
    print("[OK] All diagrams generated successfully")
    print()
    print("Generated files:")
    print("  scales/three-scale-comparison.png")
    print("  scales/macro-icon.png, meso-icon.png, micro-icon.png")
    print("  features/bidirectional-workflow.png")
    print("  hero/particle-flow-background.png")
    print()
    print("Next steps:")
    print("  1. Convert to WebP: python convert_to_webp.py")
    print("  2. Add to landing page HTML")
    print()


if __name__ == "__main__":
    main()
