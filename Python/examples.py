import pandas as pd
from google.cloud import vision
import os
import concurrent.futures

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\storage_key.json"

def get_image_labels(image_path):
    """Get labels detected in an image using Google Vision API."""
    client = vision.ImageAnnotatorClient()
    img = vision.Image()
    img.source.image_uri = image_path
    
    response = client.label_detection(image=img)
    labels = response.label_annotations
    
    return labels

def compare_labels(base_labels, target_labels):
    """Compare labels between two images and return a similarity score."""
    base_labels_set = {label.description for label in base_labels}
    target_labels_set = {label.description for label in target_labels}
    
    intersection = base_labels_set.intersection(target_labels_set)
    union = base_labels_set.union(target_labels_set)
    
    if not union:
        return 0.0
    return len(intersection) / len(union)

def compare_images(base_image_path, image_dict):
    """Compare a base image with a dictionary of images using label detection."""
    base_labels = get_image_labels(base_image_path)
    scores = []
    
    for pname, image_path in image_dict.items():
        target_labels = get_image_labels(image_path)
        score = compare_labels(base_labels, target_labels)
        scores.append((pname, image_path, score))
    
    # Sort images by similarity score in descending order
    scores.sort(key=lambda x: x[2], reverse=True)
    
    # Print similarity scores
    for pname, image_path, score in scores:
        print(f"Image Name: {pname}, Image Path: {image_path}, Similarity Score: {score:.2f}")

    return scores

# Base image path
base_image_path = 'path/to/base/image.jpg'

# Dictionary of image names and paths to compare with
image_dict = {
    'Image 1': 'https://m.media-amazon.com/images/I/61C+Y9zoAQL._SY695_.jpg',
    'Image 2': 'https://m.media-amazon.com/images/I/71YG7EClYfL._SX679_.jpg',
    'Image 3': 'https://m.media-amazon.com/images/I/81ATe15IyHL._SX695_.jpg',
    'Image 4': 'https://m.media-amazon.com/images/I/71xWtLhH2GL._SX695_.jpg',
    'Image 5': 'https://m.media-amazon.com/images/I/61OBcY37KXL._SY695_.jpg',
    'Image 6': 'https://m.media-amazon.com/images/I/710+f7XX2FL._SY695_.jpg',
    'Image 7': 'https://m.media-amazon.com/images/I/71u2XOFXAIL._SX695_.jpg',
    'Image 8': 'https://m.media-amazon.com/images/I/61U0BBQYhrL._SY695_.jpg',
}

# Compare the base image with the dictionary of images
results = compare_images('https://m.media-amazon.com/images/I/71YG7EClYfL._SX679_.jpg', image_dict)

# Print results
for pname, image_path, score in results:
    print(f"Image Name: {pname}, Image Path: {image_path}, Similarity Score: {score:.2f}")
