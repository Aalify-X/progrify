import os
from flask import Flask, session, redirect, url_for, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables
load_dotenv()

# Set template and static directories
TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/templates'))
STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/static'))

# Initialize Flask app
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Configuration
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'NSjUyKL1$8N*@(i')
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
app.config['PORT'] = int(os.getenv('PORT', 10000))
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)

# CORS Configuration
CORS(app)

# Error handling
@app.errorhandler(403)
def forbidden_error(e):
    return render_template('error.html',
                         error_code=403,
                         error_message="Access Forbidden"), 403

@app.errorhandler(404)
def not_found_error(e):
    return render_template('error.html',
                         error_code=404,
                         error_message="Page not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html',
                         error_code=500,
                         error_message="Internal server error"), 500

# Application routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/digital_planner')
def digital_planner():
    return render_template('digital_planner.html')

@app.route('/whiteboard')
def whiteboard():
    return render_template('whiteboard.html')

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')

@app.route('/pdf_tools')
def pdf_tools():
    return render_template('pdf_document_intelligence.html')

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

# Run app
if __name__ == '__main__':
    port = int(app.config.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
