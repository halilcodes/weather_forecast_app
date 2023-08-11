import streamlit as st
import plotly.express as px
from backend import get_data

# place static or stable parts
st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.capitalize()}")


if place:
    try:
        # get the temp/sky data
        sky, temp, dates_in_str = get_data(place, days)

        # plot the temperature plot
        if option == "Temperature":
            figure = px.line(x=dates_in_str, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        elif option == "Sky":
            # for condition, date in zip(sky, dates_in_str):
            #     st.image(f"images/{condition}.png", width=150)
            #     st.write(date)
            paths = [f"images/{condition}.png" for condition in sky]
            st.image(paths, width=115, caption=dates_in_str)
    except KeyError as e:
        # st.write(e)
        st.write("Invalid City name, please try again.")
