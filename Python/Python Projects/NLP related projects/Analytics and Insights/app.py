from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from process_files import process_files, generate_dashboard
import math
import json
import datetime
from pathlib import Path

app = Flask(__name__)
UPLOAD_FOLDER = 'D:\\Work and Assignments\\Python\\Assignments\\PDF Chapter Seperator\\'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'csv', 'xlsx', 'txt', 'py', 'json'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    # print(files)
    file_paths = []
    original_metadata = []

    for file in files:
        if file and allowed_file(file.filename):
            # Save the file temporarily to fetch metadata
            # filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            print(file_path)
            # file.save(file_path)

            # Fetch original metadata
            file_info = Path(file_path)
            original_metadata.append({
                'filename': file_info.name,
                'size': convert_size(file_info.stat().st_size),
                'created': format_time(file_info.stat().st_birthtime),  # Creation time
                'modified': format_time(file_info.stat().st_mtime),  # Modified time
                'accessed': format_time(file_info.stat().st_atime)   # Accessed time
            })

            file_paths.append(file_path)

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
        'results': [10, 0, 0]
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
