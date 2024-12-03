import openai
from openai import OpenAI
from tools_generador.tokens_gpt import SliderMaxTokens
from tools_generador.temperature_gpt import SliderTemperature
from tools_generador.config import TOKEN_OPENAI
from tools_generador.promts import Contenidos


class GPTLogic:
    def __init__(self, api_key: str = TOKEN_OPENAI):
        """
        Inicializa la clase con la clave API de OpenAI.
        """
        self.api_key = api_key
        openai.api_key = api_key

    def generate_content(self, model: str, prompt: str, max_tokens: int = 750, temperature: float = 0.7, stream: bool = False) -> str:
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
        try:
            if stream:
                # Manejamos el caso de streaming
                content = ""
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stream=True,
                )
                for chunk in response:
                    delta_content = chunk["choices"][0].get("delta", {}).get("content", "")
                    content += delta_content
                    print(delta_content, end="")  # Imprime en tiempo real
                return content.strip()
            else:
                # Sin streaming
                response = openai.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
                return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generando el contenido: {e}"

        except Exception as e:
            return f"Error generando el contenido: {e}"
        except openai.APIConnectionError as e:
            print('No se ha podido conectar con el servidor.')
        except openai.RateLimitError as e:
            print('Error status code 429 tiempo de espera sobrepasado, espera un poco y vuelve a intentarlo')
        except openai.APIStatusError as e:
            print(f"Se ha recibido otro status code que no es 200: {e}")
            
            