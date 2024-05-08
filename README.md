# Solving-Coding-Problems-With-Machine-Learning

## Contributors
- Joshua Brooks Jr
- Sajiv Gnanasekaran
- Dr. Nguyen Ho

CS496 capstone project at Loyola University Maryland

## Project Description

We created 3 machine learning models to predict how accurately Chat GPT 4 or Google Gemini will answer a programming question. This was the result of a semester-long research capstone. 

## File Structure

All of our machine learning work can be found in Analysis.ipynb. The data collection scraping the programming questions from kattis is in kattis.ipynb. The code for collecting Gemini responses to those questions and grading the results using the kattis-cli can be found in gemini.ipynb. 

### Kattis questions
The 3705 kattis questions we collected are in a json called kattis_questions_cleaned.json. In the kattis2 folder, each question has a subfolder with its name. In that subfolder, there is a prompt text file with the question text. There is also a gemini.py file with the Python solution Gemini was able to make, with the grade appended in a comment at the top. The comment consists of three things: (difficulty) (right/wrong/error) (fraction with tests passed). Only 1000 of these folders were able to be put viewed on Github because of size limitations. Only the first 100 have graded Gemini solutions.

## Installation Instructions
To run our Gemini scripts, you need to install the following and have an API Key
```
pip install -q -U google-generativeai
pip install openai
```
To run our GPT4 scripts, you will need to have access to the OpenAI API and pay for GPT4 API access
## How to Run

## How to Test

