from flask import Blueprint, request, jsonify
import openai
from config import OPENAI_API_KEY
from PIL import Image
import io
import base64

generate_image_bp = Blueprint('generate_image', __name__)
openai.api_key = OPENAI_API_KEY

@generate_image_bp.route('/', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt', '')
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1920x1080"  # Updated to Full HD dimensions
    )
    image_data = response['data'][0]['image']
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    image.save('generated_image.png')
    return jsonify({"message": "Image saved as 'generated_image.png'"})