import flet as ft
import custom_controls
from adb_shell import AdbShell


class Page2(ft.Container):
    def __init__(self):
        super().__init__()
        self.adb = AdbShell(0)
        self.expand = True
        self.bgcolor = '#F7F9FC'
        self.padding = ft.padding.symmetric(horizontal=16, vertical=8)
        self.row1 = ft.Row([
            custom_controls.CustomCell(
                icon_src=f'images/page/layout.svg',
                title='布局边界开关',
                text='显示手机的布局边界',
                btn1_text='开启',
                on_click_btn1=lambda e: self.adb.layout_boundaries_on(),
                btn2_text='关闭',
                on_click_btn2=lambda e: self.adb.layout_boundaries_off(),
            ),
            custom_controls.CustomCell(
                icon_src=f'images/page/screenshot.svg',
                title='一键截图',
                text='截图当前页面并发送至剪切板',
                btn1_text='一键截图',
                on_click_btn1=lambda e: self.adb.screenshot_pull(),
            ),
            ft.Container(expand=True),
        ])
        self.content = ft.Column(
            [
                self.row1
            ]
        )

# def main(page: ft.Page):
#     page.add(Page2())
#
#
# ft.app(target=main, assets_dir='../assets/')
