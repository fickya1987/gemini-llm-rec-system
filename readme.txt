Personalized Recommendation System Application using Gemini-Vision-Pro LLM


This Application uses Gemini-Vision-Pro LLM, customer's body type as well as previous purchase history to give personalized recommendations to the customer in real-time.

Natural Language Models have recently shown remarkable capabilities in comprehending human emotions, needs, preferences and behavior.  

We leverage that in demonstrating the _soon_ to be future of personalized recommendation systems

Note that - 

1. This model could be fine-tuned with large inventory data on platforms like _generative_ to give business relevant recommendations

2. This is currently an image-to-text model, but Gemini (as well as other LLMs) would be soon capable of image-to-image recommendations, that could be a game changer compared to current systems



Step 1 Generate API key from gemini (unique to each user) 

Step 2 Create virtual environment with requirements.txt file 

Step 3 Make a folder with customer's previous purchase images and personal body image 

Note that in deployment, this would be recovered from a cloud bucket (like Amazon S3) and body details taken in real-time from the customer 

Step 4 Activate the virtual environment in command line using - conda activate name_of_your_venv

Step 5 Make sure you have personalized_rec.py file in your current directory

Step 6 Launch the application by running this in command line - streamlit run personalized_rec.py

Step 7 Add a text prompt about what you want from the recommendation system

Step 8  Upload 1 body type image and 2 previous history images on the application interface that is just launched (from the folder made in Step 3) 

Step 9 Hit 'Give me recommendations' button and 'Not quite, give me more recommendations' button if you are not satisfied with the results 

Step 10 Exit the app from the terminal by pressing Ctrl+C