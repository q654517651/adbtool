import flet as ft
from config import color
from button import app_button, Btn3
from custom_controls import BtnOutline, BtnBack
from historical_version_page import ProjectList


class Page1BackBar(ft.Container):
    def __init__(self, build_content):
        super().__init__()
        self.build_content = build_content
        self.padding = ft.padding.symmetric(vertical=0, horizontal=16)
        self.height = 56
        self.content = ft.Row([
            BtnBack(on_click=lambda e: self.build_content(0))
        ],
            alignment=ft.MainAxisAlignment.START,
        )


class Page1NavBar(ft.Container):
    def __init__(self, build_content):
        super().__init__()
        self.build_content = build_content
        self.padding = ft.padding.symmetric(vertical=0, horizontal=16)
        self.height = 56
        self.content = ft.Row([
            ft.Text(value='当前项目', size=14),
            ft.Row([
                BtnOutline(
                    icon_src='images/page/history.svg',
                    text='历史包',
                    on_click=lambda e: self.build_content(1),
                ),
                BtnOutline(
                    icon_src='images/page/more.svg',
                    text='切换项目',
                    on_click=None,
                )
            ]),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, )


class InstallPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = ft.Row([ft.Column([
            ft.Image(src=f'images/page/install_animation.png', width=240, height=240),
            ft.Text(value='text', color=color['light']['text1'], size=16, font_family='微软雅黑'),
            Btn3('一键安装最新', None),
        ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        )], expand=True)


class InstallMenu(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = '#F7F9FC'
        self.content = ft.Column([
            Page1NavBar(self.build_content),
            InstallPage(),
        ])

    def build_content(self, index):
        match index:
            case 0:
                self.content.controls[0] = Page1NavBar(self.build_content)
                self.content.controls[1] = InstallPage()
                self.update()
            case 1:
                self.content.controls[0] = Page1BackBar(self.build_content)
                self.content.controls[1] = ProjectList()
                self.update()

# def main(page: ft.Page):
#     page.add(InstallPage())
#
#
# ft.app(target=main, assets_dir='../assets/')
