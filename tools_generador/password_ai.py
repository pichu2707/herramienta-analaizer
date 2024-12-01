import reflex as rx

class Passwords(rx.State):
    password_gpt: str
        
    def password_GPT():
        return rx.vstack(
            rx.input(
                placeholder="Escribe la contraseña de la cuenta de OpenAI",
                default_value=Passwords.password_gpt,
                value=Passwords.password_gpt,
                on_change=Passwords.set_password_gpt,
                on_blur=Passwords.set_password_gpt,
                type="password",
                required=True                
            ),
        )
        