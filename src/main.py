import flet as ft
from nav import Nav
from page1_install import InstallMenu
from page2 import Page2


class MainPage(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.bgcolor = "F7F9FC"
        self.expand = True
        self.content = ft.Row(
            [
                Nav(self.build_content, page), InstallMenu(),
            ],
            spacing=0,
            expand=True,
        )

    def build_content(self, index):
        match index:
            case 0:
                self.content.controls[1] = InstallMenu()
                self.update()
            case 1:
                self.content.controls[1] = Page2()
                self.update()


def main(page: ft.Page):
    page.title = 'UI工具箱'
    page.padding = 0
    page.spacing = 0
    # page.theme = ft.Theme.li

    # page.window_width = 750
    # page.window_height = 500

    page.add(MainPage(page))


ft.app(target=main, assets_dir='../assets/')
