
import reflex as rx

from herramienta_analaizer.styles.styles import Size, Color, dark_mode_toggle
from herramienta_analaizer.components.link_icon import link_icon
import herramienta_analaizer.constants as constants

def navbar_icons_item(
        text: str, icon:str,url: str
        )->rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon,
                color=Color.ACCENT.value
                ),
            rx.text(text,
                size="4",
                weight="medium",
                color=Color.ACCENT.value
                ),
        ),
        href=url,
    )
    
def navbar_icons_menu_item(
    text: str, icon: str, url: str
    )->rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon,
                    size=Size.MEDIUM.value
                    ),
            rx.text(text,
                    size="3",
                    weight="medium"
                    ),
            href=url,
        )
    )
def navbar()->rx.Component:
    return rx.box( 
            rx.desktop_only(
                rx.hstack(
                    rx.hstack(
                        rx.image(
                            src="/logo.webp",
                            width="10em",
                        ),
                    align_center="center",
                ),
                    rx.hstack(
                        navbar_icons_item("Home", "home", "/#"),
                        navbar_icons_item(
                            "Generador Contenido", "book-open-check", "/generador"
                        ),
                        navbar_icons_item(
                            "Keywords", "file-key", "/#"
                        ),
                        navbar_icons_item(
                            "indexador", "list-plus", "/#"
                        ),
                        dark_mode_toggle(),
                        spacing="6",
                    ),
                    justify="between",
                    align_items="center",
                ),
                position="sticky",
                border_bottom=f"0.25em solid {Color.ACCENT.value}",
                padding_x=Size.BIG.value,
                padding_y=Size.SMALL.value,
                z_index="999",
                top="0",
                width="100%"
            ),
    ),
