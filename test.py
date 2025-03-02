import pandas as pd
import streamlit as st
import numpy as np
import time
import date

st.write("Hello")
x=st.text_input("Fav movie")
st.write(f"Fav movie is :- {x}")
is_clicked = st.button("Click Me")
st.link_button("profile" , "/profile?id=1234")
#is_clicked.
#st.write("Clicked")
#data = pd.read_csv("C:\\Users\\e008902\\NPO\\NNI Mismatch_9 Jan 251.csv")
#st.write(data)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a","b","c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)
