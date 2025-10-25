"""Input validation utilities."""
from pathlib import Path
from typing import Any

import yaml


def validate_config_file(config_path: Path) -> dict[str, Any]:
    """Validate and load configuration file.

    Args:
        config_path: Path to YAML configuration file

    Returns:
        Parsed configuration dictionary

    Raises:
        FileNotFoundError: If config file doesn't exist
        yaml.YAMLError: If YAML parsing fails
        ValueError: If configuration is invalid
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path) as f:
        config = yaml.safe_load(f)

    # Validate required fields
    required_fields = ["project", "scales"]
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field in config: {field}")

    return config


def validate_scales(scales: list[str]) -> None:
    """Validate scale names.

    Args:
        scales: List of scale names

    Raises:
        ValueError: If any scale name is invalid
    """
    valid_scales = {"macro", "meso", "micro"}
    invalid = set(scales) - valid_scales

    if invalid:
        raise ValueError(f"Invalid scale names: {invalid}. Must be one of {valid_scales}")


def validate_parameters(parameters: dict[str, Any], required: list[str]) -> None:
    """Validate that required parameters are present.

    Args:
        parameters: Parameter dictionary
        required: List of required parameter names

    Raises:
        ValueError: If any required parameter is missing
    """
    missing = set(required) - set(parameters.keys())

    if missing:
        raise ValueError(f"Missing required parameters: {missing}")
