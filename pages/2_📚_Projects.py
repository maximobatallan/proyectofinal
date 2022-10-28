import streamlit as st
from PIL import Image


st.title("Juego de palabras de power")

st.write("aca estamos viendo la cantidad de palabras que se uso para hacer el sistema de nlp")

image = Image.open('streamlit-multipage-app-example\pages\riverr.png')

image(image, caption='Sunrise by the mountains')

st.write("en la proxima imagen se ve como ....")