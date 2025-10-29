"""
Generate use case illustration diagrams using matplotlib.

This is an alternative to PyMOL-generated images for users who don't have PyMOL installed.
Creates simplified scientific illustrations for the use cases section.

Requirements:
    pip install matplotlib numpy

Usage:
    python generate_use_case_diagrams.py
"""

import os

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle, Wedge

# Configuration
DPI = 300
FIGSIZE = (12, 8)

# NanoSim brand colors
COLOR_MACRO = "#3b82f6"
COLOR_MESO = "#8b5cf6"
COLOR_MICRO = "#ec4899"
COLOR_PRIMARY = "#2563eb"


def generate_her2_targeting():
    """Generate HER2-targeted drug delivery illustration."""
    print("Generating HER2-targeted drug delivery illustration...")

    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.axis("off")

    # Title
    ax.text(
        6,
        7.5,
        "HER2-Targeted Nanoparticle Drug Delivery",
        ha="center",
        fontsize=14,
        fontweight="bold",
        color=COLOR_PRIMARY,
    )

    # Cancer cell (large)
    cell = Circle((6, 4), 2.5, color="#ffcccc", alpha=0.3, edgecolor="#ff6666", linewidth=3)
    ax.add_patch(cell)
    ax.text(6, 4, "Cancer Cell", ha="center", fontsize=11, fontweight="bold", color="#cc0000")

    # HER2 receptors on cell membrane
    receptor_angles = np.linspace(0, 360, 12, endpoint=False)
    for angle in receptor_angles:
        rad = np.radians(angle)
        x = 6 + 2.5 * np.cos(rad)
        y = 4 + 2.5 * np.sin(rad)
        # Receptor
        receptor = Rectangle((x - 0.15, y - 0.15), 0.3, 0.4, color=COLOR_MESO, alpha=0.8, zorder=10)
        ax.add_patch(receptor)
        # Label a few
        if angle in [0, 90, 180, 270]:
            dx = 0.6 * np.cos(rad)
            dy = 0.6 * np.sin(rad)
            if angle == 0:
                ax.text(
                    x + dx + 0.3,
                    y + dy,
                    "HER2",
                    fontsize=8,
                    color=COLOR_MESO,
                    fontweight="bold",
                )

    # Nanoparticle approaching
    np_x, np_y = 2.5, 6
    nanoparticle = Circle(
        (np_x, np_y), 0.6, color=COLOR_MACRO, alpha=0.7, edgecolor="navy", linewidth=2
    )
    ax.add_patch(nanoparticle)

    # Drug molecules inside nanoparticle
    for _ in range(5):
        dx = np.random.uniform(-0.3, 0.3)
        dy = np.random.uniform(-0.3, 0.3)
        drug = Circle((np_x + dx, np_y + dy), 0.08, color="yellow", alpha=0.8)
        ax.add_patch(drug)

    # Antibody targeting ligands on nanoparticle surface
    for angle in [30, 90, 150, 210, 270, 330]:
        rad = np.radians(angle)
        x = np_x + 0.6 * np.cos(rad)
        y = np_y + 0.6 * np.sin(rad)
        # Y-shaped antibody
        ax.plot(
            [x, x + 0.3 * np.cos(rad)],
            [y, y + 0.3 * np.sin(rad)],
            color=COLOR_MICRO,
            linewidth=3,
            alpha=0.9,
        )
        ax.plot(
            [x + 0.3 * np.cos(rad), x + 0.4 * np.cos(rad - 0.3)],
            [y + 0.3 * np.sin(rad), y + 0.4 * np.sin(rad - 0.3)],
            color=COLOR_MICRO,
            linewidth=2,
            alpha=0.9,
        )
        ax.plot(
            [x + 0.3 * np.cos(rad), x + 0.4 * np.cos(rad + 0.3)],
            [y + 0.3 * np.sin(rad), y + 0.4 * np.sin(rad + 0.3)],
            color=COLOR_MICRO,
            linewidth=2,
            alpha=0.9,
        )

    ax.text(np_x, np_y - 1.2, "Nanoparticle\n(Doxorubicin)", ha="center", fontsize=9)

    # Arrow showing targeting
    ax.annotate(
        "",
        xy=(4.2, 5.2),
        xytext=(3.3, 5.8),
        arrowprops={"arrowstyle": "->", "lw": 3, "color": COLOR_PRIMARY},
    )
    ax.text(3.5, 6.5, "Targeting", fontsize=9, color=COLOR_PRIMARY, fontweight="bold")

    # Second nanoparticle bound to receptor
    np2_angle = np.radians(45)
    np2_x = 6 + 3.3 * np.cos(np2_angle)
    np2_y = 4 + 3.3 * np.sin(np2_angle)
    nanoparticle2 = Circle(
        (np2_x, np2_y), 0.5, color=COLOR_MACRO, alpha=0.8, edgecolor="navy", linewidth=2
    )
    ax.add_patch(nanoparticle2)

    # Connection to receptor
    receptor_x = 6 + 2.5 * np.cos(np2_angle)
    receptor_y = 4 + 2.5 * np.sin(np2_angle)
    ax.plot(
        [np2_x, receptor_x], [np2_y, receptor_y], color=COLOR_MICRO, linewidth=3, linestyle="--"
    )
    ax.text(np2_x + 0.3, np2_y + 0.8, "Binding", fontsize=8, color=COLOR_MICRO, fontweight="bold")

    # Legend
    legend_elements = [
        mpatches.Patch(color=COLOR_MACRO, label="Nanoparticle carrier"),
        mpatches.Patch(color=COLOR_MICRO, label="Trastuzumab antibody"),
        mpatches.Patch(color=COLOR_MESO, label="HER2 receptor"),
        mpatches.Patch(color="yellow", label="Doxorubicin drug"),
    ]
    ax.legend(handles=legend_elements, loc="lower left", fontsize=9)

    # Scale annotation
    ax.text(
        10,
        0.5,
        "Scale: ~100-200 nm",
        fontsize=8,
        style="italic",
        color="#666666",
        ha="right",
    )

    output_path = os.path.join("use-cases", "her2-targeted-delivery.png")
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"[OK] Saved: {output_path}")


