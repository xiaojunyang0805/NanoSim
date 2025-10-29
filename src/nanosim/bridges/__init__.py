"""Scale bridging modules for multi-scale simulation integration.

This package provides bidirectional bridges between simulation scales:
- Macro (CFD) <-> Meso (MD)
- Meso (MD) <-> Micro (Docking)

Supports both workflow paradigms:
1. Standard drug discovery: Macro -> Micro (Docking) -> Meso (MD validation)
2. Membrane targeting: Macro -> Meso (MD) -> Micro (Docking) -> Meso (MD validation)
"""

from .macro_to_meso import OpenFoamToGromacsConverter
from .meso_to_micro import GromacsToVinaConverter
from .micro_to_meso import VinaToGromacsConverter

__all__ = [
    "OpenFoamToGromacsConverter",
    "GromacsToVinaConverter",
    "VinaToGromacsConverter",
]
