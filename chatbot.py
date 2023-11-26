import os
import cv2

from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder
from langchain.chat_models import ChatCohere
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from typing import List
from classify import get_user_intent
from utils import BrainTumourDiagnosisAgent

COHERE_API_KEY = "K9mxtkR5NvHF6xPw5uVAPF6lqs9hWABddILV8156"
#os.environ["COHERE_API_KEY"] = COHERE_API_KEY
SYSTEM_MESSAGE_PROMPT = """

    The chatbot's name is MedChat, a help agent for medical professionals that answers questions concerning medical
    conditions and diagnoses.
    
    MedChat is able to answer three types of user questions.
    1. Diagnose brain MRI images
    2. Summarize Blood test results
    3. Answer general medical questions using medical literature
    
    No question that isn't about medicine, or disease diagnoses should be answered. If a user asks a question
    that isn't about  medicine, you should tell them that you aren't able to help them with their query.
    
"""
MEMORY_KEY = "chat_history"

class MedicalChatBot:
    """
    Master Agent.
    """
    def __init__(self, api_key, uploaded_files) -> None:
        self.api_key = api_key
        self.uploaded_files = uploaded_files

        self.llm = ChatCohere(model="large", temperature=0.0, streaming=True)

        template = """Question: {question}

        Answer: Let's think step by step."""

        self.prompt = PromptTemplate(template=template,
                                input_variables=["question"],
                                system_message=SystemMessage(content=SYSTEM_MESSAGE_PROMPT),
                                extra_prompt_messages=[
                                    MessagesPlaceholder(variable_name=MEMORY_KEY),
                                ]
                                )

        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)
        # self.chain = LLMChain(prompt=prompt, llm=llm)

        # self.prompt = AGENT_HERE.create_prompt(
        #     system_message=SystemMessage(content=SYSTEM_MESSAGE_PROMPT),
        #     extra_prompt_messages=[
        #         MessagesPlaceholder(variable_name=MEMORY_KEY),
        #     ],
        # )

        self.memory = ConversationBufferMemory(
            memory_key=MEMORY_KEY,
            return_messages=True,
            input_key="input",
            output_key="output",
        )

    def get_uploaded_file(self, uploaded_files):
        if uploaded_files:
            print(uploaded_files)

    def query(self, message):

        # first we check the user intent
        intent = get_user_intent(message)

        if intent[0] == "Diagnose Brain Tumour":
            # call brain diagnosis model
            image = cv2.imread('test_images/2_brain.jpg')
            test = BrainTumourDiagnosisAgent(image)
            result = test.diagnose()

            ans = f"According to the disease diagnosis models, the probability of a positive tumour diagnosis is {result}%. Write a one-sentence message to the user confirming this information. Do not answer in more than one sentence."

            return self.llm_chain.run(ans)

        return self.llm_chain.run(message)













