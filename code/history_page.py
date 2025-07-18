import streamlit as st
import json
import pandas as pd
from PIL import Image


def history_page():
    image = Image.open('assets\\History.jpg')
    st.image(image, caption='', width=250)
    st.header("History 📜")

    with open("constant\\database.json","r") as f:
        database = json.load(f)

    if len(database) == 0:
        st.warning("No sessions found in database")
        return
    
    history_dict = {"Application ID" : [], "DOC name" : [], "Time uploaded" : []}
    for application_id in database:
        doc_list = database[application_id]["doc_list"]
        if doc_list:
            for i in range(len(doc_list)):
                if i==0:
                    history_dict["Application ID"].append(application_id)
                else:
                    history_dict["Application ID"].append("")
                history_dict["Time uploaded"].append(doc_list[i]["time_uploaded"])
                history_dict["DOC name"].append(doc_list[i]["doc_name"])
    df = pd.DataFrame.from_dict(history_dict)
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

if __name__ == "__main__":
    history_page()