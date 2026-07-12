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

        name = answer["title"]
        name = name.lower()
        
        answer.pop("title",None)
        
        data[name] = answer
        
        upload(data)
        
        print(response.choices[0].message.content)
    
    def create_email_auto(self, prompt):
        response = self.client.chat.completions.create(
        model="openrouter/free",
        messages=[
                {
                    "role": "system",
                    "content": """
        You are an professional HTML desinger
        
        Your task is to read a text, think and respond this categories:

            objective,style,primary_color,company_name,language,include_logo,include_footer
        
        Rules:
        - Return ONLY a valid JSON object.
        - Do NOT use Markdown.
        - Do NOT explain anything.
        - Include_footer and include_logo need to be respondend in True or False (exacly like that)
        - Do not add content that is not in the text.
        
        Return exactly this JSON format:

        {
            "objective": "objective here",
            "style": "style here",
            "primary_color": "primary color here",
            "company_name": "company name here",
            "language":"the language requested here",
            "include_logo":"include logo here (True or False)",
            "include_footer":"include footer here (True or False)"
        }
        """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print(response.choices[0].message.content)
        
        answer = json.loads(response.choices[0].message.content)
        objective = answer["objective"]
        style = answer["style"]
        primary_color = answer["primary_color"]
        company_name = answer["company_name"]
        language = answer["language"]
        include_logo = answer["include_logo"]
        include_footer = answer["include_footer"]
        
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
        
        print(answer)
    
email = CreateEmail()


email.create_email_design("send an confirmation of the creation of an account ","modern and formal","blue","OpenAI","English","true","true")

#email.create_email_auto("Crie um e-mail personalizado para os clientes da empresa TechVibe Soluções, escrito em Português (Brasil). O objetivo principal deste e-mail é dar as boas-vindas aos novos usuários que acabaram de criar uma conta na plataforma. Adote um estilo de comunicação moderno, dinâmico e acolhedor. Na formatação visual do e-mail, utilize a cor Azul Indigo #4B0082 como identidade principal. Certifique-se de incluir um espaço reservado para o logotipo no topo e um rodapé estruturado com links de redes sociais e opção de descadastro.")
