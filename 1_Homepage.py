import streamlit as st
import pickle
import azure.cognitiveservices.speech as speechsdk
import requests, uuid
from PIL import Image
import urllib.request
import pandas as pd



def recognize_from_mic():
	#Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
	#Remember to delete the brackets <> when pasting your key and region!
    speech_config = speechsdk.SpeechConfig(subscription="ae00438ae4b84eb19f9215824155a6e5", region="eastus", speech_recognition_language="es-AR")

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
   
    
    #Asks user for mic input and prints transcription result on screen
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    resultado = result.text
    return resultado






with open('proyectofinal/category_classifier1.pkl', 'rb') as f:
    clf = pickle.load(f)

with open('proyectofinal/category_vectorizer1.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.set_page_config(
    page_title="Proyecto Final",
    page_icon="👋",
)

st.title("Sistema de Recomendación Amazon")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""


submit = st.button("¡Dejame escucharte!")
if submit:
   
    resultado =recognize_from_mic()
    resultado= str(resultado)
        
        # Add your key and endpoint
    key = "0cf563c082b946b3accc3a21e1725cc8"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "eastus"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'es',
        'to': ['en']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': resultado
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    for values in response[0].values():
        river = values[0].values()
        values = list(river)
        traductor = values[0]






    test_set = [traductor]
    new_test = vectorizer.transform(test_set)

    prediccion =clf.predict(new_test)
    prediccion = prediccion[0]
    
    st.title(f'Texto de voz: {resultado}')
    st.title(f'Traduccion: {traductor}')
    st.title(f'Categoria: {prediccion}')
    
    


    df = pd.read_csv(f'proyectofinal/products/{prediccion}.csv')
    df1 =df['imUrl'].head(8)
    j = 0
    
    for i in df1:
        
        



        urllib.request.urlretrieve(i,f"{j}.png")
        j = j+1


    

    col1, col2, col3,col4 = st.columns([1,1,1,1])
    image = Image.open("0.png")

    precio =str(df['price'][0])

    titulo = str(df['title'][0])

    col1.image(image, caption= f'Precio {precio} --  {titulo}')


    image = Image.open("1.png")


    precio =str(df['price'][1])

    titulo = str(df['title'][1])

    col2.image(image, caption= f'Precio {precio} --  {titulo}')
    image = Image.open("2.png")





    precio =str(df['price'][2])

    titulo = str(df['title'][2])

    col3.image(image, caption= f'Precio {precio} --  {titulo}')

    image = Image.open("3.png")



    precio =str(df['price'][3])

    titulo = str(df['title'][3])

    col4.image(image, caption= f'Precio {precio} --  {titulo}')

    
    col1, col2, col3,col4 = st.columns([1,1,1,1])
    image = Image.open("4.png")




    precio =str(df['price'][4])

    titulo = str(df['title'][4])

    col1.image(image, caption= f'Precio {precio} --  {titulo}')
    image = Image.open("5.png")






    precio =str(df['price'][5])

    titulo = str(df['title'][5])

    col2.image(image, caption= f'Precio {precio} --  {titulo}')

    image = Image.open("6.png")




    precio =str(df['price'][6])

    titulo = str(df['title'][6])

    col3.image(image, caption= f'Precio {precio} --  {titulo}')





    image = Image.open("7.png")



    precio =str(df['price'][7])

    titulo = str(df['title'][7])

    col4.image(image, caption= f'Precio {precio} --  {titulo}')

            