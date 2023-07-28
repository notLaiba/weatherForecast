import streamlit as st
import plotly.express as px
from backend import get_data

# interface
st.title("Weather Forecast for Next Few Days")
place = st.text_input("Place:")
days = st.slider("Forecasted_days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place} ")

if place:
    # get the data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                      "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_conditons = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditons]
            print(sky_conditons)
            st.image(image_paths, width=115)

    except KeyError:
        st.write("That place does not exist.")