def generate_mrna_vaccine():
    """Generate mRNA vaccine delivery illustration."""
    print("Generating mRNA vaccine delivery illustration...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left panel: Lipid nanoparticle structure
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title(
        "mRNA Lipid Nanoparticle (LNP)", fontsize=12, fontweight="bold", pad=20, color=COLOR_PRIMARY
    )

    # Outer lipid bilayer (circular)
    circle_outer = Circle((5, 5), 3, fill=False, edgecolor=COLOR_MESO, linewidth=8, alpha=0.6)
    ax1.add_patch(circle_outer)

    # Inner lipid layer
    circle_inner = Circle((5, 5), 2.7, fill=False, edgecolor=COLOR_MESO, linewidth=6, alpha=0.4)
    ax1.add_patch(circle_inner)

    # Lipid heads (small circles on outer layer)
    for angle in np.linspace(0, 360, 40, endpoint=False):
        rad = np.radians(angle)
        x = 5 + 3 * np.cos(rad)
        y = 5 + 3 * np.sin(rad)
        head = Circle((x, y), 0.15, color=COLOR_MESO, alpha=0.8)
        ax1.add_patch(head)

    # mRNA strands inside (wavy lines)
    np.random.seed(42)
    for i in range(3):
        angle_offset = i * 120
        t = np.linspace(0, 4 * np.pi, 100)
        radius = 1.5 + i * 0.3
        x = 5 + radius * np.cos(t / 4 + np.radians(angle_offset)) * np.exp(-t / 20)
        y = 5 + radius * np.sin(t / 4 + np.radians(angle_offset)) * np.exp(-t / 20)
        ax1.plot(x, y, color="red", linewidth=2, alpha=0.7)

    ax1.text(5, 1, "mRNA cargo", ha="center", fontsize=9, color="red", fontweight="bold")

    # Labels
    ax1.text(
        8.5, 5, "Ionizable\nlipids", fontsize=8, ha="center", color=COLOR_MESO, fontweight="bold"
    )
    ax1.text(5, 8.5, "~80-100 nm", fontsize=9, style="italic", ha="center", color="#666666")

    # Right panel: Cellular uptake process
    ax2.set_xlim(0, 12)
    ax2.set_ylim(0, 10)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title(
        "Cellular Uptake & Endosomal Escape",
        fontsize=12,
        fontweight="bold",
        pad=20,
        color=COLOR_PRIMARY,
    )

    # Cell membrane
    membrane_y = 3
    for x in np.linspace(0, 12, 60):
        y_offset = 0.1 * np.sin(x * 2)
        circle = Circle((x, membrane_y + y_offset), 0.12, color=COLOR_MESO, alpha=0.6)
        ax2.add_patch(circle)

    ax2.text(1, membrane_y - 0.5, "Cell membrane", fontsize=8, color=COLOR_MESO)

    # LNP approaching
    lnp1 = Circle((3, 5.5), 0.4, color=COLOR_MACRO, alpha=0.7, edgecolor="navy", linewidth=2)
    ax2.add_patch(lnp1)
    ax2.arrow(3, 5, 0, -1, head_width=0.3, head_length=0.3, fc=COLOR_PRIMARY, ec=COLOR_PRIMARY)

    # Endocytosis (LNP being engulfed)
    lnp2_x, lnp2_y = 6, 2.8
    lnp2 = Circle(
        (lnp2_x, lnp2_y), 0.4, color=COLOR_MACRO, alpha=0.7, edgecolor="navy", linewidth=2
    )
    ax2.add_patch(lnp2)
    # Membrane wrapping around
    arc1 = Wedge((lnp2_x, lnp2_y), 0.8, 180, 360, width=0.2, color=COLOR_MESO, alpha=0.5, zorder=5)
    ax2.add_patch(arc1)

    # Endosome
    endosome_x, endosome_y = 9, 2
    endosome = Circle(
        (endosome_x, endosome_y), 0.8, fill=False, edgecolor="orange", linewidth=3, linestyle="--"
    )
    ax2.add_patch(endosome)
    lnp3 = Circle(
        (endosome_x, endosome_y), 0.4, color=COLOR_MACRO, alpha=0.8, edgecolor="navy", linewidth=2
    )
    ax2.add_patch(lnp3)
    ax2.text(endosome_x, endosome_y - 1.3, "Endosome", fontsize=8, ha="center", color="orange")

    # mRNA release
    for i in range(3):
        angle = 30 + i * 40
        rad = np.radians(angle)
        x_end = endosome_x + 1.2 * np.cos(rad)
        y_end = endosome_y + 1.2 * np.sin(rad)
        ax2.plot(
            [endosome_x, x_end],
            [endosome_y, y_end],
            color="red",
            linewidth=2,
            alpha=0.7,
            linestyle=":",
        )

    ax2.text(10.5, 3.5, "mRNA\nrelease", fontsize=8, ha="center", color="red", fontweight="bold")

    # Cytoplasm label
    ax2.text(1, 1, "Cytoplasm", fontsize=9, style="italic", color="#666666")

    # Process labels
    ax2.text(3, 6.5, "1. Approach", fontsize=8, color=COLOR_PRIMARY, fontweight="bold")
    ax2.text(6, 4, "2. Endocytosis", fontsize=8, color=COLOR_PRIMARY, fontweight="bold")
    ax2.text(9, 4, "3. Escape", fontsize=8, color=COLOR_PRIMARY, fontweight="bold")

    plt.tight_layout()
    output_path = os.path.join("use-cases", "mrna-vaccine-delivery.png")
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"[OK] Saved: {output_path}")


