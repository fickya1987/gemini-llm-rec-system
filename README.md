# Personalized Clothing Recommendation Application built using Gemini-Vision-Pro LLM

_Keywords_ - Gemini Vision, LLM, Streamlit, NLP, chatbot, personalization, recommendation system, virtual environment

## Context 

Natural Language Models have recently shown remarkable capabilities in comprehending human needs, preferences, behavior and emotions. <br> 
We leverage that in demonstrating the future of personalized recommendation systems. <br>
We build a personalized clothing recommendation application using Gemini-Vision-Pro LLM and Streamlit. It uses images of customer's body type as well as images of the items previously purchased to give personalized recommendations to the customer in real-time. <br> 

Note that - 
1. This model could be fine-tuned with large inventory data on platforms like _generative_ to give business relevant recommendations. <br>
2. This is currently an image-to-text model from Gemini initial release, but Gemini (as well as other LLMs) would be soon capable of image-to-image communication, that could be a game changer compared to current systems. <br>

## Method 

Step 1 : Generate API key from Gemini (unique to each user). <br>

Step 2 : Create virtual environment with requirements.txt file. <br>

Step 3 : Make a folder with customer's previous purchase images and personal body image. <br>

Note that in deployment, this would be recovered from a cloud bucket (like Amazon S3) and body details taken in real-time from the customer. <br>

Step 4 : Activate the virtual environment in command line using - conda activate name_of_your_venv. <br>

Step 5 : Make sure you have personalized_rec.py file in your current directory. <br>

Step 6 : Launch the application by running this in command line - streamlit run personalized_rec.py. <br>

Step 7 : Add a text prompt about what you want from the recommendation system. <br>

Step 8 : Upload 1 body type image and 2 previous history images on the application interface that is just launched (from the folder made in Step 3). <br>

Step 9 : Hit 'Give me recommendations' button and 'Not quite, give me more recommendations' button if you are not satisfied with the results. <br>

Step 10 : Exit the app from the terminal by pressing Ctrl+C. <br> 

## Demo 
1. Launching the application from command line 
![](demo1_1.png)

2. Adding description of what I am looking for in the store (in natural language text) 
![](demo1_2.png)

3. Uploading body type image
![](demo1_3.png)

4. Uploading previous purchase images
![](demo1_4.png)
![](demo1_5.png)
![](demo1_6.png)

5. Hit 'Give me Recommendations' and see the LLM response
![](demo1_7.png)

6. Hit 'Not quite, give me more recommendations' if not satisfied
![](demo1_8.png)





