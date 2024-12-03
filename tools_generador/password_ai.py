import reflex as rx

class Passwords(rx.State):
    password_gpt: str
    
    def set_password_gpt(self, value: str):
        self.password_gpt=value
        
    def procesando_pass_gpt(self):
        print(f"{self.password_gpt}")
        
def password_GPT():
    return rx.vstack(
        rx.input(
            rx.heading("API Key de GPT"),
            placeholder="Escribe aquí la API Key de GPT",
            default_value=Passwords.password_gpt,
            value=Passwords.password_gpt,
            on_change=Passwords.set_password_gpt,
            on_blur=Passwords.set_password_gpt,
            type="password",
            required=True                
        ),
    )
    