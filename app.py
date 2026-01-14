import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import altair as alt  # type: ignore
st.header('Vehicles in the US')

# Load the CSV
df = pd.read_csv('vehicles_us.csv')

# Show columns and first few rows
st.write(df.columns)
st.write(df.head())

# Histogram of model years
fig = px.histogram(df, x='model_year', title="Histogram of Model Years")
st.plotly_chart(fig)

# Optional Condition vs Model Year histogram
show_histogram = st.checkbox('Show Condition Vs Model Year Histogram')
if show_histogram:
    fig_hist = px.histogram(
        df,
        x="condition",
        y="model_year",
        title="Condition Vs Model Year",
        labels={'condition': 'Condition', 'model_year': 'Model Year'}
    )
    st.plotly_chart(fig_hist)

# Scatter plot: Price vs Model Year
fig2 = px.scatter(df, x='model_year', y='price', title="Price vs Model Year")
st.plotly_chart(fig2)