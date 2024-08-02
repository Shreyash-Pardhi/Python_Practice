import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def generate_usage_report():
    conn = sqlite3.connect('document_usage.db')
    df = pd.read_sql_query("SELECT * FROM access_logs", conn)
    conn.close()
    
    usage_summary = df.groupby(['document_id', 'action']).size().reset_index(name='count')
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    time_series = df.set_index('timestamp').groupby('document_id').resample('D').size().unstack().fillna(0)
    
    time_series.plot(figsize=(10, 6))
    plt.title('Document Usage Over Time')
    plt.xlabel('Time')
    plt.ylabel('Usage Count')
    plt.legend(title='Document ID')
    plt.show()
