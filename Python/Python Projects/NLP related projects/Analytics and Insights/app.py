from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
import numpy as np
from process_files import process_files, generate_dashboard, export_data
from werkzeug.utils import secure_filename
import time
import math
import json
import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'csv', 'xlsx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_metadata(file):
    file_info = file.stream
    size = convert_size(file_info.seek(0, os.SEEK_END))
    file_info.seek(0, os.SEEK_SET)
    return size, file_info

def convert_size(size):
    if size == 0:
        return '0B'
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return '%s %s' % (s, size_name[i])

def format_time(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return redirect(request.url)
    files = request.files.getlist('files[]')
    file_paths = []
    original_metadata = []

    for file in files:
        if file and allowed_file(file.filename):
            # Fetch original metadata
            size, file_info = get_file_metadata(file)
            original_metadata.append({
                'filename': secure_filename(file.filename),
                'size': size,
                'created': format_time(file_info.stat().st_birthtime),  # Placeholder for original created time
                'modified': format_time(file_info.stat().st_mtime),  # Placeholder for original modified time
                'accessed': format_time(file_info.stat().st_atime)   # Placeholder for original accessed time
            })

            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filename)
            file_paths.append(filename)

    return redirect(url_for('dashboard', file_paths=','.join(file_paths), metadata=json.dumps(original_metadata)))

@app.route('/dashboard')
def dashboard():
    file_paths = request.args.get('file_paths').split(',')
    original_metadata = json.loads(request.args.get('metadata'))

    documents = process_files(file_paths, original_metadata)

    user_interactions = pd.DataFrame({
        'user_id': [1, 2, 1],
        'doc_id': [1, 2, 3],
        'time_spent': [30, 45, 10],
        'activity': ['view', 'download', 'edit']
    })

    search_queries = pd.DataFrame({
        'query': ['document management', 'analytics', 'reporting'],
        'results': [10, 5, 0]
    })

    dashboard_data = generate_dashboard(documents, user_interactions, search_queries)

    # Limit content column to 2 lines and add ellipses if it exceeds
    max_content_length = 500  # Adjust as needed
    documents['content_preview'] = documents['content'].apply(lambda x: (x[:max_content_length] + '...') if len(x) > max_content_length else x)

    # Convert DataFrames to HTML
    dashboard_data_html = {key: value.to_html(classes='table table-striped') if isinstance(value, pd.DataFrame) else value for key, value in dashboard_data.items()}
    
    return render_template('dashboard.html', data=dashboard_data_html)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
