import streamlit as st
import plotly.express as px
import datetime as dt


def get_data(days_num):
    today = dt.datetime.today()
    date = [(today + dt.timedelta(days=i)).strftime("%b %d, %Y") for i in range(days_num)]
    temperature = [30+i for i in range(days_num)]
    temperature = [days_num * i for i in temperature]
    return date, temperature


# st.set_page_config(layout="wide")

# st.markdown("<h1 style='text-align: center'>Home</h1>", unsafe_allow_html=True)

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.capitalize()}")

d, t = get_data(int(days))
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)
