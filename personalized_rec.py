from dotenv import load_dotenv
load_dotenv() ##loading all the environment variable

import streamlit as st
import os,io
import google.generativeai as genai
from PIL import Image as PIL_Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## function to load gemini pro model and get responses 
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input_content):
    if input_content!='':
        response = model.generate_content(input_content)
    else : 
        response = model.generate_content(input_content)

    return response.text


## intialize streamlit app

st.set_page_config(page_title='Gaman Personalized Recommendation System!')
st.header('Gaman Personalized Recommendations!')

input_customer = st.text_input('Please add description of what kind of products or services you are looking for ...  ',key='input')
uploaded_body_file = st.file_uploader("Please upload an image of your suggestion ", type=['jpg','jpeg','png'])
uploaded_history_files = st.file_uploader("Please upload two images of your selected items", type=['jpg','jpeg','png'],accept_multiple_files=True)
image = ""
body_image = ""
history_images = []

if uploaded_body_file is not None:
    body_image = PIL_Image.open(uploaded_body_file)
    st.image(body_image,caption="Here is your uploaded Body image.", use_column_width = True)

# Check if the number of uploaded files is exactly two, display it and store it for Gemini prompt
if uploaded_history_files is not None:
    if len(uploaded_history_files) == 2:
        # Process and display the images
        for uploaded_file in uploaded_history_files:
            bytes_data = uploaded_file.getvalue()
            image = PIL_Image.open(io.BytesIO(bytes_data))
            history_images.append(image)
            st.image(image, caption='Uploaded Previous Shopping Images.', use_column_width=True)
        history_image_1 = history_images[0]
        history_image_2 = history_images[1]
    else:
        st.error("Please insert your selected Gaman E-Commerce items!")


submit = st.button('Give me recommendations')
response_arr = []

## when submit is clicked
if submit: 

    input_content = ["You are a smart recommender system for clothing. Based on the body type of a customer here",
                 "body image:" , body_image,
    "and the requirements given by customer here %s and the previous history of shopping in the images below, suggest 2 more clothings with detailed explanation\
    that this customer would be interested in buying"%input_customer,
    "dress 1:", history_image_1,
    "dress 2:", history_image_2]
    response = get_gemini_response(input_content)
    response_arr.append(response)
    st.subheader('The Response is')
    st.write(response)


submit1 = st.button('Not quite, give me more recommendations')
print(response_arr)

## when submit1 is clicked
if submit1: 

    input_content1 = [" As a smart recommender system for clothing, you just gave this response - %s based on the body type of a customer "%response_arr,
                 "body image:" , body_image,
    "and the requirements given by customer here %s and the previous history of shopping in the images below"%input_customer,
    "dress 1:", history_image_1,
    "dress 2:", history_image_2,
    "suggest 2 more clothings with detailed explanation as your previous suggestions were not helpful"]

    response1 = get_gemini_response(input_content1)
    st.subheader('I apologize that was not helpful, let me try again ')
    st.write(response1)

