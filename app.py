import streamlit as st
import pandas as pd

df = pd.read_csv("data/verbs.tsv", sep="\t")
df["number"] = df["number"].astype("category")
st.dataframe(df.sample(10))
