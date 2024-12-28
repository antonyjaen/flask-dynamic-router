"""Parameter parsing utilities for dynamic routes."""
import re
from typing import Tuple

def parse_dynamic_param(directory_name: str) -> Tuple[bool, str]:
    """
    Parse a directory name to check if it contains a dynamic parameter.
    
    Args:
        directory_name: Name of the directory
        
    Returns:
        Tuple of (is_dynamic, parameter_name)
    """
    param_pattern = r'\[(.*?)\]'
    match = re.search(param_pattern, directory_name)
    
    if match:
        param_name = match.group(1)
        # Convert camelCase or PascalCase to snake_case
        param_name = re.sub(r'(?<!^)(?=[A-Z])', '_', param_name).lower()
        return True, param_name
    
    return False, directory_name