from openai import OpenAI
import os 
from dotenv import load_dotenv

class create_email():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPEN_AI_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

        def create_email_design(self,standard):
            client = self.client
            response = client.chat.completions.create(
                model="qwen/qwen3-30b-a3b:free",
                messages=[
                    {
                        "role": "system",
                        "content": "Você é especialista em criar emails HTML profissionais."
                    }])

            print(response.choices[0].message.content)

            print(response.text)