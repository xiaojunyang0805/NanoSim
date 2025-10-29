"""Pre-configured workflows for common use cases.

This package contains reference implementations of standard workflows:
- Standard virtual screening (docking-first)
- Membrane targeting (MD-first)
- Custom workflow templates
"""

from .membrane_targeting import MembraneTargeting
from .standard_vs import StandardVirtualScreening

__all__ = [
    "StandardVirtualScreening",
    "MembraneTargeting",
]
