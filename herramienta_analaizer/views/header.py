import reflex as rx
import herramienta_analaizer.styles.styles as styles
from herramienta_analaizer.styles.styles import Size

def header()->rx.Component:
    return rx.vstack(
        rx.desktop_only(
            rx.heading(),
            rx.vstack(
                rx.hstack(
                    rx.card(
                        rx.link(
                            rx.flex(
                                rx.avatar(
                                    src="favi.png",
                                ),
                                rx.box(
                                    rx.heading("Creando tarjeta de primera herramienta"),
                                    rx.text("Esta es el texto de la tarjeta")
                                    ),

                                ),
                            spacing="2",
                            ),
                            size="6",
                        ),
                    as_child=True,
                    ),
                rx.hstack(                    rx.card(
                        rx.link(
                            rx.flex(
                                rx.avatar(
                                    src="favi.png",
                                ),
                                rx.box(
                                    rx.heading("Creando tarjeta de primera herramienta"),
                                    rx.text("Esta es el texto de la tarjeta")
                                    ),

                                ),
                            spacing="2",
                            ),
                            size="5",
                        ),
                    as_child=True,
                    ),
                ),
        ),
    )