import reflex as rx
from tools_generador.gpt_logic import GPTLogic
from tools_generador.wordpress import DatosWP
from tools_generador.config import TOKEN_OPENAI

class AppState(rx.State):
    api_key: str = TOKEN_OPENAI
    prompt: str = ""
    model: str = "gpt-4"
    max_tokens: int = 750
    temperature: float = 0.7
    content: str = ""
    status_message: str = ""
    generated_content: str = ""


    def set_prompt(value: str):
        """Actualiza el estado del prompt

        Args:
            value (str): Valor del prompt escrito
        """
        
        AppState.prompt = str(value)# Actualiza el prompt
        print(f"Valor recibido en set_prompt {value}")



    def set_model(value: str):
        AppState.model = value  # Actualiza el modelo

    def generate_content(self):
        self.status_message = "Generando contenido..."
        try:
            gpt = GPTLogic(api_key=self.api_key)
            self.content = gpt.generate_content(
                model=self.model,
                prompt=self.prompt,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stream=False,
            )
            self.generated_content = self.content
            self.status_message = "Contenido generado correctamente."
        except Exception as e:
            self.status_message = f"Error generando el contenido: {str(e)}"
