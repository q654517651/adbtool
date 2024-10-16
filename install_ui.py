import flet as ft
from button import app_button
from config import color


def install_ui(page, visible):
    ui = ft.Column(
        [
            ft.Column([
                ft.Image(src=f'images/page/install_animation.png', width=240, height=240),
                update_text('一键安装最新测试包'),
            ],
                spacing=8,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            app_button(3, '一键安装最新', '')
        ],
        visible=visible,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        spacing=32,
    )

    return ui


def update_text(text):
    text = ft.Text(value=text, color=color['light']['text1'], size=16, font_family='微软雅黑')
    return text
