# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 12:14:08 2025

@author: win
"""
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route for the root URL
@app.route('/')
def home():
    return "Welcome to the Logistics Project Site! Use the /upload endpoint to upload files."

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