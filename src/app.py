import flet as ft
from src.adb_shell import AdbShell
from button import app_button
from config import color

adb_shell = AdbShell()


class InstallMenu(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = True,
        self.bgcolor = '#999999'
        self.content = ft.Column(
                [
                    ft.Column([
                        ft.Image(src=f'images/page/install_animation.png', width=240, height=240),
                        ft.Text(value='text', color=color['light']['text1'], size=16, font_family='微软雅黑')
                    ],
                        spacing=8,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    app_button(3, '一键安装最新', '')
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                spacing=32,
            )





def main(page: ft.Page):
    # page.expand = True
    a = ft.Row([ft.Text('1')],width=page.width,)
    page.add(
        a
    )
    print(a.width)


ft.app(
    target=main,
    assets_dir='../assets/',
)
