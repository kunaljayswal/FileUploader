# Standard Library Imports
import json

# Third-Party Imports
from flask import Blueprint, request
from sqlalchemy.orm import sessionmaker
import asyncio

# Custom modules
from app.models.fileDbModel import File
from service.errorHandler import error_handler
from service.response import response
from utils.s3Uploader import upload_to_s3
from utils.virusTotalScanner import start_scan
from datetime import datetime
from utils.dbManager import db_manager

# * Defining Blueprint for API Routes
file_module = Blueprint("file_module", __name__)

# * Defining API Route for Create User API
@file_module.route("/", methods=["POST"], endpoint="upload-file")
@error_handler
def upload_file_main():
    try:
        # Checking if 'file' key exists in request.files
        if 'file' not in request.files:
            return response(400, {"error": "No file part in the request"})

        # Accessing the file object from request.files
        file_obj = request.files['file']

        # Checking if the file object is not empty
        if file_obj.filename == '':
            return response(400, {"error": "No selected file"})

        # Accessing file details
        filename = file_obj.filename

        print(filename)
        user_details = request.form.get("uploadedby")
        print(user_details)
        # Save file metadata to PostgreSQL
        Session = sessionmaker(bind=db_manager.engine)
        
        s3_URL = upload_to_s3(file_obj, filename)

        print(s3_URL)

        virus_scan_result = asyncio.run(start_scan(s3_URL))

        print(virus_scan_result, "virsus_scan_result")

        virus_scan_result = False

        session = Session()

        file_metadata = {
            "filename": filename,
            "uploadtime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "virusscanresult": virus_scan_result,
            "userdetails": user_details
        }

        session.add(File(**file_metadata))
        session.commit()
        session.close()

        body = {
            "file_metadata": file_metadata,
            "s3_URL": s3_URL,
            "msg": "Uploaded file and metadata successfully.",
        }

        return response(201, body)
    
    except Exception as e:
        return response(500, {"error": str(e)})