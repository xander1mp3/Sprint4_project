import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore
st.header('Vehicles in the US')
df = pd.read_csv('vehicles_us.csv')
st.write(df.columns)
fig = px.histogram(df, x='model_year', title="Histogram of Condition Vs Model Year")
fig.show()
show_histogram = st.checkbox('Show Condition Vs Model Year Histogram')
if show_histogram:
    fig_hist = px.histogram(df, x="condition", y="model_year", title="Condition Vs Model year", labels={'condition': 'Condition', 'model_year': 'Model Year'})
    st.plotly_chart(fig_hist)

fig2 = px.scatter(df, x='model_year', y='price', title="Price vs Model Year")
st.plotly_chart(fig2)
st.write(df.columns)
st.write(df.head())
