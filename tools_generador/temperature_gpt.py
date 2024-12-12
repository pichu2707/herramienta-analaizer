import reflex as rx

class SliderTemperature(rx.State):
    temperature: float=0.5
    
    def set_temperature(self, value: float):
        """Actualiza el valor de la temperatura al confirmar el cambio

        Args:
            value (float): Valor de temperatura del GPT que va desde 0.0 hasta 1
        """
        self.temperature=value
        print(f"el valor de temperatura es: {self.temperature}")
        