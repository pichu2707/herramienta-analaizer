from tools_generador.model_gpt import SelectModel
from tools_generador.tokens_gpt import SliderMaxTokens
from tools_generador.temperature_gpt import SliderTemperature
from tools_generador.prompts import Contenidos
from tools_generador.password_ai import Passwords
from tools_generador.gpt_logic import generate_content
import reflex as rx

class MaterState(rx.State):
    result: str="" #almacenamos el contenido generdo
    wordpress_status: str="" #almacenamos el estado de la publicación de wordpress
    
    async def run_generate_content(self):
        """Recopila dastos de los estados y genera contenido con ellos"""
        
        model = SelectModel.model
        prompt = Contenidos.prompt
        max_tokens = SliderMaxTokens.slider
        temperature = SliderTemperature.temperature
        
        # if not (model and prompt and max_tokens and temperature):
        #     self.result = "Por favor, completa todas las configuraciones"
        #     return
        
        self.result=generate_content(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            )
        