def generate_blood_brain_barrier():
    """Generate blood-brain barrier crossing illustration."""
    print("Generating blood-brain barrier crossing illustration...")

    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

    # Title
    ax.text(
        7,
        9.5,
        "Crossing the Blood-Brain Barrier",
        ha="center",
        fontsize=14,
        fontweight="bold",
        color=COLOR_PRIMARY,
    )

    # Blood vessel (top)
    vessel = FancyBboxPatch(
        (1, 6),
        12,
        2,
        boxstyle="round,pad=0.2",
        facecolor="#ffcccc",
        alpha=0.3,
        edgecolor="#ff6666",
        linewidth=3,
    )
    ax.add_patch(vessel)
    ax.text(2, 7.5, "Blood Vessel", fontsize=10, color="#cc0000", fontweight="bold")

    # Red blood cells
    for x in [3, 5, 7, 9, 11]:
        rbc = mpatches.Ellipse(
            (x, 7), 0.6, 0.3, color="red", alpha=0.4, edgecolor="darkred", linewidth=1
        )
        ax.add_patch(rbc)

    # Endothelial cells forming BBB
    for x in np.linspace(1, 13, 7):
        cell = Rectangle(
            (x - 0.4, 5.2), 0.8, 0.8, color="#99ccff", alpha=0.5, edgecolor="blue", linewidth=2
        )
        ax.add_patch(cell)
        # Nucleus
        nucleus = Circle((x, 5.6), 0.15, color="darkblue", alpha=0.6)
        ax.add_patch(nucleus)

    # Tight junctions
    for x in np.linspace(1.4, 12.6, 6):
        ax.plot([x, x], [5.2, 6], color="darkblue", linewidth=3, alpha=0.8)
        ax.plot([x - 0.1, x], [5.4, 5.2], color="darkblue", linewidth=2, alpha=0.8)
        ax.plot([x + 0.1, x], [5.4, 5.2], color="darkblue", linewidth=2, alpha=0.8)

    ax.text(13, 5.6, "BBB", fontsize=9, color="blue", fontweight="bold")

    # Brain tissue (bottom)
    brain = FancyBboxPatch(
        (1, 0.5),
        12,
        4,
        boxstyle="round,pad=0.2",
        facecolor="#e6ccff",
        alpha=0.3,
        edgecolor="#9966cc",
        linewidth=3,
    )
    ax.add_patch(brain)
    ax.text(2, 2, "Brain Tissue", fontsize=10, color="#663399", fontweight="bold")

    # Neurons
    for pos in [(3.5, 2), (6, 1.5), (9, 2.5), (11, 1.8)]:
        # Cell body
        neuron_body = Circle(pos, 0.3, color="#cc99ff", alpha=0.7, edgecolor="#663399", linewidth=2)
        ax.add_patch(neuron_body)
        # Dendrites
        for angle in [30, 90, 150, 210, 270, 330]:
            rad = np.radians(angle)
            x_end = pos[0] + 0.5 * np.cos(rad)
            y_end = pos[1] + 0.5 * np.sin(rad)
            ax.plot([pos[0], x_end], [pos[1], y_end], color="#663399", linewidth=1.5, alpha=0.7)

    # Nanoparticles attempting to cross
    # Failed crossing (standard NP)
    np_fail = Circle((4, 7), 0.3, color="#cccccc", alpha=0.6, edgecolor="gray", linewidth=2)
    ax.add_patch(np_fail)
    ax.text(4, 8.2, "Standard NP\n(blocked)", ha="center", fontsize=8, color="gray")

    # Successful crossing (functionalized NP)
    np_success_positions = [(8, 7.2), (8.2, 6.5), (8.3, 5.8), (8.4, 5), (8.5, 3.5)]

    for i, (x, y) in enumerate(np_success_positions):
        alpha_val = 0.9 - i * 0.15
        np_cross = Circle(
            (x, y), 0.25, color=COLOR_MACRO, alpha=alpha_val, edgecolor="navy", linewidth=2
        )
        ax.add_patch(np_cross)

        # Targeting ligands
        if i == 0:
            for angle in [0, 120, 240]:
                rad = np.radians(angle)
                lx = x + 0.25 * np.cos(rad)
                ly = y + 0.25 * np.sin(rad)
                ligand = Circle((lx, ly), 0.08, color=COLOR_MICRO, alpha=0.9)
                ax.add_patch(ligand)

    # Arrow showing pathway
    ax.annotate(
        "",
        xy=(8.5, 4),
        xytext=(8, 7),
        arrowprops={"arrowstyle": "->", "lw": 2, "color": COLOR_PRIMARY, "linestyle": "--"},
    )

    ax.text(
        8,
        8.5,
        "Functionalized NP\n(transferrin)",
        ha="center",
        fontsize=8,
        color=COLOR_MACRO,
        fontweight="bold",
    )
    ax.text(9.5, 4.5, "Transcytosis", fontsize=8, color=COLOR_PRIMARY, fontweight="bold")

    # Legend
    legend_elements = [
        mpatches.Patch(color=COLOR_MACRO, label="Functionalized nanoparticle"),
        mpatches.Patch(color=COLOR_MICRO, label="Targeting ligand (transferrin)"),
        mpatches.Patch(color="blue", label="Tight junctions"),
        mpatches.Patch(color="#cc99ff", label="Neurons"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=8)

    output_path = os.path.join("use-cases", "blood-brain-barrier.png")
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"[OK] Saved: {output_path}")


def main():
    """Generate all use case diagram images."""
    print("=" * 60)
    print("NanoSim Use Case Diagrams Generator")
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

    # Create output directory
    os.makedirs("use-cases", exist_ok=True)

    print()
    print("Generating use case diagrams...")
    print("-" * 60)

    # Generate all diagrams
    try:
        generate_her2_targeting()
        generate_mrna_vaccine()
        generate_blood_brain_barrier()
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        import traceback

        traceback.print_exc()
        return

    print("-" * 60)
    print("[OK] All use case diagrams generated successfully")
    print()
    print("Generated files:")
    print("  use-cases/her2-targeted-delivery.png")
    print("  use-cases/mrna-vaccine-delivery.png")
    print("  use-cases/blood-brain-barrier.png")
    print()
    print("Next steps:")
    print("  1. Convert to WebP: python convert_to_webp.py")
    print("  2. Add to landing page HTML use cases section")
    print()


if __name__ == "__main__":
    main()
