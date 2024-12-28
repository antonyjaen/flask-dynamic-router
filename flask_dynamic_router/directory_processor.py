"""Module for processing directory structures."""
import os
from pathlib import Path
from typing import Optional
from .utils.param_parser import parse_dynamic_param
from .route_registrar import RouteRegistrar

class DirectoryProcessor:
    """Processes directory structures to register routes."""
    
    def __init__(self, registrar: RouteRegistrar):
        self.registrar = registrar
        
    def process_directory(self, directory: Path, parent_path: str = '') -> None:
        """
        Process a directory recursively to register routes.
        
        Args:
            directory: Directory path to process
            parent_path: Parent URL path
        """
        for item in directory.iterdir():
            if item.is_file() and item.name == '__init__.py':
                self.registrar.register_blueprint(item, parent_path)
            elif item.is_dir() and not item.name.startswith('__'):
                is_dynamic, param_name = parse_dynamic_param(item.name)
                if is_dynamic:
                    new_parent = os.path.join(parent_path, f'<{param_name}>').replace('\\', '/')
                else:
                    new_parent = os.path.join(parent_path, item.name).replace('\\', '/')
                self.process_directory(item, new_parent)