import openai

from tools_generador.tokens_gpt import SliderMaxTokens
from tools_generador.temperature_gpt import SliderTemperature
from tools_generador.prompts import Contenidos
from tools_generador.model_gpt import SelectModel
from tools_generador.password_ai import Passwords

def generate_content(model: str, prompt: str, max_tokens: int = 750, temperature: float = 0.7, stream: bool = False) -> str:
    """
    Genera contenido usando el modelo de OpenAI.

    Args:
        model (str): Modelo a usar (por ejemplo, "gpt-4").
        prompt (str): Prompt de entrada.
        max_tokens (int): Número máximo de tokens en la respuesta.
        temperature (float): Nivel de creatividad.
        stream (bool): Si debe usarse streaming.

    Returns:
        str: El texto generado.
    """
    client=openai.OpenAI(api_key=Passwords.password_gpt)
    try:
        if stream:
            # Manejamos el caso de streaming
            content = ""
            response = openai.chat.completions.create(
                model=SelectModel.model,
                messages=[{"role": "user", "content": Contenidos.prompt}],
                max_tokens=SliderMaxTokens.slider,
                temperature=SliderTemperature.temperature,
                stream=True,
            )
            content = "".join(
                chunk["choices"][0].get("delta", {}).get("content", "") for chunk in response
            )
            return content.strip()
        else:
            # Sin streaming
            response = openai.chat.completions.create(
                model=SelectModel.model,
                messages=[{"role": "user", "content": Contenidos.prompt}],
                max_tokens=SliderMaxTokens.slider,
                temperature=SliderTemperature.temperature,
            )
            return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generando el contenido: {e}"
    except openai.APIConnectionError as e:
        print('No se ha podido conectar con el servidor.')
    except openai.RateLimitError as e:
        print('Error status code 429 tiempo de espera sobrepasado, espera un poco y vuelve a intentarlo')
    except openai.APIStatusError as e:
        print(f"Se ha recibido otro status code que no es 200: {e}")
        
            