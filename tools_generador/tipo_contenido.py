import reflex as rx

class SelectTipoContenido(rx.State):
    tipo_contenido: str="posts"
    
    
    def change_tipo_contenido(self, value: str):
        """Cambio la selección del valor de tipo de contenido

        Args:
            value (str): Los valores son los diferentes tipos de contenido que tiene la posibilidad de escoger el usuario

        Returns:
            str: Nos devuelve el valor del tipo de contenido seleccionado
        """
        self.tipo_contenido=value
        print(f"el tipo de contenido es: {self.tipo_contenido}")