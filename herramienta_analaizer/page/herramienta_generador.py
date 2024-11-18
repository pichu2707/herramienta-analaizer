import requests
from requests.auth import HTTPBasicAuth
import json
import base64

import reflex as rx

import herramienta_analaizer.styles.styles as styles
from herramienta_analaizer.styles.styles import Size
from herramienta_analaizer.views.navbar import navbar

import openai
from openai import OpenAI


    




client=openai.OpenAI(api_key=api_gpt)



@rx.page(route="/generador", title="Generador de contenido AnalAITools")
def generador()->rx.components:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Generador de contenidos"
                    ),
                    rx.vstack(
                        rx.hstack(
                            tipo_contenido(),
                            rx.text(SelectTipoContenido.tipo_contenido),
                        ),
                        rx.hstack(
                            model(),
                            rx.text(SelectModel.model),
                        ),
                        rx.hstack(
                            estado_contenido(),
                            rx.text(SelectEstadoContenido.estado_contenido),
                                ),
                        rx.hstack(
                            slider_intro(),
                            rx.text(f" La temperatura es de: {SliderTemperature.value}"),
                        ),      
                        rx.hstack(
                            user_WP(),
                            rx.text(UserAPI.text),
                        ),
                        rx.hstack(
                            dominio_WP(),
                            rx.text(Dominio.text),
                            ),
                        rx.hstack(
                            password_WP(),
                            rx.text(TextPassword.text),
                            ),
                        rx.hstack(
                            blur_prompt(),
                            rx.text(TextPrompt.text),
                        ),
                        rx.hstack(
                            titleContenido(),
                            rx.text(Title.text),
                        ),
                    ),
                ),
        ),
    ),
)



class SelectModel(rx.State):
    model: str="gpt-3.5-turbo"
    
    @rx.event
    def change_model(self, model: str):
        """Cambio la selección del valor de model

        Args:
            value (str): Los valores son los diferentes modelos que tiene la posibilidad de escoger el usuario

        Returns:
            str: Nos devuelve el valor del modelo seleccionado
        """
        self.model=model
    
class SelectEstadoContenido(rx.State):
    estado_contenido: str ="draft"
    
    @rx.event
    def change_estado_contenido(self, estado_contenido: str):
        """Cambio la selección del valor de estado de contenido

        Args:
            value (str): Los valores son los diferentes estados de contenido que tiene la posibilidad de escoger el usuario

        Returns:
            str: Nos devuelve el valor del estado de contenido seleccionado
        """
        self.estado_contenido=estado_contenido
    
class SelectTipoContenido(rx.State):
    tipo_contenido: str="posts"
    
    @rx.event
    def change_tipo_contenido(self, tipo_contenido: str):
        """Cambio la selección del valor de tipo de contenido

        Args:
            value (str): Los valores son los diferentes tipos de contenido que tiene la posibilidad de escoger el usuario

        Returns:
            str: Nos devuelve el valor del tipo de contenido seleccionado
        """
        self.tipo_contenido=tipo_contenido

class SliderTemperature(rx.State):
    value: float=0.5
    
    @rx.event
    def set_end(self, value: list[float]):
        self.value=value[0]
        
def slider_intro():
    return rx.vstack(
        rx.heading("Selector de temperatura"),
        rx.slider(on_value_commit=SliderTemperature.set_end,
                custom_attrs={"step":0.1},
                min=0,
                max=1),
        width="100%"
    )
    
class SliderMaxTokens(rx.State):
    value: int= 750
    
    @rx.event
    def set_end(self, value: list[int]):
        self.value=value[0]
        
def slider_max_token():
    return rx.vstack(
        rx.heading("Selector de tokens aproximados para usar"),
        rx.slider(on_value_commit=SliderMaxTokens.set_end),
        width="100%"
    )
    
class UserAPI(rx.State):
    text: str="Mi usuario de Rest API de WordPress"
    
def user_WP():
    return rx.vstack(
        rx.input(
            placeholder="introduce aquí tu nombre de usuario de REST API de Wordpress",
            default_value=UserAPI.text,
            value=UserAPI.text,
            on_change=UserAPI.set_text,
            required=True,
        ),
    )
    
class Dominio(rx.State):
    text: str = "Mi dominio de WP"

def dominio_WP():
    return rx.vstack(
        rx.input(
            placeholder="Introduce aquí el dominio de tu WP",
            default_value=Dominio.text,
            value=Dominio.text,
            on_change=Dominio.set_text,
            on_blur=Dominio.set_text,
            required=True,
        ),
    )
    
class Title(rx.State):
    text: str 
    
def titleContenido():
    return rx.vstack(
        rx.input(
            placeholder="Seleccionando el título de mi contenido",
            value= Title.text,
            on_change=Title.set_text,
            required=True,
        ),
    )

class TextPrompt(rx.State):
    text: str = ""
    
def blur_prompt():
    return rx.vstack(
        rx.text_area(
            placeholder="Escirbe aquí tu prompt",
            default_value=TextPrompt.text,
            size="2",
            value=TextPrompt.text,
            on_change=TextPrompt.set_text,
            on_blur=TextPrompt.set_text,
            resize="both",
            radius="large",
            # autofocus=True,
        )
    )

class TextPassword(rx.State):
    text: str
    
def password_WP():
    return rx.vstack(
        rx.input(
            placeholder="Escribe la contraseña de la cuenta de WordPress",
            default_value=TextPassword.text,
            value=TextPassword.text,
            on_change=TextPassword.set_text,
            on_blur=TextPassword.set_text,
            type="password",
            required=True                
        ),
    )
    
def model():
    return rx.center(
        rx.select(
            ["gpt-3.5-turbo", "gpt-4"],
            value=SelectModel.model,
            on_change=SelectModel.change_model,
            required=True,
        ),
    )

def tipo_contenido():
    return rx.center(
        rx.select(
            ["posts", "pages"],
            value=SelectTipoContenido.tipo_contenido,
            on_change=SelectTipoContenido.change_tipo_contenido,
            required=True,
        ),
    )

def estado_contenido():
    return rx.center(
        rx.select(
            ["draft", "publish", "pending", "private"],
            value=SelectEstadoContenido.estado_contenido,
            on_change=SelectEstadoContenido.change_estado_contenido,
        ),
    )
    
class TextAPIKeyGPT(rx.State):
    text: str
    
def password_GPT():
    return rx.vstack(
        rx.input(
            placeholder="Escribe la contraseña de la cuenta de OpenAI",
            default_value=TextAPIKeyGPT.text,
            value=TextAPIKeyGPT.text,
            on_change=TextAPIKeyGPT.set_text,
            on_blur=TextAPIKeyGPT.set_text,
            type="password",
            required=True                
        ),
    )
    
@rx.background
async def generate_content(self, model, prompt, temperature=SliderTemperature.value, max_tokens=SliderMaxTokens.value):
    async with self:
        generate_content = ""
        try:
            stream = client.chat.completions.create(
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