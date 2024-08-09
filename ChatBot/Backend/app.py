import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, redirect


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'



def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    description = df.describe().to_html()

    # Plot
    plt.figure()
    df.hist(figsize=(15, 17))
    plot_path = 'static/plot.png'
    plt.savefig(plot_path)
    plt.close()

    return description, plot_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            description, plot_path = analyze_csv(file_path)
            return render_template('index.html', description=description, plot_path=plot_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
