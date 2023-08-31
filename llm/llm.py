from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

import os

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

class LLM:
    def __init__(self):
        self.key = os.environ["OPENAI_API_KEY"]

        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=self.key, max_tokens=50)

        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    """You are Sorena V humanoid robot having a conversation with a human. 
                    Please don't say anything about that you are a language model.
                    you are deveploed at CAST (Center of Advanced Systems and Technologies) in the University of Tehran, Iran.
                    you have 43 degrees of freedom and can speak only english.
                    please only respond with text and not code."""
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}")
            ]
        )

        self.memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
        self.conversation = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            verbose=True,
            memory=self.memory
        )

    def talk(self, text):
        response = self.conversation({"question": text})
        return response['text']


if __name__ == "__main__":
    llm = LLM()
    print(llm.talk("who are you? and who made you?"))