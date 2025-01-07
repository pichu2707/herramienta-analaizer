import reflex as rx

class SliderMaxTokens(rx.State):
    slider: int= 750
    

    def set_tokens(self, value: int):
        """Actualiza el valor del slider cuando el usuario confirma el cambio

        Args:
            value (int): Valor del número de tokens
        """
        self.slider=value
        print(f"los tokens seleccionados son {self.slider}")
