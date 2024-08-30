from flask import Flask
from routes.generate_text import generate_text_bp
from routes.generate_image import generate_image_bp
from routes.summarize_text import summarize_text_bp
from routes.analyze_json import analyze_json_bp  # Import the new route

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(generate_text_bp, url_prefix='/generate_text')
app.register_blueprint(generate_image_bp, url_prefix='/generate_image')
app.register_blueprint(summarize_text_bp, url_prefix='/summarize_text')
app.register_blueprint(analyze_json_bp, url_prefix='/analyze_json')  

if __name__ == '__main__':
    app.run(debug=True)