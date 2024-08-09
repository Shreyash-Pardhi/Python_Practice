import os
import pandas as pd
import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# from flask import Flask, request, render_template, redirect, url_for
from openai import OpenAI
from api_key import key
from DB import get_employee_data

client = OpenAI(api_key=key)


def analyze_csv():
    df = get_employee_data()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert data analyst with experience in data visualization."},
            {"role": "user", "content": f"Please analyze the following data sample and suggest appropriate types of graphs(only bar, pie and histogram) for each column. Here's a preview of the data:\n{df.head().to_string()}\n\nProvide your suggestions in JSON format with the following structure: `{{\"plot_name\": \"graph_type\", \"column_names\": [\"column1\", \"column2\"]}}`. Include a graph type and the relevant column names for each suggested graph.(do not give anything other than this)"},
        ],
    )
    ai_response = response.choices[0].message.content.strip()
    return ai_response


print(analyze_csv())
