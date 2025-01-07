import os
import json
import base64

from dotenv import load_dotenv

import openai
from openai import OpenAI

from .tokens_gpt import SliderMaxTokens
from .temperature_gpt import SliderTemperature
from .prompts import Contenidos
from .model_gpt import SelectModel
from .password_ai import Passwords


# import reflex as rx
load_dotenv()
api_key = os.getenv("TOKEN_OPENAI")

if not api_key:
    raise ValueError("No se ha encontrado la variable de API KEY de OpenAI. Por favor, revisa tu archivo .env")
print("La API está configurada correctamente")


client = OpenAI(api_key=os.getenv("TOKEN_OPENAI"))


def generate_content(model: str = SelectModel, prompt: str = Contenidos, max_tokens: int = SliderMaxTokens, temperature: float = SliderTemperature) -> str:
    """
    Genera contenido usando el modelo de OpenAI.

    Args:
        model (str): Modelo a usar (por ejemplo, "gpt-4").
        prompt (str): Prompt de entrada.
        max_tokens (int): Número máximo de tokens en la respuesta.
        temperature (float): Nivel de creatividad.
        stream (bool): Si debe usarse streaming.

    Returns:
        str: El texto generado o un mensaje de error.
    """

    try:
        # Modo de streaming
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
        )
        
        generated_content = ""
        
        for chunk in response:
            if "choices" in chunk and "delta" in chunk.choices[0]:
                generated_content += chunk.choices[0].delta.get("content", "")
        
        return generated_content

    except openai.APIConnectionError:
        print('Error: No se ha podido conectar con el servidor. Verifica tu conexión a Internet.')
        return("Error: No se ha podido conectar con el servidor. Verifica tu conexión a Internet.")
    except openai.RateLimitError:
        print('Error: Tiempo de espera sobrepasado (código 429). Espera un momento e inténtalo de nuevo.')
        return("Error: Tiempo de espera sobrepasado (código 429). Espera un momento e inténtalo de nuevo.")
    except openai.APIError as e:
        print(f"Error de la API: {e}")
        return(f"Error de la API: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        return(f"Error inesperado: {e}")


print(generate_content(model="gpt-4", prompt="Háblame de tazas de café", max_tokens=100, temperature=0.5))

# def post_to_wordpress(title: str, estado_contenido: str, content: str, dominio: str, user: str, password: str, tipo_contenido: str) -> str:
#     """
#     Publica contenido en un sitio de WordPress.

#     Args:
#         title (str): Título del post.
#         content (str): Contenido del post.
#         user (str): Nombre de usuario.
#         password (str): Contraseña.
#         dominio (str): dominio del sitio de WordPress.
#         tipo_contenido (str): Tipo de contenido (por ejemplo, "posts").
#         estado_contenido (str): Estado del contenido (por ejemplo, "publish").

#     Returns:
#         str: Mensaje de éxito o error.
#     """
#     credentials = f"{user}:{password}"
#     token = base64.b64encode(credentials.encode()).decode()
#     headers = {'Authorization' : f'Basic {token}'}
#     post_data = {
#         'title': title,
#         'content': estado_contenido,
#         'status': content,
#     }
#     url = f'{dominio}/wp-json/wp/v2/{tipo_contenido}'
#     response = requests.post(url, headers=headers, json=post_data)
#     if response.status_code == 201:
#         return 'El post se ha publicado con éxito.'
#     else:
#         return f'Error al publicar el {tipo_contenido}[:1]: {response.content}'
    
# # Genera el contenido que subiremos a la web de WordPress

# content = generate_content(model, prompt)
# if content:
#     title=title 
#     post_to_wordpress(title, estado_contenido, content, dominio, user, password, tipo_contenido)
# else:
#     print('No se ha podido generar contenido, completa todos los campos')