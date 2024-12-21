import reflex as rx

class SelectModel(rx.State):
    model: str="gpt-3.5-turbo"
        
    @rx.event
    def set_model(self, value: str):
        """Cambio la selección del valor de modelo

        Args:
            value (str): Los valores son los diferentes modelos que tiene la posibilidad de escoger el usuario

        Returns:
            str: Nos devuelve el valor del modelo seleccionado
        """
        self.model=value
        print(f"Modelo seleccionado: {self.model}")