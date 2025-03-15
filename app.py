# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 12:14:08 2025

@author: win
"""
from flask import Flask, request, jsonify, render_template  # Add render_template
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route for the root URL
@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html file from the templates folder

# Route for file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file to the upload folder
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # Disable reloader for Spyder
