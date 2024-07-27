import os

import openai

class Chatbot:
    def __init__(self):
       openai.api_key = os.getenv("OPENAIAPIKEY")

    def get_response(self, user_input):
        response = openai.Completion.create(
            #engine="text-davinci-003", This GPT Model was deprecated
            engine="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("write a joke about birds")
    print(response)


