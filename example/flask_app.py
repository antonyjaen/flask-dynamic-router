from flask import Flask
from flask_dynamic_router import DynamicRouter

# Create Flask app
app = Flask(__name__)

# Initialize the router
router = DynamicRouter(app)

# Register routes from a directory
router.register_routes('routes')

if __name__ == '__main__':
    app.run()