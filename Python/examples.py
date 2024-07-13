import os
from google.cloud import vision
import pandas as pd
import concurrent.futures
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\storage_key.json"

# def get_image_labels(image_path):
#     """Get labels detected in an image using Google Vision API."""
#     client = vision.ImageAnnotatorClient()
#     img = vision.Image()
#     img.source.image_uri = image_path
    
#     response = client.label_detection(image=img)
#     labels = response.label_annotations
    
#     return [label.description for label in labels]

# def vectorize_labels(labels_list):
#     """Convert list of labels into vectors using CountVectorizer."""
#     vectorizer = CountVectorizer()
#     label_vectors = vectorizer.fit_transform(labels_list)
#     return label_vectors

# def compare_images(base_image_path, image_dict):
#     """Compare a base image with a dictionary of images using cosine similarity."""
#     base_labels = get_image_labels(base_image_path)
#     labels_list = [base_labels] + [get_image_labels(image_path) for image_path in image_dict.values()]
    
#     # Convert labels to strings for vectorization
#     labels_list_str = [" ".join(labels) for labels in labels_list]
    
#     # Vectorize labels
#     label_vectors = vectorize_labels(labels_list_str)
    
#     # Calculate cosine similarity
#     similarity_scores = cosine_similarity(label_vectors[0:1], label_vectors[1:]).flatten()
    
#     # Pair scores with image names and paths
#     scores = [(pname, image_path, score) for pname, image_path, score in zip(image_dict.keys(), image_dict.values(), similarity_scores)]
    
#     # Sort images by similarity score in descending order
#     scores.sort(key=lambda x: x[2], reverse=True)
    
#     # Print similarity scores
#     for pname, image_path, score in scores:
#         print(f"Image Name: {pname}, Image Path: {image_path}, Similarity Score: {score:.2f}")

#     return scores

# # Base image path
# base_image_path = 'https://m.media-amazon.com/images/I/71YG7EClYfL._SX679_.jpg'

# # Dictionary of image names and paths to compare with
# image_dict = {
#     'Image 1': 'https://m.media-amazon.com/images/I/61C+Y9zoAQL._SY695_.jpg',
#     'Image 2': 'https://m.media-amazon.com/images/I/71YG7EClYfL._SX679_.jpg',
#     'Image 3': 'https://m.media-amazon.com/images/I/81ATe15IyHL._SX695_.jpg',
#     'Image 4': 'https://m.media-amazon.com/images/I/71xWtLhH2GL._SX695_.jpg',
#     'Image 5': 'https://m.media-amazon.com/images/I/61OBcY37KXL._SY695_.jpg',
#     'Image 6': 'https://m.media-amazon.com/images/I/710+f7XX2FL._SY695_.jpg',
#     'Image 7': 'https://m.media-amazon.com/images/I/71u2XOFXAIL._SX695_.jpg',
#     'Image 8': 'https://m.media-amazon.com/images/I/61U0BBQYhrL._SY695_.jpg',
# }

# # Compare the base image with the dictionary of images
# results = compare_images(base_image_path, image_dict)

# # Print results
# for pname, image_path, score in results:
#     print(f"Image Name: {pname}, Image Path: {image_path}, Similarity Score: {score:.2f}")

dfURL = [
    'https://m.media-amazon.com/images/I/61C+Y9zoAQL._SY695_.jpg',
    'https://m.media-amazon.com/images/I/71YG7EClYfL._SX679_.jpg',
    'https://m.media-amazon.com/images/I/81ATe15IyHL._SX695_.jpg',
    'https://m.media-amazon.com/images/I/71xWtLhH2GL._SX695_.jpg',
    'https://m.media-amazon.com/images/I/61OBcY37KXL._SY695_.jpg',
    'https://m.media-amazon.com/images/I/710+f7XX2FL._SY695_.jpg',
    'https://m.media-amazon.com/images/I/71u2XOFXAIL._SX695_.jpg',
    'https://m.media-amazon.com/images/I/61U0BBQYhrL._SY695_.jpg',
]

def featureExtraction(url):
    n = 'no'
    return str(url),n

def preProcessData():
    # dfURL = df['product_url']
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(featureExtraction, dfURL)

    f = [r for r in results]
    for item in f:
        print(item[0])
        print(item[1])
        print('\n')
        

if __name__ == '__main__':
    preProcessData()