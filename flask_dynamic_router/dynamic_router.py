"""Main module for Flask Dynamic Router."""
from pathlib import Path
from typing import Optional, Union
from flask import Flask

from .route_registrar import RouteRegistrar
from .directory_processor import DirectoryProcessor

class DynamicRouter:
    """
    A class to handle dynamic route registration in Flask applications.
    """
    
    def __init__(self, app: Optional[Flask] = None):
        """
        Initialize the DynamicRouter extension.
        
        Args:
            app: Optional Flask application instance
        """
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """
        Initialize the extension with the Flask application.
        
        Args:
            app: Flask application instance
        """
        self.app = app
        # Set default configuration
        app.config.setdefault('DYNAMIC_ROUTER_CASE_SENSITIVE', True)
        app.config.setdefault('DYNAMIC_ROUTER_URL_PREFIX', '')
        
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['dynamic_router'] = self
        
        self.route_registrar = RouteRegistrar(app)
        self.directory_processor = DirectoryProcessor(self.route_registrar)

    def register_routes(self, routes_path: Union[str, Path]) -> None:
        """
        Register routes from the specified directory.
        
        Args:
            routes_path: Path to the routes directory
        """
        if isinstance(routes_path, str):
            routes_path = Path(routes_path)

        if not routes_path.exists():
            raise FileNotFoundError(f"Routes directory not found: {routes_path}")

        self.directory_processor.process_directory(routes_path)