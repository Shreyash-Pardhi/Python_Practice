import gradio as gr
from feature_extraction import features
from product_search_obj import prodSearch 

with gr.Blocks(title="Google Vision API",
               css="footer {visibility: hidden}"    
            ) as demo:
        with gr.Tab("Search Relevent Products"):
            prodSearch.render()
        with gr.Tab("Extract Image-Features"):
            features.render()
demo.launch()