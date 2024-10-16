import flet as ft
import time

def main(page: ft.Page):
    c = ft.Container(
        width=150,
        height=150,
        opacity=1,
        bgcolor="blue",
        border_radius=10,
        offset=ft.transform.Offset(0, -2),
        animate_offset=ft.animation.Animation(duration=300, curve="easeOutCubic"),
        animate_opacity=ft.animation.Animation(duration=300, curve="easeOutCubic"),
    )

    def animate(e):
        page.open(control=c)

    page.add(
        c,
        ft.ElevatedButton("Reveal!", on_click=animate),
    )


ft.app(target=main)
