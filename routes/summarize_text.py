from flask import Blueprint, request, jsonify
import openai
from config import OPENAI_API_KEY

summarize_text_bp = Blueprint('summarize_text', __name__)
openai.api_key = OPENAI_API_KEY

@summarize_text_bp.route('/', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text', '')
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=50
    )
    return jsonify(response.choices[0].text.strip())