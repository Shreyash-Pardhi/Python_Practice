import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import json
import datetime

# Sample data structure for documents and user interactions
documents = pd.DataFrame({
    'doc_id': [1, 2, 3],
    'title': ['Doc 1', 'Doc 2', 'Doc 3'],
    'content': ['Content of document 1', 'Content of document 2', 'Content of document 3'],
    'views': [150, 200, 50],
    'downloads': [100, 150, 30],
    'edits': [10, 20, 5],
    'feedback': ['Good', 'Average', 'Poor'],
    'ratings': [4.5, 3.0, 2.0],
    'last_accessed': ['2024-07-01', '2024-06-15', '2024-05-20']
})

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

# Function to calculate document access metrics
def document_access_metrics(documents):
    documents['total_interactions'] = documents[['views', 'downloads', 'edits']].sum(axis=1)
    most_accessed = documents.sort_values(by='total_interactions', ascending=False).head(1)
    least_accessed = documents.sort_values(by='total_interactions').head(1)
    return most_accessed, least_accessed

# Function to monitor user engagement
def user_engagement(user_interactions):
    user_activity = user_interactions.groupby('user_id').size()
    active_users = user_activity[user_activity > 1]
    inactive_users = user_activity[user_activity == 1]
    return active_users, inactive_users

# Function to perform trend analysis
def trend_analysis(documents):
    documents['last_accessed'] = pd.to_datetime(documents['last_accessed'])
    documents.set_index('last_accessed', inplace=True)
    trend = documents.resample('M').sum()
    return trend

# Function to collect and analyze feedback
def sentiment_analysis(feedback):
    from textblob import TextBlob
    feedback['sentiment'] = feedback['feedback'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return feedback

# Function to identify knowledge gaps
def search_query_analysis(search_queries):
    no_results = search_queries[search_queries['results'] == 0]
    return no_results

# Function to detect redundancy in documents
def redundancy_detection(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents['content'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Function to generate dashboard
def generate_dashboard(documents, user_interactions, search_queries):
    most_accessed, least_accessed = document_access_metrics(documents)
    active_users, inactive_users = user_engagement(user_interactions)
    trend = trend_analysis(documents)
    sentiment = sentiment_analysis(documents[['feedback']])
    gaps = search_query_analysis(search_queries)
    redundancy = redundancy_detection(documents)

    print("Most Accessed Document:\n", most_accessed)
    print("Least Accessed Document:\n", least_accessed)
    print("Active Users:\n", active_users)
    print("Inactive Users:\n", inactive_users)
    print("Trend Analysis:\n", trend)
    print("Sentiment Analysis:\n", sentiment)
    print("Knowledge Gaps:\n", gaps)
    print("Document Redundancy:\n", redundancy)

# Function to export data
def export_data(data, format='csv'):
    if format == 'csv':
        data.to_csv('exported_data.csv', index=False)
    elif format == 'excel':
        data.to_excel('exported_data.xlsx', index=False)
    elif format == 'json':
        data.to_json('exported_data.json')
    else:
        print("Unsupported format")

# Main function
if __name__ == "__main__":
    generate_dashboard(documents, user_interactions, search_queries)
    export_data(documents, format='csv')
