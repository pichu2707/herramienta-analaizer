import reflex as rx

class DatosWP(rx.State):
    passwpord_wp: str
    dominio_wp: str
    user_wp: str
    title_wp: str

    #Definiendo los datos de la web
    def set_dominio_wp(self, value: str):
        self.dominio_wp=value
        print(f"Dominio introducido: {self.dominio_wp}")
    
    def set_password_wp(self, value: str):
        self.passwpord_wp=value
        print(f"password introducida: {self.passwpord_wp}")
    
    def set_user_wp(self, value: str):
        self.user_wp=value
        print(f"Usuario modificado: {self.user_wp}")
    
    def set_title_wp(self, value: str):
        self.title_wp=value
        print(f"Título introducido: {self.title_wp}")
