"""Test cases for Flask Dynamic Router."""
import pytest
from flask import Flask
from flask_dynamic_router import DynamicRouter
from pathlib import Path

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_init_app(app):
    router = DynamicRouter(app)
    assert 'dynamic_router' in app.extensions

def test_default_config(app):
    router = DynamicRouter(app)
    assert app.config['DYNAMIC_ROUTER_CASE_SENSITIVE'] is True
    assert app.config['DYNAMIC_ROUTER_URL_PREFIX'] == ''

def test_invalid_routes_path(app):
    router = DynamicRouter(app)
    with pytest.raises(FileNotFoundError):
        router.register_routes('nonexistent_path')