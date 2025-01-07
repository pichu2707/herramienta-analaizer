import reflex as rx

class Contenidos(rx.State):
    prompt: str = ""
    
    
    def set_prompt(self, value: str) -> str:
        """Combina el nuevo texto ingresado por el usuario con el promp predefinido
        """
        
        promt_optimizacion="""
        Si es necesario para poder dar un contexto a tu contenido. El HTML solo hay que crear la parte del <body>, lo demás ya lo tenemos creado con el contexto que te he pasado. Todo este
            contenido debe ser original y con al menos 1000 palabras. No me crees estilos tampoco y la parte de <H1> también obviala porque usamos WordPress y ya
            tenemos el título que hace de <H1> y así aprovechamos para un mayor contenido. La parte de <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Medidores de Campo para Instalación de Antenas de Televisión</title>
        </head> y el marcado de <body> también quítalo del código, ten en cuenta que ya estás empezando a subir el texto en el body de manera automática
            No te inventes nada. 
            Pásame el cóntenido con marcado HTML para poderlo súbir con el código directamente.
            Tambíen dame un comienzo y un final al artículo, no dejes frases sin acabar o sin contexto.
        """
        
        self.prompt = str(value + promt_optimizacion)
        print(self.prompt)


