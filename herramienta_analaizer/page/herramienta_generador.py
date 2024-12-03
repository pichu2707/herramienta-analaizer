import reflex as rx

from tools_generador.model_gpt import SelectModel, model
from tools_generador.estado_contenido import estado_contenido
from tools_generador.tipo_contenido import tipo_contenido
from tools_generador.tokens_gpt import SliderMaxTokens, slider_max_token
from tools_generador.temperature_gpt import SliderTemperature, slider_intro
from tools_generador.wordpress import DatosWP, dominio_WP, password_WP, user_WP, title_WP
from tools_generador.password_ai import password_GPT
from tools_generador.promts import Contenidos
from tools_generador.gpt_logic import GPTLogic

import herramienta_analaizer.styles.styles as styles
from herramienta_analaizer.styles.styles import Size
from herramienta_analaizer.views.navbar import navbar
from tools_generador.config import TOKEN_OPENAI
    


class AppState(rx.State):
    api_key: str = TOKEN_OPENAI
    user: str = ""
    password: str = ""
    dominio: str = ""
    title: str = ""
    tipo_contenido: str = "posts"
    estado_contenido: str = "draft"
    model: str = "gpt-4"  # Modelo por defecto
    temperature: float = 0.7
    max_tokens: int = 750
    prompt: str = Contenidos.generate_final_prompt()
    print(f"prompt de listado: {prompt}")
    content: str = ""
    status_message: str = ""
    generated_content: str = ""
    post_status: str =""
    
    #Generar el contenido con GPT
    
    def generate_content(self):
        self.status_message = "Generando contenido..."
        try:
            gpt = GPTLogic(api_key=self.api_key)
            print(f"Usando modelo: {self.model}, prompt: {self.prompt}")
            self.content = gpt.generate_content(
                model=self.model,
                prompt=self.prompt,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stream=False,
            )
            print(f"Contenido generado: {self.content}")
            self.generated_content = self.content
            self.status_message = "Contenido generado correctamente."
        except Exception as e:
            print(f"Error al generar el contenido: {e}")
            self.status_message = f"Error generando el contenido: {e}"

    def publish_content(self):
        if not all([self.user, self.password, self.dominio, self.title, self.content]):
            self.status_message = "Por favor, completa todos los campos obligatorios."
            return
        self.status_message = "Publicando contenido..."
        try:
            print("Publicando contenido en WordPress...")
            self.status_message = post_to_wordpress(
                title=self.title,
                estado_contenido=self.estado_contenido,
                content=self.content,
                dominio=self.dominio,
                user=self.user,
                password=self.password,
                tipo_contenido=self.tipo_contenido,
            )
            print(f"Resultado de publicación: {self.status_message}")  
        except Exception as e:
            print(f"Error al publicar contenido: {e}")
            self.status_message = f"Error al publicar contenido: {e}"
        
@rx.page(route="/generador", title="Generador de contenido AnalAITools")
def generador()->rx.components:
    return rx.vstack(
                navbar(),
            rx.vstack(
                #Datos de WP
                rx.heading("Configuraciones de WP"),
                dominio_WP(),
                user_WP(),
                password_WP(),
                title_WP(),
                
                rx.heading("Configuración de tokens"),
                slider_max_token(),
                
                #Configuración inicial
                rx.heading("Generar el contenido", size=Size.BIG.value),
                rx.text_area(
                    placeholder="Introduce aquí la configuración de tu prompt",
                    on_blur=lambda value:AppState.set_prompt(value),
                    default_value=Contenidos.generate_final_prompt(),
                ),
                rx.button("Generar el contenido",
                        on_click=AppState.generate_content,
                        ),
                rx.text(AppState.generated_content),
                
                #Selector de modelos de GPT
                rx.heading("Selecciona el tipo de página"),
                model(),
                tipo_contenido(),
                estado_contenido(),
                ),
            
            #Publicar el contenido
            rx.heading("Publicar el contenido en WP"),
            rx.button("Publicar el contenido",
                    on_click=AppState.publish_content,
                    ),
            rx.text(AppState.post_status),
    ),
    


