import os
import pandas as pd
import numpy as np
import datetime
import fitz  # PyMuPDF
from docx import Document
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import datetime
import math

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_excel(file_path):
    return pd.read_excel(file_path)

def read_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def process_files(file_paths, metadata):
    documents = []
    for file_path, meta in zip(file_paths, metadata):
        if file_path.endswith('.pdf'):
            content = extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            content = extract_text_from_docx(file_path)
        elif file_path.endswith('.csv'):
            content = read_csv(file_path).to_string()
        elif file_path.endswith('.xlsx'):
            content = read_excel(file_path).to_string()
        elif file_path.endswith('.txt'):
            content = read_txt(file_path)
        else:
            print(f"Unsupported file type: {file_path}")
            continue

        documents.append({
            'file_path': meta['filename'],
            'content': content,
            'size': meta['size'],
            'views': np.random.randint(0, 100),  # Simulated data
            'downloads': np.random.randint(0, 100),  # Simulated data
            'edits': np.random.randint(0, 10),  # Simulated data
            "created": meta['created'],
            "modified": meta['modified'],
            "accessed": meta['accessed'],
            'last_accessed': datetime.datetime.now() - pd.to_timedelta(np.random.randint(0, 365), unit='d')
        })
    return pd.DataFrame(documents)

def document_access_metrics(documents):
    documents['total_interactions'] = documents[['views', 'downloads', 'edits']].sum(axis=1)
    documents = documents.drop('content', axis=1)
    most_accessed = documents.sort_values(by='total_interactions', ascending=False).head(1)
    least_accessed = documents.sort_values(by='total_interactions').head(1)
    return most_accessed, least_accessed

def trend_analysis(documents):
    documents['last_accessed'] = pd.to_datetime(documents['last_accessed'])
    documents = documents.drop('content', axis=1)
    trend = documents.groupby(pd.Grouper(key='last_accessed', freq='M')).sum()
    trend = trend[(trend.T != 0).any()]
    trend = trend.sort_values(by='total_interactions', ascending=False)
    return trend

def search_query_analysis(search_queries):
    no_results = search_queries[search_queries['results'] == 0]
    return no_results

def redundancy_detection(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents['content'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    suggetion = 'NA'
    num_docs = len(documents)
    for i in range(num_docs):
        for j in range(num_docs):
            if i != j and cosine_sim[i, j] > 0.95:
                suggetion = f"Documents '{documents.iloc[i]['file_path']}' and '{documents.iloc[j]['file_path']}' contain similar content."
                
    return cosine_sim, suggetion

def generate_dashboard(documents, user_interactions, search_queries):
    most_accessed, least_accessed = document_access_metrics(documents)
    trend = trend_analysis(documents)
    gaps = search_query_analysis(search_queries)
    redundancy, sug = redundancy_detection(documents)

    dashboard_data = {
        'most_accessed': most_accessed,
        'least_accessed': least_accessed,
        'trend': trend,
        'gaps': gaps,
        'redundancy': redundancy,
        'suggestion': sug
    }

    plt.figure(figsize=(12, 6))
    sns.barplot(x=documents['file_path'], y=documents['total_interactions'])
    plt.title('Document Access Metrics: Total Interactions')
    plt.xlabel('Document')
    plt.ylabel('Total Interactions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/doc_interactions.png')
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.countplot(x=user_interactions['user_id'])
    plt.title('User Engagement: Number of Interactions')
    plt.xlabel('User ID')
    plt.ylabel('Number of Interactions')
    plt.tight_layout()
    plt.savefig('static/images/user_engagement.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=trend.index, y=trend['total_interactions'])
    plt.title('Trend Analysis: Document Interactions over Time')
    plt.xlabel('Time')
    plt.ylabel('Total Interactions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/trend_analysis.png')
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.barplot(x='query', y='results', data=search_queries)
    plt.title('Knowledge Gaps: Search Queries with No Results')
    plt.xlabel('Search Query')
    plt.ylabel('Number of Results')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/knowledge_gaps.png')
    plt.close()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(redundancy, annot=True, fmt='.2f', cmap='coolwarm', xticklabels=documents['file_path'], yticklabels=documents['file_path'])
    plt.title('Redundancy Heatmap: Document Similarity')
    plt.xlabel('Document')
    plt.ylabel('Document')
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/redundancy_heatmap.png')
    plt.close()
    
    return dashboard_data

def export_data(data, format='json'):
    if format == 'csv':
        data.to_csv('exported_data.csv', index=False)
    elif format == 'excel':
        data.to_excel('exported_data.xlsx', index=False)
    elif format == 'json':
        data.to_json('exported_data.json')
    else:
        print("Unsupported format")
