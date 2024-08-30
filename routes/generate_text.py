from flask import Blueprint, request, jsonify
import openai
from config import OPENAI_API_KEY

generate_text_bp = Blueprint('generate_text', __name__)
openai.api_key = OPENAI_API_KEY

@generate_text_bp.route('/', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())