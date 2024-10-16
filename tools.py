import flet as ft
from button import app_button


def tool_cell(img_src, text, btn1, btn2):
    cell = ft.Container(
        content=ft.Row(
            [
                ft.Image(src=img_src, width=40, height=40),
                ft.Container(
                    content=ft.Text(text),
                    expand=True,
                ),
                app_button(1, btn1, ''),
                app_button(2, btn2, ''),
            ],
            expand=True,
        ),
        bgcolor='#ffffff',
        padding=12,
        border_radius=8,
    )
    return cell


def tools(page, visible):
    page = ft.Container(
        content=ft.Column(
            [
                tool_cell(f'images/project_logo/ChatChill.png', 'ChatChill', '开启', '关闭')
            ]
        ),
        expand=True,
        visible=visible,
    )
    return page
