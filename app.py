# Imports

import streamlit as st
import pandas as pd

# Set up data

df = pd.read_csv("data/verbs.tsv", sep="\t")
df["number"] = df["number"].astype("category")

# Set up interface

st.write("LatFlex v0.2")

st.dataframe(df.sample(10))

if st.button("Refresh"):
    st.experimental_rerun()

st.write(
    "Coded by diyclassics, Jan. 2023. Code [here](https://github.com/diyclassics/latflex)."
)
