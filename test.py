from doc import Documents
from rag import Rag
import cohere
import os
import hnswlib
import json
import uuid
from typing import List, Dict
from unstructured.partition.html import partition_html
from unstructured.chunking.title import chunk_by_title

co = cohere.Client('xxgLc7lYofMMXtHhUcqM60iPlRWvjHQ4Syy6ttKz')

class App:
    def __init__(self, rag: Rag):
        """
        Initializes an instance of the App class.

        Parameters:
        chatbot (Chatbot): An instance of the Chatbot class.

        """
        self.rag = rag
    
    def run(self):
        """
        Runs the chatbot application.

        """
        while True:
            # Get the user message
            message = input("User: ")

            # Typing "quit" ends the conversation
            if message.lower() == "quit":
                print("Ending chat.")
                break
            else:
                print(f"User: {message}")

            # Get the chatbot response
            response = self.chatbot.generate_response(message)
            print(response)
            
            # Print the chatbot response
            print("Chatbot:")
            flag = False
            for event in response:
                # Text
                if event.event_type == "text-generation":
                    print(event.text, end="")

                # Citations
                if event.event_type == "citation-generation":
                    if not flag:
                        print("\n\nCITATIONS:")
                        flag = True
                    print(event.citations)

            print(f"\n{'-'*100}\n")

# read docs.json as a list of dictionaries
import json
with open('source/docs.json') as f:
    docs = json.load(f)

documents = Documents(docs)

# Create an instance of the Chatbot class with the Documents instance
rag = Rag(documents)

# Create an instance of the App class with the Chatbot instance
app = App(rag)

# Run the chatbot
app.run()