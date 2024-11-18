import reflex as rx


def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        rx.avatar(src=icon),
        href=url,
        is_external=True,
        target="_blank"
    )