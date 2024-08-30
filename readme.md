pip install -r requirements.txt
set FLASK_APP=app.py
flask run

OR

pip install -r requirements.txt
python app.py

http://127.0.0.1:5000/

text payload
url - routes/generate_text.py

{
  "prompt": "A futuristic cityscape at sunset",
  "text": "This is a sample text to summarize.",
  "json_data": {
    "key1": "value1",
    "key2": "value2"
  }
}

url - routes/generate_image.py

url - routes/summarize_text.py

url - routes/analyze_json.py

# Generate Text
curl -X POST http://127.0.0.1:5000/generate_text -H "Content-Type: application/json" -d '{"prompt": "Write a poem about the sea."}'

# Generate Image
curl -X POST http://127.0.0.1:5000/generate_image -H "Content-Type: application/json" -d '{"prompt": "A futuristic cityscape at sunset"}'

# Summarize Text
curl -X POST http://127.0.0.1:5000/summarize_text -H "Content-Type: application/json" -d '{"text": "This is a sample text to summarize."}'

# Analyze JSON
curl -X POST http://127.0.0.1:5000/analyze_json -H "Content-Type: application/json" -d '{"json_data": {"key1": "value1", "key2": "value2"}}'

