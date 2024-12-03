import reflex as rx

class DatosWP(rx.State):
    passwpord_wp: str
    dominio_wp: str
    user_wp: str
    title_wp: str

        #Definiendo los modelos
    def set_dominio_wp(self,value):
        self.dominio_wp=value
        
    def set_password_wp(self,value):
        self.passwpord_wp=value
        
    def set_user_wp(self,value):
        self.user_wp=value
        
    def set_title_wp(self, value):
        self.title_wp=value
        
    def procesar_datos(self):
        print(f"Dominio: {self.dominio_wp}")
        print(f"Usuario: {self.user_wp}")
        print(f"Contraseña: {self.passwpord_wp}")
        
        
def dominio_WP():
    return rx.vstack(
        rx.input(
            placeholder="Introduce aquí el dominio de tu WP",
            default_value=DatosWP.dominio_wp,
            value=DatosWP.dominio_wp,
            on_change=DatosWP.set_dominio_wp,
            on_blur=DatosWP.set_dominio_wp,
            required=True,
        ),
    )
        
def password_WP():
    return rx.vstack(
        rx.input(
            placeholder="Escribe la contraseña de la cuenta de WordPress",
            default_value=DatosWP.passwpord_wp,
            value=DatosWP.passwpord_wp,
            on_change=DatosWP.set_password_wp,
            on_blur=DatosWP.set_password_wp,
            type="password",
            required=True                
        ),
    )
    
def user_WP():
    return rx.vstack(
        rx.input(
            placeholder="introduce aquí tu nombre de usuario de REST API de Wordpress",
            default_value=DatosWP.user_wp,
            value=DatosWP.user_wp,
            on_change=DatosWP.set_user_wp,
            required=True,
        ),
    )
        
def title_WP():
    return rx.vstack(
        rx.input(
            placeholder="Introduce aquí el título de tu contenido",
            default_value=DatosWP.title_wp,
            value=DatosWP.title_wp,
            on_change=DatosWP.set_title_wp,
            required=True,
        ),
    )
