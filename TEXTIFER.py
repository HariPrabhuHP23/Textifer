def Image_to_text():
    st.write("""
    Image to text
    """)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    
    if image_file is not None:
        img=Image.open(image_file)
        st.image((image_file),width=250)
        st.write(pytesseract.image_to_string(img))
    else:
        pass

    
def Speech_to_text():
    st.write("""
    Speech to text
    """)
    r = sr.Recognizer()
    audio_file = st.file_uploader("Upload Audio", type=["wav","mp3","ogg","flv"])
 
    if audio_file is not None:
        file_audio = st.audio(audio_file)
        with sr.AudioFile((audio_file)) as source:
            audio_text= r.listen(source)
            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                # using google speech recognition
                text = r.recognize_google(audio_text)
                st.write('Converting audio transcripts into text ...')
                st.write(text)
            except:
                st.write('Sorry.. run again...')
    
def translation():
    st.write("""
    Translator
    """)
    lang=st.selectbox("Select Language",('English','French','German','Spanish','arabic'))
    InputLanguageChoice='English'
    TranslateLanguageChoice=lang
    TextVar= st.text_input("Enter text")
    translator = Translator(from_lang= InputLanguageChoice,to_lang=TranslateLanguageChoice)
    Translation = translator.translate(TextVar)
    st.write(Translation)

import streamlit as st
import speech_recognition as sr
from translate import Translator
import pytesseract
from PIL import ImageTk, Image
import os
import cv2

st.title("TEXTIFER")

st.write("""
## Online Text Editor
""")
dataset_name=st.sidebar.selectbox("Select The Required Option",("Image to text","Speech to text","translator"))
if(dataset_name=="Image to text"):
    Image_to_text()
elif(dataset_name=="Speech to text"):
    Speech_to_text()

else:
    translation()

    
