from flask import Flask
from src.api.endpoints import initialize_routes

# Initialize Flask app
app = Flask(__name__)

# Initialize API Routes
initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
