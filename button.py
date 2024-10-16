import flet as ft
from config import color


class MyButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text


def app_button(button_type, text, on_click):
    if button_type == 1:
        button = ft.ElevatedButton(
            style=ft.ButtonStyle(
                color=color['light']['button_text1'],
                bgcolor=color['light']['button_bg1'],
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=4,
                elevation=0,
            ),
            width=64,
            height=32,
            on_click=on_click,
        )
        return button
    elif button_type == 2:
        button = ft.ElevatedButton(
            text=text,
            style=ft.ButtonStyle(
                color=color['light']['button_text2'],
                bgcolor=color['light']['button_bg2'],
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=4,
                elevation=0,
            ),
            width=64,
            height=32,
            on_click=on_click,
        )
        return button

    elif button_type == 3:
        button = ft.ElevatedButton(
            content=ft.Container(
                content=ft.Text(value=text, size=20),
            ),
            style=ft.ButtonStyle(
                color=color['light']['button_text1'],
                bgcolor=color['light']['button_bg1'],
                # padding=ft.padding.symmetric(20, 28),
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=ft.padding.only(left=40)
                # padding=12,
            ),
        )
        return button


class Btn3(ft.Container):
    def __init__(self, text, on_click):
        super().__init__()
        self.text = text
        self.padding = ft.padding.symmetric(vertical=12, horizontal=32)
        self.border_radius = 12
        self.bgcolor = '#367CFF'
        self.on_click = on_click
        self.margin = ft.margin.only(top=32)
        self.content = ft.Text(value=self.text, size=20, color=color['light']['button_text1'], )
        # print(self.bgcolor)


# def main(page: ft.Page):
#     page.title = 'UI工具箱'
#     page.padding = 0
#     page.spacing = 0
#     page.window_width = 750
#     page.window_height = 500
#
#     page.add(Btn3('一键安装最新', ''), )


# ft.app(target=main, assets_dir='../assets/')
