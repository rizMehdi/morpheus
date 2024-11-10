import streamlit as st
import streamlit.components.v1 as components
import os

# Set up the path for the offline webpage
offline_page_path = "index.html"

# Check if the offline file exists
if os.path.exists(offline_page_path):
    # Display the iframe with the offline webpage
    st.write("## Offline Webpage Viewer")
    st.write("This is an offline webpage embedded in an iframe.")
    
    # Embed the offline page in the iframe
    with open(offline_page_path, 'r') as f:
        html_content = f.read()
    
    # Render iframe with the HTML content
    components.html(html_content, height=800, scrolling=True)
else:
    st.error("Offline webpage not found. Please check the file path.")
