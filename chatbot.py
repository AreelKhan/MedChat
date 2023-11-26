import os
import cohere
import cv2

import numpy as np
from PIL import Image
from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder
from langchain.chat_models import ChatCohere
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from typing import List
from classify import get_user_intent
from utils import BrainTumourDiagnosisAgent
from doc import Documents
from rag import Rag

import json

with open('source/docs.json') as f:
    docs = json.load(f)

DOCS = Documents(docs)

COHERE_API_KEY = "K9mxtkR5NvHF6xPw5uVAPF6lqs9hWABddILV8156"

SYSTEM_MESSAGE_PROMPT = """
You are a chat bot named MedChat, a help agent for medical professionals that answers questions concerning medical conditions and diagnoses. You have access to medical documents with reliable information which you can use to answer questions.
You are able to answer three types of user questions.
1. Diagnose brain MRI images
2. Summarize Blood test results
3. Answer general medical questions using medical literature

Any question that isn't about medicine, or disease diagnoses should not be answered. If a user asks a question that isn't about medicine, you should tell them that you aren't able to help them with their query. Keep your answers concise, and shorter than 5 sentences.
"""
MEMORY_KEY = "chat_history"

class MedicalChatBot:
    """
    Master Agent.
    """
    def __init__(self, api_key, uploaded_files) -> None:
        self.api_key = api_key
        self.uploaded_files = uploaded_files

        self.co = cohere.Client(COHERE_API_KEY)

    def read_image(self, file):
        # Read the image file into a NumPy array
        image = Image.open(file)
        image_array = np.array(image)
        return image_array
 
    def get_image_file(self):
        if self.uploaded_files:
            file = self.uploaded_files[-1]
            if file.type.startswith("image"):
                return self.read_image(file)
        return None
    
    def generate_response(self, message, chat_history, message_placeholder):
        full_response = ""
        for response in self.co.chat(
            message=message,
            model="command-nightly",
            chat_history=[
                {"role": m["role"], "message": m["message"]}
                for m in chat_history
            ],
            stream=True
        ):
            if response.event_type == 'text-generation':
                full_response += (response.text)
                message_placeholder.markdown(full_response + "▌")
        return full_response

    def query(self, message, chat_history, message_placeholder):

        # first we check the user intent
        intent = get_user_intent(message)

        if intent[0] == "Diagnose Brain Tumour":
            # call brain diagnosis model
            image = self.get_image_file()
            test = BrainTumourDiagnosisAgent(image)
            result = test.diagnose()

            message = f"According to the disease diagnosis models, the probability of a positive tumour diagnosis is {result}%. Write a one-sentence message to the user confirming this information. Give the answer as a percent. Do not answer in more than one sentence."
        
            full_response = self.generate_response(message, chat_history=chat_history, message_placeholder=message_placeholder)
        
            return full_response
        
        if intent[0] == "Other":
            rag = Rag(DOCS)
            response =  rag.generate_response(message)

            answer = []

            flag = False
            for event in response:
                # Text
                if event.event_type == "text-generation":
                    answer.append(str(event.text).join("\n"))
                    answer.append("\n")

                # Citations
                if event.event_type == "citation-generation":
                    if not flag:
                        answer.append("Citations: \n")
                        flag = True
                    answer.append(str(event.citations))
                    answer.append("\n")

            print(answer)
            try:
                return "".join(answer)
            except:
                return "Something went wrong"
        
        else:
            return "Something went wrong"














