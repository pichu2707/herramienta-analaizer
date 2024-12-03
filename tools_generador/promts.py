from tools_generador.config import TOKEN_OPENAI

import reflex as rx
import openai


promt_optimizacion="""
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

_client = None

def get_openai_client():
    global _client
    if _client is None:
        _client = openai.OpenAI(api_key=TOKEN_OPENAI)
    return _client

class Contenidos(rx.State):
    title: str = ""
    prompt: str = ""

    def set_promt(self, new_prompt: str):
        """Combina el nuevo texto ingresado por el usuario con el promp predefinido
        """
        predefinido = Contenidos.generate_final_prompt()
        self.prompt = f"{predefinido}\n{new_prompt.strip()}"
        print(f"Prompt actualizado: {self.prompt}")
        
        
    @staticmethod
    def title_contenido():
        return rx.vstack(
            rx.input(
                placeholder="Selecciona el título de tu contenido",
                value=Contenidos.title,
                on_change=Contenidos.set_title,
                required=True,
            ),
        )

    @staticmethod
    def blur_prompt():
        return rx.vstack(
            rx.text_area(
                placeholder="Escribe aquí tu prompt",
                default_value=Contenidos.prompt,
                value=Contenidos.prompt,
                on_change=Contenidos.set_prompt,
                on_blur=Contenidos.set_prompt,
                resize="both",
                radius="large",
            ),
        )

    @staticmethod
    @rx.event
    def generate_final_prompt():
        """
        Combina el prompt del usuario con el prompt de optimización.
        """
        final_prompt = f"{Contenidos.prompt.strip()} {promt_optimizacion.strip()}"
        return final_prompt