import streamlit as st
import requests
import pandas as pd

@st.cache_data
def run_algo(data, selected_algo, min_sup, min_conf):
    print("text:", data)    
    url = f"http://localhost:8000/{selected_algo}"
    data = {
        "data": data,
        "minSup": min_sup,
        "minConf": min_conf
    }
    response = requests.post(url, json=data)
    return response.json(), response.status_code

st.title('Demo Application')

# Initialize session state variables if they do not exist
if 'text' not in st.session_state:
    st.session_state.text = ""

# Text box for entering text
text = st.text_area("Enter the data you want to test", value=st.session_state.text, height=150)

# Voice selection buttons
algo_options = ['Apriori', "AprioriHashTree", "FPGrowth"]
selected_algo = st.radio("Choose an algorithm:", algo_options, format_func=lambda x: x.capitalize(), horizontal=True)

# Input boxes for minSup and minConf
min_sup = st.number_input("Enter minSup:", min_value=0.0, max_value=1.0, value=0.6, step=0.1)
min_conf = st.number_input("Enter minConf:", min_value=0.0, max_value=1.0, value=0.8, step=0.1)

# Button to trigger algorithm
if st.button("Submit"):
    lines = text.strip().split('\n')
    data = [line.split(',') for line in lines]
    result, status_code = run_algo(data, selected_algo, min_sup, min_conf)
    if status_code == 200:
        st.write("Response:")

        # Process and display freq_itemsets
        freq_itemsets = result['freq_itemsets']
        st.write("Frequent Itemsets:")
        formatted_itemsets = ["(" + itemset + ")" for itemset in freq_itemsets]
        st.write(", ".join(formatted_itemsets))

        # Process and display rules
        rules = result['rules']
        st.write("Rules:")
        for rule in rules:
            lhs = ', '.join(rule['lhs'])
            rhs = ', '.join(rule['rhs'])
            st.write(f"{{'{lhs}'}} ------> {{'{rhs}'}} conf: {rule['confidence']}")
    else:
        st.write("Error:", status_code)
