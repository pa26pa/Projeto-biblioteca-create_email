from openai import OpenAI
import os 
from dotenv import load_dotenv
import json
from resources import load, upload

load_dotenv()

class CreateEmail():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def create_email_design(self,objective,style,primary_color,company_name,language,include_logo,include_footer):
        needs = f"objective: {objective}, style: {style}, primary_color:{primary_color},company_name:{company_name}, language: {language}, include_logo:{include_logo},include_footer:{include_footer}"
        
        
        response = self.client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "system",
                    "content": """
        You are an expert HTML email designer.

        Your task is to create professional, responsive HTML email templates.

        Rules:
        - Return ONLY a valid JSON object.
        - Do NOT use Markdown.
        - Do NOT wrap the HTML inside ```html.
        - Do NOT explain anything.
        - Use only HTML with internal CSS inside a <style> tag.
        - The HTML must be compatible with most email clients (Gmail, Outlook, Apple Mail).
        - Use tables for layout when necessary.
        - The design must be clean, modern and responsive.
        - All CSS must be inside the HTML.
        - Do not use external CSS or JavaScript.
        - Images must use placeholder URLs.
        - Include a clear CTA (Call To Action) whenever appropriate.
        - Choose an appropriate color palette according to the email purpose.

        Return exactly this JSON format:

        {
            "template": "<complete html here>",
            "main_color": "#HEXCOLOR",
            "type": "email category",
            "title": "template title"
        }
        """
                },
                {
                    "role": "user",
                    "content": needs
                }
            ]
        )

        answer = json.loads(response.choices[0].message.content)
        
        data = load()
        
        name = (answer["title"])
        name = name.lower()
        
        answer = answer.pop("title",None)
        
        data[name] = answer
        
        upload(data)
        
        print(response.choices[0].message.content)

email = CreateEmail()

email.create_email_design("send an confirmation of the creation of an account ","modern and formal","blue","OpenAI","English","true","true")
