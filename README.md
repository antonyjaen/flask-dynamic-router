# Flask Dynamic Router

Flask extension that provides automatic and dynamic route registration for Flask applications, inspired by Next.js's file-system based routing..

## Installation

```bash
pip install flask-dynamic-router
```

## How to Use

### Basic Setup

```python
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
```

### Route Examples

1. **Basic Route** (`routes/root/__init__.py`):
```python
from flask import Blueprint

main = Blueprint('root', __name__)

@main.route('/')
def index():
    return {'message': 'Welcome to the API'}
```

2. **Dynamic Parameter** (`routes/users/[user_id]/__init__.py`):
```python
from flask import Blueprint

main = Blueprint('user_detail', __name__)

@main.route('/')
def get_user(user_id):
    return {'message': f'User details for ID: {user_id}'}
```

3. **Nested Routes** (`routes/products/[productID]/reviews/__init__.py`):
```python
from flask import Blueprint

main = Blueprint('product_reviews', __name__)

@main.route('/')
def get_reviews(product_id):
    return {'message': f'Reviews for product ID: {product_id}'}
```

### Configuration Options

```python
# Make routes case-insensitive
app.config['DYNAMIC_ROUTER_CASE_SENSITIVE'] = False

# Add a global prefix to all routes
app.config['DYNAMIC_ROUTER_URL_PREFIX'] = '/api/v1'
```

## Directory Structure

The router follows a convention-based approach where your directory structure maps directly to URL routes:

```
📦 routes
├── 📂 root
│   ├── 📄 __init__.py          ➜  🌐 /
│   ├── 📂 version
│   │   └── 📄 __init__.py      ➜  🌐 /version
│   └── 📂 about
│       └── 📄 __init__.py      ➜  🌐 /about
│
├── 📂 users
│   ├── 📄 __init__.py          ➜  🌐 /users
│   ├── 📂 [user_id]             ➜  💫 Dynamic Parameter
│   │   ├── 📄 __init__.py      ➜  🌐 /users/<user_id>
│   │   └── 📂 profile
│   │       └── 📄 __init__.py  ➜  🌐 /users/<user_id>/profile
│   └── 📂 settings
│       └── 📄 __init__.py      ➜  🌐 /users/settings
│
└── 📂 products
    ├── 📄 __init__.py          ➜  🌐 /products
    └── 📂 [product_id]          ➜  💫 Dynamic Parameter
        └── 📄 __init__.py      ➜  🌐 /products/<product_id>
```

## Route Mapping Examples

| Directory Structure | Generated Route | Type |
|--------------------|-----------------|------|
| `root/__init__.py` | `/` | Static Route |
| `user/__init__.py` | `/users` | Static Route |
| `user/[userID]/__init__.py` | `/users/<user_id>` | Dynamic Route |
| `product/[productID]/__init__.py` | `/products/<product_id>` | Dynamic Route |

## Dynamic Parameters

Dynamic parameters are defined using square brackets in directory names:
- 📂 `[userID]` ➜ `<user_id>`
- 📂 `[productID]` ➜ `<product_id>`
- 📂 `[categoryName]` ➜ `<category_name>`

## License

This project is licensed under the MIT License - see the LICENSE file for details.