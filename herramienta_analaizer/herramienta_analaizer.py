import reflex as rx

import herramienta_analaizer.styles.styles as styles
from herramienta_analaizer.styles.styles import Size
from herramienta_analaizer.views.navbar import navbar
from herramienta_analaizer.views.header import header
from herramienta_analaizer.page.herramienta_generador import generador

from rxconfig import config


def index() -> rx.Component:
    return rx.box(
        navbar(),
        header(),
    )

def generador()->rx.Component:
    return rx.box(
        navbar(),
        generador(),
        
    )
    
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index,
            title="Herramientas AnalAITools",
            description="Tenemos las herramientas que vayan siendo necesarias para los trabajos de Analítica")
