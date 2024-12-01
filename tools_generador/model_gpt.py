import reflex as rx

class SelectModel(rx.State):
    model: str="gpt-3.5-turbo"
        
    def change_model(self, value: str):
        """Cambio la selección del valor de model

        Args:
            value (str): Los valores son los diferentes modelos que tiene la posibilidad de escoger el usuario

        Returns:
            str: Nos devuelve el valor del modelo seleccionado
        """
        self.model=value
        
    def procesando_models(self):
        print(f"Modelo: {self.model}")
        

def model():
    return rx.center(
        rx.select(
            ["gpt-3.5-turbo", "gpt-4", "gpt-4o","gpt-4o-mini"],
            value=SelectModel.model,
            on_change=SelectModel.change_model,
            required=True,
        ),
        
    )