import gradio as gr
from google.cloud import vision
import os
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Django Projects\\E_Commerce\\storage_key.json"
import webcolors



def get_colour_name(requested_colour):
    try:
        return webcolors.rgb_to_name(requested_colour)
    except ValueError:
        r_req, g_req, b_req = requested_colour
        min_diff = float('inf')
        closest_name = None
        
        for hex_value, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(hex_value)
            diff = (r_c - r_req) ** 2 + (g_c - g_req) ** 2 + (b_c - g_req) ** 2
            if diff < min_diff:
                min_diff = diff
                closest_name = name
        
        return closest_name


#Extracting features from input image
def Input_IMG_features(img_path):
    txt=''
    l=''
    try:
        if(img_path == None):
            gr.Warning("Please upload a Image")
            return txt

        #reading input image
        client = vision.ImageAnnotatorClient()
        with open(img_path, "rb") as image_file:
            content = image_file.read()
        img = vision.Image(content=content)
        
        #For retriving Labels
        res_label = client.label_detection(img)
        label = [label.description for label in res_label.label_annotations]

        response = client.image_properties(image=img)
        props = response.image_properties_annotation
        dominant_color = props.dominant_colors.colors[0].color
        rgb = (dominant_color.red, dominant_color.green, dominant_color.blue)
        label.append(get_colour_name(rgb))

        l+=f"{label}"
        #for objects
        objects = client.object_localization(image=img).localized_object_annotations
        obj = [ob.name for ob in objects]
        txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj}"
        print(l)
    except Exception as e:
        gr.Warning(f"Something happened!!!, \nPlease refresh and start again...{e}")
    
    return check_relevent_products(txt, l)

def rel(df: pd.DataFrame, inp):
    # Convert list of labels to strings
    df_labels_str = df['label'].apply(lambda x: " ".join(ast.literal_eval(x)))
    inp_str = " ".join(inp)
    
    # Vectorize labels
    vectorizer = CountVectorizer().fit(df_labels_str)
    df_vectors = vectorizer.transform(df_labels_str)
    inp_vector = vectorizer.transform([inp_str])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(inp_vector, df_vectors).flatten()
    
    sim =  [
        (df.iloc[i]['product_name'], df.iloc[i]['product_url'], score)
        for i, score in enumerate(similarities)
    ]
    return sorted(sim, key=lambda x: x[2], reverse=True)

def check_relevent_products(inp_features, lbl):
    try: 
        #Reading Data From Google Cloud Bucket CSV
        DB = pd.read_csv("gs://bucket-shreyash/Product_Data/Product_D.csv")
        #features Present in database csv file
        DB_features = DB['object']
        
        inp_features = set(ast.literal_eval(inp_features))
        lbl = set(ast.literal_eval(lbl))
        
        data = [len(inp_features.intersection(set(ast.literal_eval(feature)))) > 0 for feature in DB_features]
        
        new_df = DB[data][['product_name', 'product_url', 'label']] #.reset_index(drop=True)
        
        final = rel(new_df, lbl)
        # print(final)
        name, link = zip(*[(n, l) for n, l, _ in final])
        
        if(len(link)==0):
            gr.Warning(f"No product found in dataBase, \nPlease try again later")
        
        return zip(link,name)
    except Exception as e:
        gr.Warning(f"Failed to fetch relevent products, \nPlease refresh and start again...{e}")



relevent_prod = gr.Gallery(columns=[4],object_fit='contain',label='Relevent Products',height="fit-content",container=False, elem_id='gl',visible=True)

with gr.Blocks(title="Relevent Product Search",
               css="footer {visibility: hidden}"    
            ) as demo:
        
        gr.Interface(fn= Input_IMG_features,
                        inputs=gr.Image(label='Upload Product Image',type='filepath',height="auto"),
                        outputs= relevent_prod,
                        allow_flagging='never', 
                        submit_btn="Search"
                        
                    )
        
        gr.HTML("""
        <style>
            h1{
                margin-bottom:5px;
            }
            img{
                background-color: white;
                height:300px;
            }
            .unequal-height.svelte-sa48pu{
                display: flex;
                align-items:center;
                position: relative;
                flex-direction: column;
            }
            .svelte-vt1mxs.gap.panel{
                width: auto;
                margin-bottom:40px;
            }
            .grid-wrap svelte-hpz95u fixed-height{
                height:100%
            }
            .lg.svelte-cmf5ev {
                width: 250px;
            }
            .image-frame.svelte-rrgd5g img{
                width:400px;
                height:400px;
                object-fit: contain;
            }
        </style>
        """)

demo.launch(debug=True)