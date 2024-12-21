import reflex as rx

from tools_generador.estado_contenido import SelectEstadoContenido
from tools_generador.tipo_contenido import SelectTipoContenido
from tools_generador.tokens_gpt import SliderMaxTokens
from tools_generador.temperature_gpt import SliderTemperature
from tools_generador.wordpress import DatosWP
from tools_generador.prompts import Contenidos
from tools_generador.model_gpt import SelectModel
from tools_generador.password_ai import Passwords
from tools_generador.gpt_logic import content_button


import herramienta_analaizer.styles.styles as styles
from herramienta_analaizer.styles.styles import Size
from herramienta_analaizer.views.navbar import navbar


@rx.page(route="/generador", title="Generador de contenido AnalAITools")
def generador():
    return rx.vstack(
        navbar(),
        
        rx.heading("Configuraciones de WP"),
        rx.input(
            placeholder="Introduce aquí el dominio de tu WordPress",
            on_blur=DatosWP.set_dominio_wp,  # Actualiza el estado
            required=True,
        ),
        
        rx.input(
            placeholder="Escribe la contraseña de tu cuenta de WordPress",
            on_blur=DatosWP.set_password_wp,  # Actualiza el estado
            type="password",
            required=True,
        ),
        
        rx.input(
            placeholder="Introduce aquí tu nombre de usuario",
            on_blur=DatosWP.set_user_wp,  # Actualiza el estado
            required=True,
        ),
        
        rx.input(
            placeholder="Introduce aquí el título de tu contenido",
            on_blur=DatosWP.set_title_wp,  # Actualiza el estado
            required=True,
        ),
        
        rx.heading("Selector de temperatura"),
        rx.text(f"Temperatura seleccionada: {SliderTemperature.temperature}"),
        rx.slider(
                on_value_commit=SliderTemperature.set_temperature,
                custom_attrs={"step":0.1},
                min=0,
                max=1,
                default_value=0.5,
        ),
        
        rx.select(
            ["gpt-3.5-turbo", "gpt-4", "gpt-4o","gpt-4o-mini"],
            value=SelectModel.model,
            on_change=SelectModel.set_model,
            required=True,
        ),
        
        rx.heading("Selector de tokens aproximados para usar"),
        rx.slider(
            min=500,
            max=2500,
            step=50,
            default_value=750,
            on_value_commit=SliderMaxTokens.set_tokens,
            ),
        
        rx.input(
            rx.heading("API Key de GPT"),
            placeholder="Escribe aquí la API Key de GPT",
            value=Passwords.password_gpt,
            on_change= Passwords.set_password_gpt,
            type="password",
            required=True,
            size="3",
            width="3"
        ),
        
        rx.select(
            ["draft", "publish", "pending", "private"],
            value=SelectEstadoContenido.estado_contenido,
            on_change=SelectEstadoContenido.change_estado_contenido,
        ),
        
        rx.input(
            placeholder="Escribe aquí tu prompt",
            on_blur=Contenidos.set_prompt,
        ),
        
        rx.select(
            ["posts", "pages"],
            value=SelectTipoContenido.tipo_contenido,
            on_change=SelectTipoContenido.change_tipo_contenido,
            required=True,
            
        ),
        
        # content_button(),
        )
        
    


