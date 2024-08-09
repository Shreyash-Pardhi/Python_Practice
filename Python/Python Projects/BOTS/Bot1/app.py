import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, redirect, url_for
from openai import OpenAI
from api_key import key

client = OpenAI(api_key=key)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    description = df.describe().to_html()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Analyze the following data:"},
            {"role": "user", "content": df.head().to_string()}
        ],
    )
    ai_response = response.choices[0].message.content.strip()

    num_columns = len(df.columns)
    possible_plots = []
    if num_columns >= 2:
        possible_plots.append('scatter')
        possible_plots.append('line')
    if num_columns >= 3:
        possible_plots.append('bar')
    if 'date' in df.dtypes.values:
        possible_plots.append('time_series')

    return description, ai_response, possible_plots

def generate_plot(file_path, plot_type):
    df = pd.read_csv(file_path)

    if plot_type == 'scatter' and len(df.columns) >= 2:
        plt.figure()
        plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
        plt.title('Scatter Plot')
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
    elif plot_type == 'line' and len(df.columns) >= 2:
        plt.figure()
        plt.plot(df.iloc[:, 0], df.iloc[:, 1])
        plt.title('Line Plot')
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
    elif plot_type == 'bar' and len(df.columns) >= 3:
        plt.figure()
        plt.bar(df.iloc[:, 0], df.iloc[:, 1])
        plt.title('Bar Plot')
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
    elif plot_type == 'time_series' and 'date' in df.dtypes.values:
        df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])
        df = df.set_index(df.columns[0])
        plt.figure()
        plt.plot(df.index, df.iloc[:, 1])
        plt.title('Time Series Plot')
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])

    plot_path = os.path.join(app.config['UPLOAD_FOLDER'], f'plot_{plot_type}.png')
    plt.savefig(plot_path)
    plt.close()

    return plot_path

@app.route('/', methods=['GET', 'POST'])
def index():
    description = None
    ai_response = None
    plots = []

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            description, ai_response, possible_plots = analyze_csv(file_path)

            for plot_type in possible_plots:
                plot_path = generate_plot(file_path, plot_type)
                plots.append((plot_type, os.path.basename(plot_path)))

            return render_template('index.html', description=description, ai_response=ai_response, plots=plots)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)