import re
import pdfplumber
from docx import Document
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models

nltk.download('stopwords')

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to extract text from DOCX files
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to read CSV files
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

# Function to perform topic modeling
def topic_modeling(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    topics = lda.print_topics(num_words=4)
    return topics

# Function to visualize topics
def visualize_topics(topics):
    for i, topic in enumerate(topics):
        print(f"Topic {i+1}: {topic}")

# Function to plot usage trends
def plot_usage_trends(usage_data):
    usage_data['date'] = pd.to_datetime(usage_data['date'])
    usage_data.set_index('date', inplace=True)
    usage_data.resample('M').sum().plot()
    plt.title('Document Usage Trends')
    plt.xlabel('Date')
    plt.ylabel('Usage Count')
    plt.show()

# Main function to analyze document
def analyze_document(file_path, file_type, usage_data=None):
    if file_type == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif file_type == 'docx':
        text = extract_text_from_docx(file_path)
    elif file_type == 'csv':
        data = read_csv_file(file_path)
        text = data.to_string()
    else:
        raise ValueError("Unsupported file type")

    preprocessed_text = preprocess_text(text)
    topics = topic_modeling([preprocessed_text])
    visualize_topics(topics)

    if usage_data is not None:
        plot_usage_trends(usage_data)

# Example usage
if __name__ == "__main__":
    # Analyze a PDF document
    analyze_document('D:\\Work and Assignments\\Python\\Python Projects\\NLP related projects\\Chapter1.pdf', 'pdf')

    # Analyze a DOCX document
    analyze_document('D:\\Work and Assignments\\Python\\Python Projects\\NLP related projects\\new.docx', 'docx')

    # Analyze a CSV document and plot usage trends
    usage_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
        'usage_count': [10, 15, 10, 5]
    })
    analyze_document('D:\\Work and Assignments\\Python\\Python Projects\\NLP related projects\\demo.csv', 'csv', usage_data)
