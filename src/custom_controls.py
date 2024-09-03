import flet as ft
from config import color


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


class Btn1(ft.Container):
    def __init__(self, text, on_click):
        super().__init__()
        # self.expand = True
        self.text = text
        self.padding = ft.padding.all(4)
        self.width = 64
        self.height = 32
        self.border_radius = 8
        self.alignment = ft.alignment.center
        self.on_click = on_click
        self.bgcolor = color['light']['button_bg1']
        self.content = ft.Text(value=self.text, size=12, color=color['light']['button_text1'], )


class Btn2(ft.Container):
    def __init__(self, text, on_click):
        super().__init__()
        # self.expand = True
        self.visible = True if text else False
        self.text = text
        self.padding = ft.padding.all(4)
        self.width = 64
        self.height = 32
        self.border_radius = 8
        self.alignment = ft.alignment.center
        self.on_click = on_click
        self.bgcolor = color['light']['button_bg2']
        self.content = ft.Text(value=self.text, size=12, color=color['light']['button_text2'], )


class CustomCell(ft.Container):
    def __init__(self, icon_src, title, text, btn1_text=None, btn2_text=None, on_click_btn1=None, on_click_btn2=None):
        super().__init__()

        # 设置组件属性
        self.padding = ft.padding.symmetric(vertical=16, horizontal=0)
        self.bgcolor = '#ffffff'
        self.expand = True
        self.border_radius = 8

        # 直接使用参数来创建内容
        self.content = ft.Column(
            [
                ft.Image(src=icon_src, width=48, height=48),
                ft.Text(value=title, size=12, color='#000000'),
                ft.Text(value=text, size=12, color='#4d000000'),
                ft.Row(
                    [
                        Btn1(text=btn1_text, on_click=on_click_btn1),
                        Btn2(text=btn2_text, on_click=on_click_btn2),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=False,
        )


class BtnOutline(ft.ElevatedButton):
    def __init__(self, icon_src, text, on_click=None):
        super().__init__()
        self.on_click = on_click
        self.content = ft.Container(
            content=ft.Row(
                [
                    ft.Image(src=icon_src, width=16, height=16),
                    ft.Text(value=text, color='#787F8D')
                ]
            ),
            border=ft.border.all(width=1, color='#0d000000'),
            padding=ft.padding.symmetric(vertical=8, horizontal=8),
            border_radius=8,
        )
        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.symmetric(vertical=0, horizontal=0),
            elevation=0,
            color='#00000000',
            overlay_color='0d000000',
        )


class BtnBack(ft.ElevatedButton):
    def __init__(self, on_click):
        super().__init__()
        self.icon_src = 'images/page/back.svg'
        self.on_click = on_click
        self.width = 32
        self.height = 32
        self.content = ft.Container(
            content=ft.Image(src=self.icon_src),
            border=ft.border.all(width=1, color='#0d000000'),
            padding=ft.padding.symmetric(vertical=8, horizontal=8),
            border_radius=8,
        )
        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.symmetric(vertical=0, horizontal=0),
            elevation=0,
            color='#00000000',
            overlay_color='0d000000',
        )
