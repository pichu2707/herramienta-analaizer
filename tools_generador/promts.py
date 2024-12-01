import requests
import base64

from tools_generador.config import TOKEN_OPENAI
from .temperature_gpt import SliderTemperature
from .tokens_gpt import SliderMaxTokens
from .password_ai import Passwords

import reflex as rx
import openai
from openai import OpenAI

promt_optimización="""
Si es necesario para poder dar un contexto a tu contenido. El HTML solo hay que crear la parte del <body>, lo demás ya lo tenemos creado con el contexto que te he pasado. Todo este
    contenido debe ser original y con al menos 1000 palabras. No me crees estilos tampoco y la parte de <H1> también obviala porque usamos WordPress y ya
    tenemos el título que hace de <H1> y así aprovechamos para un mayor contenido. La parte de <!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Medidores de Campo para Instalación de Antenas de Televisión</title>
</head> y el marcado de <body> también quítalo del código, ten en cuenta que ya estás empezando a subir el texto en el body de manera automática
    No te inventes nada. 
    Pásame el cóntenido con marcado HTML para poderlo súbir con el código directamente.
    Tambíen dame un comienzo y un final al artículo, no dejes frases sin acabar o sin contexto.
"""

_client=None

def get_openai_client():
    global _client 
    if _client is None:
        _client=openai.OpenAI(api_key=TOKEN_OPENAI)
        
    return _client

class Contenidos(rx.State):
    title: str 
    promt: str
        
    def titleContenido():
        return rx.vstack(
            rx.input(
                placeholder="Seleccionando el título de mi contenido",
                value= Contenidos.title,
                on_change=Contenidos.title,
                required=True,
            ),
        )

    def blur_prompt():
        return rx.vstack(
            rx.text_area(
                placeholder="Escirbe aquí tu prompt",
                default_value=Contenidos.promt,
                size="2",
                value=Contenidos.promt,
                on_change=Contenidos.set_promtt,
                on_blur=Contenidos.set_promt,
                resize="both",
                radius="large",
                # autofocus=True,
            ),
        )

@rx.background
async def generate_content(self, model, prompt, temperature=SliderTemperature.temperature, max_tokens=SliderMaxTokens.slider):
    async with self:
        generate_content = ""
        try:
            stream = _client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens
            )
            for chunk in stream:
                rx.console_log(chunk.choices[0].delta.content or "", end="")
                generate_content += chunk.choices[0].delta.content or ""

        except openai.APIConnectionError as e:
            rx.console_log('No se ha podido conectar con el servidor.')
        except openai.RateLimitError as e:
            rx.console_log('Error status code 429 tiempo de espera sobrepasado, espera un poco y vuelve a intentarlo')
        except openai.APIStatusError as e:
            rx.console_log(f"Se ha recibido otro status code que no es 200: {e}")
        return generate_content
    
@rx.background
async def post_to_wordpress(self,title, estado_contenido, content, dominio, user, password, tipo_contenido):
    async with self:
        credentials = f"{user}:{password}"
        token = base64.b64encode(credentials.encode()).decode()
        headers = {'Authorization': f'Basic {token}'}
        post_data = {
            'title': title,
            'status': estado_contenido,
            'content': content,
        }
        url = f'{dominio}/wp-json/wp/v2/{tipo_contenido}'
        response = requests.post(url, headers=headers, json=post_data)
        if response.status_code == 201:
            rx.console_log('Contenido subido con éxito.')
        else:
            rx.console_log(f"Error al publicar el {tipo_contenido[:-1]}: {response.content}")
            
@rx.event
def Promt(promt1=Contenidos.promt, promp2=promt_optimización):
    promt1=Contenidos.promt
    promp2=promt_optimización
    promt=promt1+ ' ' +promp2
    return promt