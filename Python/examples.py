import pandas as pd
from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\storage_key.json"
import concurrent.futures

import requests
def is_url_image(url):
   response = requests.head(url)  # Use HEAD request to check headers only
   content_type = response.headers.get('Content-Type')
   if content_type and 'image' in content_type:
      return True
   else:
      return False
  
sam = pd.read_csv('D:\\Work and Assignments\\Python\\sampleCSV.csv')
s_uri = sam['product_url'].tolist()


def extract_info(uri):
        txt = ''
        if(is_url_image(uri)==True):
            client = vision.ImageAnnotatorClient()
            img = vision.Image()
            img.source.image_uri = uri
            
            res_label = client.label_detection(img)
            labels = res_label.label_annotations
            label = [lab.description for lab in labels]
            
            objects = client.object_localization(image=img).localized_object_annotations
            obj = [ob.name for ob in objects]
            txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj}"
        
        else:
           txt = "Invalid"
        return txt

res = sam

def my():
    #if __name__ == '__main__':
        # Use ProcessPoolExecutor to execute the function in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(extract_info, s_uri)

        # Print the results after they are computed
        fea = [r for r in results]
        # for r in results:
        #     fea.append(r)

        for i in range(len(fea)):
            res.loc[i, "objects_extracted"] = fea[i]
        
        print(res)
my()
