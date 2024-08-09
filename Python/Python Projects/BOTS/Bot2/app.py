from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio
import pandas as pd
from DB import get_employee_data

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch employee data
    df = get_employee_data()

    # 1. Salary Distribution Histogram
    scatter_fig = px.histogram(df, x='salary', nbins=10, title="Salary Distribution")
    scatter_html = pio.to_html(scatter_fig, full_html=False)
    
    # 2. Average Salary by Department (Bar Graph)
    avg_salary_by_dept = df.groupby('work_dept')['salary'].mean().reset_index()
    bar_fig = px.bar(avg_salary_by_dept, x='work_dept', y='salary', color='work_dept',
                     title="Average Salary by Department",
                     labels={'salary': 'Average Salary'})
    bar_html = pio.to_html(bar_fig, full_html=False)
    
    # 3. Gender Distribution Pie Chart
    gender_counts = df['gender'].value_counts().reset_index()
    gender_counts.columns = ['gender', 'count']
    pie_fig = px.pie(gender_counts, names='gender', values='count', title="Gender Distribution")
    pie_html = pio.to_html(pie_fig, full_html=False)

    return render_template('index.html', scatter_html=scatter_html, pie_html=pie_html, bar_html=bar_html)

if __name__ == '__main__':
    app.run(debug=True)
