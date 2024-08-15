import streamlit as st
import requests
import pandas as pd

@st.cache_data
def run_algo( id, top_k, num_animes):
    url = f"http://localhost:8000/colab_filtering"
    data = {
        "id": id,
        "top_k": top_k,
        "num_animes": num_animes
    }
    response = requests.post(url, json=data)
    return response.json(), response.status_code

st.title('Demo Colab filtering Application')

# Initialize session state variables if they do not exist
if 'text' not in st.session_state:
    st.session_state.text = ""

# Input boxes for minSup and minConf
id = st.number_input("Enter minSup:", min_value=0, value=0, step=1)
top_k = st.number_input("Enter minConf:", min_value=0, value=2, step=1)
num_anime = st.number_input("Enter minConf:", min_value=0, value=3, step=1)

# Button to trigger algorithm
if st.button("Submit"):
    result, status_code = run_algo(id, top_k, num_anime)
    if status_code == 200:
        st.write("Recommended Anime Name:")
        print(result)
        for anime in result['animes']:
            st.write(anime)
    else:
        st.write("Error:", status_code)
