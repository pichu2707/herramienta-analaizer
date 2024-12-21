import reflex as rx
class Passwords(rx.State):
    password_gpt: str
    
    @rx.event
    def set_password_gpt(self, value: str):
        self.password_gpt=value
        print(f"{self.password_gpt}")

