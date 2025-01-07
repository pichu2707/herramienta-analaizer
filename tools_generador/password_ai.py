from dotenv import load_dotenv
import os

import reflex as rx

load_dotenv('.env')


class Passwords(rx.State):
    password_gpt: str
    
    @rx.event
    def set_password_gpt(self, value: str):
        self.password_gpt=os.getenv("TOKEN_OPENAI") #value
        print(f"la pass es: {self.password_gpt}")

