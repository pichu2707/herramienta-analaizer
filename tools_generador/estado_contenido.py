import reflex as rx

class SelectEstadoContenido(rx.State):
    estado_contenido: str ="draft"
    
    def change_estado_contenido(self, value: str):
        """Cambio la selección del valor de estado de contenido

        Args:
            value (str): Los valores son los diferentes estados de contenido que tiene la posibilidad de escoger el usuario

        Returns:
            str: Nos devuelve el valor del estado de contenido seleccionado
        """
        self.estado_contenido=value
        print(f"el estado de contenido es: {self.estado_contenido}")