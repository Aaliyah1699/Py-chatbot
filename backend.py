import openai
import os
from dotenv import load_dotenv

load_dotenv()


# Backend
class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("API_KEY")

    def get_response(self, user_input):
        res = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return res


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("What skills make a good software engineer?")
    print(response)
