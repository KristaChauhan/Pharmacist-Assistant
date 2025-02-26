# Pharmacist Assistant

## Overview
An AI-powered application that reads handwritten prescriptions, extracts medicine names using OCR, and validates them against a database.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pharmacist-assistant.git
   cd pharmacist-assistant
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Project
1. Start the backend:
   ```sh
   python app.py
   ```
2. Open `index.html` in a browser.

## Dependencies
- Flask
- pytesseract
- openai
- pillow
- sqlite3

## How AI is Used
- OCR (Optical Character Recognition) extracts text from images.
- AI model validates medicine names.

## Example Usage
1. Upload a prescription image.
2. The system extracts and validates medicine names.
3. The validated prescription is displayed.

