
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# car_types = ["toyota", "bmw", "mercedes"]
#
# car = st.text_input("Type a car model")
# button = st.button("Check availability")
#
# if button == True:
#     if car in car_types:
#         st.success("Car is available")
#     else:
#         st.error("Car is not available")

with st.sidebar:
    addSelectbox = st.sidebar.selectbox(
        "Select an option",
        ("x", "y")
    )

tab1, tab2 = st.tabs(["graph1", "graph2"])
df = pd.read_csv('data.csv')

with tab1:
    st.header("Graph 1")
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    st.pyplot(fig)
with tab2:
    st.header("Graph 2")
##edit test
