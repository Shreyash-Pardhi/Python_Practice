from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

def find_redundant_documents(documents):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)
    
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(X)
    
    similarity_matrix = cosine_similarity(X)
    redundancies = identify_redundancies(similarity_matrix)
    
    return redundancies

def identify_redundancies(similarity_matrix):
    threshold = 0.8
    redundant_pairs = []
    for i in range(len(similarity_matrix)):
        for j in range(i+1, len(similarity_matrix)):
            if similarity_matrix[i][j] > threshold:
                redundant_pairs.append((i, j))
    return redundant_pairs
