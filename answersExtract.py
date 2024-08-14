import os
from dotenv import load_dotenv
from google.generativeai.types.content_types import *
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

parser = StrOutputParser()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=GOOGLE_API_KEY)

criteria = ""
with open("criteria.txt","r") as JD:
    criteria += JD.read()

transcript = ""
with open("data.txt","r") as data:
    transcript += data.read()

template = """ transcript : {transcript}
 once done reading the text. return values as mentioned in {criteria}

 """

#future template
"""Hi Gemini. You are a generative llm, which is designed to partake in grading the
 responses of an interviewee. Your job is to analyze the transcript of a 
 recorded meeting. Your first step is to read the transcript and look for all 
 the possible questions the interviewer asks. Secondly, you have to pay close 
 attention to the responses from the interviewee and deduce how relevant the 
 answers were to the question asked. Job criteria: {criteria} and Transcript:
 {transcript}"""

chatPrompt = ChatPromptTemplate.from_template(template)
chain = chatPrompt | llm | parser

result = chain.invoke({"criteria":criteria, "transcript":transcript})
with open("FinalOutput.txt","w") as file:
    file.write(result)