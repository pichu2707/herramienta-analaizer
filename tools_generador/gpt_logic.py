import openai
from tools_generador.tokens_gpt import SliderMaxTokens
from tools_generador.temperature_gpt import SliderTemperature
from tools_generador.prompts import Contenidos
from tools_generador.model_gpt import SelectModel
from tools_generador.password_ai import Passwords
import reflex as rx

def generate_content(model: str, prompt: str, max_tokens: int, temperature: float, stream: bool = False) -> str:
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
    
    model = rx.cond(model ,model , SelectModel.model)
    prompt = rx.cond(prompt, prompt , Contenidos.prompt)
    max_tokens = rx.cond( max_tokens, max_tokens , SliderMaxTokens.slider)
    temperature = rx.cond(temperature, temperature , SliderTemperature.temperature)

    
    # Configuración de la API Key
    # if not Passwords.password_gpt:
    #     return "Error: La API Key no está configurada. Por favor, introdúcela antes de usar la función."

    openai.api_key = Passwords.password_gpt

    try:
        if stream:
            # Modo de streaming
            response = openai.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
                stream=True,
            )
            content = ""
            for chunk in response:
                if "choices" in chunk and chunk["choices"][0].get("delta", {}).get("content"):
                    content += chunk["choices"][0]["delta"]["content"]
                    print(content)
            return content.strip()
        else:
            # Modo sin streaming
            response = openai.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response["choices"][0]["message"]["content"].strip()
        
        
    except openai.APIConnectionError:
        return 'Error: No se ha podido conectar con el servidor. Verifica tu conexión a Internet.'
    except openai.RateLimitError:
        return 'Error: Tiempo de espera sobrepasado (código 429). Espera un momento e inténtalo de nuevo.'
    except openai.APIError as e:
        return f"Error de la API: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"

# Función para el botón y manejo del estado
def content_button():
    class ContentState(rx.State):
        generated_content: str = ""

        
        def trigger_content_generation(self, cls, value):
            cls.generated_content = generate_content(
                model=SelectModel.model,
                prompt=Contenidos.prompt,
                max_tokens=SliderMaxTokens.slider,
                temperature=SliderTemperature.temperature,
            )
            print(self.generated_content)
            self.generated_content=value
