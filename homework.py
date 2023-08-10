import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("happy.csv")

st.title("In search for happiness")

option_x = st.selectbox("Select the data for the X-Axis: ", ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the y-Axis: ", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{option_x} and {option_y}")

match option_x:
    case "GDP":
        x_axis = df["gdp"]
    case "Happiness":
        x_axis = df["happiness"]
    case "Generosity":
        x_axis = df["generosity"]

match option_y:
    case "GDP":
        y_axis = df["gdp"]
    case "Happiness":
        y_axis = df["happiness"]
    case "Generosity":
        y_axis = df["generosity"]

figure = px.scatter(x=x_axis, y=y_axis, labels={"x": option_x, "y": option_y})

st.plotly_chart(figure)
