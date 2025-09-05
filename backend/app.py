import os
from flask import Flask, render_template

# Get the base directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set template and static directories correctly
TEMPLATE_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'templates'))
STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'static'))

# Initialize Flask app
app = Flask(__name__, 
            template_folder=TEMPLATE_DIR, 
            static_folder=STATIC_DIR)

# Simple test route
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

@app.route('/test')
def test():
    return "Test route is working!"

if __name__ == '__main__':
    port = 10000
    print(f"Template directory: {TEMPLATE_DIR}")
    print(f"Static directory: {STATIC_DIR}")
    print(f"Templates exist: {os.path.exists(TEMPLATE_DIR)}")
    if os.path.exists(TEMPLATE_DIR):
        print(f"Templates found: {os.listdir(TEMPLATE_DIR)}")
    
    app.run(host='0.0.0.0', port=port, debug=True)