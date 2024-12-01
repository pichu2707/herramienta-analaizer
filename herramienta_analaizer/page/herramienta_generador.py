import requests
from requests.auth import HTTPBasicAuth
import json
import base64

import reflex as rx

from tools_generador.model_gpt import SelectModel, model
from tools_generador.estado_contenido import SelectEstadoContenido, estado_contenido
from tools_generador.tipo_contenido import SelectTipoContenido, tipo_contenido
from tools_generador.tokens_gpt import SliderMaxTokens, slider_max_token
from tools_generador.temperature_gpt import SliderTemperature, slider_intro
from tools_generador.wordpress import DatosWP, dominio_WP, password_WP, user_WP
from tools_generador.password_ai import Passwords
from tools_generador.promts import Contenidos

import herramienta_analaizer.styles.styles as styles
from herramienta_analaizer.styles.styles import Size
from herramienta_analaizer.views.navbar import navbar
    
@rx.page(route="/generador", title="Generador de contenido AnalAITools")
def generador()->rx.components:
    return rx.vstack(
                navbar(),
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        "Generador de contenidos"
                    ),
                    rx.vstack(                                    


                                # rx.vstack(
                                #     tipo_contenido(),
                                #     rx.text(SelectTipoContenido.tipo_contenido),
                                # ),
                                rx.vstack(
                                    model(),
                                    rx.text(SelectModel.model),
                                ),
                                rx.vstack(
                                    rx.button(
                                            "Generate Texto",
                                            type="submit",
                                            size="3",
                                            on_click=SelectModel.procesando_models,
                                            ),
                                    align="stretch",
                            ),
                                # rx.vstack(
                                #     estado_contenido(),
                                #     rx.text(SelectEstadoContenido.estado_contenido),
                                # ),
                                rx.vstack(
                                slider_max_token(),
                                ),      
                                rx.vstack(
                                    user_WP(),
                                ),
                                rx.vstack(
                                    dominio_WP(),
                                    ),
                                rx.vstack(
                                    password_WP(),
                                    ),
                                rx.vstack(
                                    slider_intro(),
                                ),
                                # rx.vstack(
                                #     Contenidos.blur_prompt(),
                                #     rx.text(Contenidos.promt),
                                # ),
                                # rx.vstack(
                                #     Contenidos.titleContenido(),
                                #     rx.text(Contenidos.title),
                                #     ),
                                # rx.vstack(
                                #     Passwords.password_GPT(),
                                # ),
                                
                                rx.vstack(
                                    rx.button(
                                            "Generate Texto",
                                            type="submit",
                                            size="3",
                                            on_click=DatosWP.procesar_datos,
                                            ),
                                    align="stretch",
                            ),
                                rx.vstack(
                                    rx.button(
                                            "Slider tokens",
                                            type="submit",
                                            size="3",
                                            on_click=SliderMaxTokens.procesado_datos,
                                            ),
                                    align="stretch",
                            ),
                                rx.vstack(
                                    rx.button(
                                            "Slider temperature",
                                            type="submit",
                                            size="3",
                                            on_click=SliderTemperature.procesando_datos,
                                            ),
                                    align="stretch",
                            ),
                    ),
                    
            ),
                    
        ),
    ),



