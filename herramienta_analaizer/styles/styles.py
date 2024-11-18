import reflex as rx
from reflex.style import set_color_mode, color_mode
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

def dark_mode_toggle()->rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        rx.segmented_control.item(
            rx.icon(tag="monitor", size=20),
            value="system",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )

MAX_WIDTH="1000px"

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"
    VERY_BIG="4em"
    LOGO_BIG="6em"
    
STYLESHEETS=[
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

BASE_STYLE={
    "font_family": Font.DEFAULT.value,
    "color": TextColor.ACCENT.value,
    "background":Color.PRIMARY.value,
    rx.heading:{
        "color":TextColor.ACCENT.value,
        "font_size":Size.MEDIUM.value,
        "_hover":{
            "color":Color.ACCENT.value,
        },
    },
    rx.flex:{
        "font_size":Size.SMALL.value,
    },
    
}


max_width_style= dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)