from flask import Flask, request, render_template, jsonify
import pytesseract
from PIL import Image
import sqlite3
import openai
import os

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('prescriptions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prescriptions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')
    conn.commit()
    conn.close()

init_db()


def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def validate_prescription(text):
    openai.api_key = "your-openai-api-key" 
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Validate and correct medicine names in the given prescription."},
                  {"role": "user", "content": text}]
    )
    return response['choices'][0]['message']['content'].strip()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    filepath = os.path.join('data', file.filename)
    file.save(filepath)
    extracted_text = extract_text(filepath)
    validated_text = validate_prescription(extracted_text)
    
 
    conn = sqlite3.connect('prescriptions.db')
    c = conn.cursor()
    c.execute("INSERT INTO prescriptions (text) VALUES (?)", (validated_text,))
    conn.commit()
    conn.close()
    
    return jsonify({'extracted_text': extracted_text, 'validated_text': validated_text})

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)  
    app.run(debug=True)
