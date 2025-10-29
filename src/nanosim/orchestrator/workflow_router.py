"""Workflow router for intelligent pipeline selection.

This module determines the optimal workflow based on use case characteristics,
supporting both standard drug discovery (docking-first) and specialized
nanomedicine workflows (MD-first).
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class WorkflowType(Enum):
    """Supported workflow types."""

    DOCKING_FIRST = "docking_first"  # Standard virtual screening
    MD_FIRST = "md_first"  # Membrane targeting, cryptic pockets
    ITERATIVE = "iterative"  # Induced fit, alternating MD-docking
    CUSTOM = "custom"  # User-defined workflow


class ScaleSequence(Enum):
    """Scale execution sequences."""

    MACRO_MICRO_MESO = "macro_micro_meso"  # Standard: CFD → Docking → MD
    MACRO_MESO_MICRO_MESO = "macro_meso_micro_meso"  # Membrane: CFD → MD → Docking → MD
    MICRO_MESO = "micro_meso"  # Direct: Docking → MD validation
    MESO_MICRO = "meso_micro"  # Direct: MD → Docking


@dataclass
class UseCaseCharacteristics:
    """Characteristics of a simulation use case."""

    # Target information
    has_known_receptor_structure: bool
    has_known_binding_site: bool
    receptor_type: str  # 'soluble', 'membrane', 'unknown'

    # Screening scope
    compound_library_size: int  # Number of compounds to screen
    has_target_compounds: bool  # Specific compounds vs. library

    # Biological context
    is_membrane_system: bool
    is_nanoparticle_delivery: bool
    needs_induced_fit: bool
    is_cryptic_pocket: bool

    # Computational resources
    compute_budget: str  # 'limited', 'moderate', 'high'
    time_constraint: str  # 'hours', 'days', 'weeks'

    # Scientific goals
    goal: str  # 'screening', 'validation', 'mechanism', 'optimization'


class WorkflowRouter:
    """Routes simulation requests to appropriate workflows.

    This is the intelligence layer that makes NanoSim adaptive and flexible.
    """

    def __init__(self):
        """Initialize workflow router."""
        self.decision_history: list[dict[str, Any]] = []

    def determine_workflow(self, use_case: UseCaseCharacteristics) -> WorkflowType:
        """Determine optimal workflow based on use case.

        Args:
            use_case: Characteristics of the simulation problem

        Returns:
            Recommended workflow type

        Decision logic:
        1. Standard drug discovery → DOCKING_FIRST
        2. Membrane/nanoparticle systems → MD_FIRST
        3. Induced fit scenarios → ITERATIVE
        4. Edge cases → CUSTOM with guidance
        """
        # Decision tree implementation
        if self._is_standard_virtual_screening(use_case):
            workflow = WorkflowType.DOCKING_FIRST

        elif self._is_membrane_targeting(use_case):
            workflow = WorkflowType.MD_FIRST

        elif self._is_induced_fit(use_case):
            workflow = WorkflowType.ITERATIVE

        else:
            workflow = WorkflowType.CUSTOM

        # Log decision
        self._log_decision(use_case, workflow)

        return workflow

    def build_pipeline(
        self, workflow_type: WorkflowType, use_case: UseCaseCharacteristics
    ) -> dict[str, Any]:
        """Build execution pipeline for workflow type.

        Args:
            workflow_type: Type of workflow to build
            use_case: Use case characteristics for parameterization

        Returns:
            Pipeline configuration dictionary

        Pipeline structure:
        {
            'scale_sequence': ScaleSequence,
            'stages': [list of stage configurations],
            'bridges': [required bridge converters],
            'validation': [validation checks per stage],
            'estimated_time': time estimate,
            'estimated_cost': cost estimate
        }
        """
        if workflow_type == WorkflowType.DOCKING_FIRST:
            return self._build_docking_first_pipeline(use_case)

        elif workflow_type == WorkflowType.MD_FIRST:
            return self._build_md_first_pipeline(use_case)

        elif workflow_type == WorkflowType.ITERATIVE:
            return self._build_iterative_pipeline(use_case)

        else:
            return self._build_custom_pipeline(use_case)

    def _is_standard_virtual_screening(self, use_case: UseCaseCharacteristics) -> bool:
        """Check if use case matches standard virtual screening.

        Criteria:
        - Known receptor structure
        - Known binding site
        - Large compound library (>1000)
        - Soluble protein target
        - Standard screening goal
        """
        return (
            use_case.has_known_receptor_structure
            and use_case.has_known_binding_site
            and use_case.compound_library_size >= 1000
            and use_case.receptor_type == "soluble"
            and use_case.goal == "screening"
            and not use_case.is_membrane_system
            and not use_case.is_nanoparticle_delivery
        )

    def _is_membrane_targeting(self, use_case: UseCaseCharacteristics) -> bool:
        """Check if use case is membrane/nanoparticle targeting.

        Criteria:
        - Membrane-embedded system OR nanoparticle delivery
        - May not have clear binding site initially
        - Needs MD to understand membrane interactions
        """
        return (
            use_case.is_membrane_system
            or use_case.is_nanoparticle_delivery
            or (use_case.receptor_type == "membrane" and not use_case.has_known_binding_site)
        )

    def _is_induced_fit(self, use_case: UseCaseCharacteristics) -> bool:
        """Check if use case needs induced fit docking.

        Criteria:
        - Large conformational changes upon binding
        - Cryptic pocket that opens with ligand
        - Needs iterative MD-docking cycles
        """
        return use_case.needs_induced_fit or use_case.is_cryptic_pocket

    def _build_docking_first_pipeline(self, use_case: UseCaseCharacteristics) -> dict[str, Any]:
        """Build standard docking-first pipeline.

        Pipeline: Macro → Micro (Docking) → Meso (MD validation)

        Stages:
        1. OpenFOAM: Blood flow / transport (optional, if macro scale needed)
        2. AutoDock Vina: High-throughput docking
        3. Post-docking filtering: Score-based + clustering
        4. GROMACS: MD validation of top poses
        5. Analysis: Stability metrics
        """
        stages = []

        # Stage 1: Macro (optional)
        if use_case.is_nanoparticle_delivery:
            stages.append(
                {
                    "name": "macro_transport",
                    "tool": "openfoam",
                    "purpose": "Calculate nanoparticle distribution",
                    "estimated_time": "2-6 hours",
                }
            )

        # Stage 2: Docking
        stages.append(
            {
                "name": "molecular_docking",
                "tool": "autodock_vina",
                "purpose": "Screen compound library",
                "parameters": {
                    "exhaustiveness": self._get_docking_exhaustiveness(use_case),
                    "num_modes": 9,
                },
                "estimated_time": self._estimate_docking_time(use_case.compound_library_size),
            }
        )

        # Stage 3: Post-processing
        stages.append(
            {
                "name": "pose_selection",
                "tool": "internal",
                "purpose": "Select diverse poses for validation",
                "parameters": {
                    "top_n": self._get_validation_count(use_case),
                    "rmsd_cutoff": 2.0,
                },
                "estimated_time": "5-15 minutes",
            }
        )

        # Stage 4: MD validation
        stages.append(
            {
                "name": "md_validation",
                "tool": "gromacs",
                "purpose": "Validate binding stability",
                "parameters": {
                    "simulation_time": self._get_md_duration(use_case),
                    "replicas": 3,
                },
                "estimated_time": self._estimate_md_time(use_case),
            }
        )

        # Stage 5: Analysis
        stages.append(
            {
                "name": "stability_analysis",
                "tool": "internal",
                "purpose": "Calculate RMSD, H-bonds, binding energy",
                "estimated_time": "10-30 minutes",
            }
        )

        return {
            "scale_sequence": ScaleSequence.MACRO_MICRO_MESO
            if stages[0]["name"] == "macro_transport"
            else ScaleSequence.MICRO_MESO,
            "stages": stages,
            "bridges": ["MicroToMesoBridge"]
            if len(stages) <= 4
            else ["MacroToMesoBridge", "MicroToMesoBridge"],
            "validation": self._get_validation_checks("docking_first"),
            "estimated_total_time": self._sum_stage_times(stages),
            "estimated_cost": self._estimate_pipeline_cost(stages, use_case),
        }

    def _build_md_first_pipeline(self, use_case: UseCaseCharacteristics) -> dict[str, Any]:
        """Build MD-first pipeline for membrane systems.

        Pipeline: Macro → Meso (MD) → Micro (Docking) → Meso (MD validation)

        Stages:
        1. OpenFOAM: Nanoparticle transport
        2. GROMACS (CG): Coarse-grained membrane interaction
        3. Binding site identification
        4. AutoDock Vina: Ligand-receptor docking
        5. GROMACS (AA): Atomistic validation
        """
        stages = [
            {
                "name": "macro_transport",
                "tool": "openfoam",
                "purpose": "Nanoparticle distribution in vasculature",
                "estimated_time": "2-6 hours",
            },
            {
                "name": "membrane_md",
                "tool": "gromacs",
                "type": "coarse_grained",
                "purpose": "NP-membrane interaction and approach",
                "parameters": {"simulation_time": "1-5 microseconds"},
                "estimated_time": "6-24 hours",
            },
            {
                "name": "binding_site_detection",
                "tool": "internal",
                "purpose": "Identify exposed receptor binding sites",
                "estimated_time": "15-30 minutes",
            },
            {
                "name": "molecular_docking",
                "tool": "autodock_vina",
                "purpose": "Dock targeting ligands to receptors",
                "parameters": {"exhaustiveness": 16, "num_modes": 9},
                "estimated_time": "30 minutes - 2 hours",
            },
            {
                "name": "atomistic_validation",
                "tool": "gromacs",
                "type": "atomistic",
                "purpose": "Validate ligand-receptor binding in membrane context",
                "parameters": {"simulation_time": "50-100 ns"},
                "estimated_time": "12-48 hours",
            },
        ]

        return {
            "scale_sequence": ScaleSequence.MACRO_MESO_MICRO_MESO,
            "stages": stages,
            "bridges": ["MacroToMesoBridge", "MesoToMicroBridge", "MicroToMesoBridge"],
            "validation": self._get_validation_checks("md_first"),
            "estimated_total_time": self._sum_stage_times(stages),
            "estimated_cost": self._estimate_pipeline_cost(stages, use_case),
        }

    def _build_iterative_pipeline(self, use_case: UseCaseCharacteristics) -> dict[str, Any]:
        """Build iterative MD-docking pipeline for induced fit.

        Pipeline: Multiple cycles of MD → Docking → Scoring

        Not implemented in Phase 1.
        """
        raise NotImplementedError("Iterative workflow will be added in Phase 2")

    def _build_custom_pipeline(self, use_case: UseCaseCharacteristics) -> dict[str, Any]:
        """Provide guidance for custom workflow construction.

        Returns recommendations but requires user configuration.
        """
        return {
            "scale_sequence": ScaleSequence.MACRO_MICRO_MESO,  # Default suggestion
            "stages": [],
            "bridges": [],
            "validation": [],
            "message": "This use case requires custom workflow configuration. Please consult documentation or contact support.",
            "recommendations": self._generate_recommendations(use_case),
        }

    def _get_docking_exhaustiveness(self, use_case: UseCaseCharacteristics) -> int:
        """Determine Vina exhaustiveness parameter."""
        if use_case.compound_library_size > 10000:
            return 8  # Fast screening
        elif use_case.compound_library_size > 1000:
            return 16  # Balanced
        else:
            return 32  # Thorough

    def _get_validation_count(self, use_case: UseCaseCharacteristics) -> int:
        """Determine how many poses to validate with MD."""
        if use_case.compute_budget == "limited":
            return 3
        elif use_case.compute_budget == "moderate":
            return 5
        else:
            return 10

    def _get_md_duration(self, use_case: UseCaseCharacteristics) -> str:
        """Determine MD simulation duration."""
        if use_case.goal == "screening":
            return "10 ns"  # Quick validation
        elif use_case.goal == "validation":
            return "50 ns"  # Standard
        else:
            return "100 ns"  # Publication quality

    def _estimate_docking_time(self, library_size: int) -> str:
        """Estimate docking time."""
        compounds_per_hour = 1000  # Approximate
        hours = library_size / compounds_per_hour
        if hours < 1:
            return f"{int(hours * 60)} minutes"
        elif hours < 24:
            return f"{int(hours)} hours"
        else:
            return f"{int(hours / 24)} days"

    def _estimate_md_time(self, use_case: UseCaseCharacteristics) -> str:
        """Estimate MD time."""
        duration_map = {"10 ns": "2-6 hours", "50 ns": "12-24 hours", "100 ns": "1-2 days"}
        return duration_map.get(self._get_md_duration(use_case), "variable")

    def _sum_stage_times(self, stages: list[dict[str, Any]]) -> str:
        """Sum estimated times across stages."""
        # Simplified - just return range
        return "1-7 days (depending on parallelization)"

    def _estimate_pipeline_cost(
        self, stages: list[dict[str, Any]], use_case: UseCaseCharacteristics
    ) -> str:
        """Estimate computational cost."""
        if use_case.compute_budget == "limited":
            return "$50-$200"
        elif use_case.compute_budget == "moderate":
            return "$200-$1000"
        else:
            return "$1000-$5000"

    def _get_validation_checks(self, workflow_type: str) -> list[str]:
        """Get validation checks for workflow type."""
        common = ["mass_conservation", "energy_conservation", "structural_integrity"]
        if workflow_type == "docking_first":
            return common + ["binding_site_coverage", "pose_diversity", "rmsd_stability"]
        elif workflow_type == "md_first":
            return common + [
                "membrane_integrity",
                "binding_site_identification",
                "ligand_stability",
            ]
        return common

    def _generate_recommendations(self, use_case: UseCaseCharacteristics) -> list[str]:
        """Generate recommendations for custom workflows."""
        recommendations = []
        if not use_case.has_known_receptor_structure:
            recommendations.append("Use AlphaFold2 or homology modeling to generate structure")
        if not use_case.has_known_binding_site:
            recommendations.append("Run pocket detection (Fpocket, SiteMap) before docking")
        if use_case.compound_library_size > 100000:
            recommendations.append("Consider ligand-based filtering before structure-based docking")
        return recommendations

    def _log_decision(self, use_case: UseCaseCharacteristics, workflow: WorkflowType) -> None:
        """Log workflow decision for analysis."""
        self.decision_history.append({"use_case": use_case, "workflow": workflow.__dict__})
