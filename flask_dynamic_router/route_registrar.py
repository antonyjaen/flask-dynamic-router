"""Module for handling route registration logic."""
from pathlib import Path
from flask import Flask, Blueprint
import importlib.util

class RouteRegistrar:
    """Handles the registration of routes and blueprints."""
    
    def __init__(self, app: Flask):
        self.app = app
        
    def register_blueprint(self, file_path: Path, url_prefix: str) -> None:
        """
        Register a blueprint from a route file.
        
        Args:
            file_path: Path to the route file
            url_prefix: URL prefix for the blueprint
        """
        module_name = file_path.parent.name
        
        # Import the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None or spec.loader is None:
            return
            
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Check for Blueprint instance
        if hasattr(module, 'main') and isinstance(module.main, Blueprint):
            if not self.app.config['DYNAMIC_ROUTER_CASE_SENSITIVE']:
                url_prefix = url_prefix.lower()
                
            full_prefix = f"{self.app.config['DYNAMIC_ROUTER_URL_PREFIX']}/{url_prefix}".rstrip('/')
            self.app.register_blueprint(module.main, url_prefix=full_prefix)