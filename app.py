import streamlit as st
import pandas as pd
from data.scraper import generate_sample_data
from data.clean import clean_data, summarize_by_district
from data.map import create_heatmap
import streamlit.components.v1 as components

st.set_page_config(page_title="Darmstadt Rent Analysis", layout="wide")

st.title("🏠 Darmstadt Rent Price Analysis")
st.markdown("Interactive rent price analysis based on sample data for Darmstadt districts.")

df = generate_sample_data()
df = clean_data(df)
summary = summarize_by_district(df)

col1, col2, col3 = st.columns(3)
col1.metric("Avg. Price per sqm", f"{summary['avg_price_per_sqm'].mean():.2f} €")
col2.metric("Cheapest District", summary.loc[summary['avg_price_per_sqm'].idxmin(), 'district'])
col3.metric("Most Expensive District", summary.loc[summary['avg_price_per_sqm'].idxmax(), 'district'])

st.subheader("Price per sqm by District")
st.dataframe(summary.sort_values("avg_price_per_sqm", ascending=False), use_container_width=True)

st.subheader("Interactive Heatmap")
m = create_heatmap(summary)
m.save("map.html")
with open("map.html", "r") as f:
    html_content = f.read()
components.html(html_content, height=500)