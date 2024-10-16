import flet as ft
from config import color, icon_src, select_icon_src, nav_text


class NavCell(ft.Container):
    def __init__(self, img_src, selected_img_src, text, nav_cell_index, is_active, on_click):
        super().__init__()
        self.icon_src = img_src
        self.selected_icon_src = selected_img_src
        self.text = text
        self.is_active = is_active
        self.text_color = color['light']['text1']
        self.selected_text_color = color['light']['text2']
        self.font_family = '微软雅黑'

        self.data = nav_cell_index
        self.bg_color = color['light']['bgc2']
        self.selected_bg_color = color['light']['bgc1']
        self.border_radius = 12
        self.on_click = on_click
        self.width = 80
        self.height = 80

        self.bgcolor = self.set_bg_color()
        self.content = ft.Column(
            [
                ft.Image(
                    src=self.set_icon_src()
                ),
                ft.Text(value=self.text, color=self.set_text_color(), size=12, font_family=self.font_family),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

    def set_icon_src(self):
        if self.is_active:
            return self.selected_icon_src
        else:
            return self.icon_src

    def set_text_color(self):
        if self.is_active:
            return self.selected_text_color
        else:
            return self.text_color

    def set_bg_color(self):
        if self.is_active:
            return self.selected_bg_color
        else:
            return self.bg_color


class Nav(ft.Container):
    def __init__(self, build_content, page):
        super().__init__()
        self.select_index = 0
        self.nav = None
        self.content = self.side_nav()
        self.width = 128
        # self.height = page.height
        self.alignment = ft.alignment.center
        self.padding = ft.padding.only(top=16)
        self.bgcolor = color['light']['bgc2']
        self.build_content = build_content

    def build_content(self, index):
        # 调用传入的回调函数
        if self.build_content:
            self.build_content(index)

    def side_nav(self):
        def on_click(e):
            key = e.control.data
            self.select_index = key
            for index, cell in enumerate(self.nav.content.controls):
                cell.is_active = (index == key)
                cell.content.controls[0].src = cell.set_icon_src()
                cell.content.controls[1].color = cell.set_text_color()
                cell.bgcolor = cell.set_bg_color()
            self.build_content(self.select_index)
            self.update()

        self.nav = ft.Container(
            content=ft.Column(
                [
                    NavCell(
                        img_src=icon_src[0],
                        selected_img_src=select_icon_src[0],
                        text=nav_text[0],
                        nav_cell_index=0,
                        is_active=True if self.select_index == 0 else False,
                        on_click=on_click,
                    ),
                    NavCell(
                        img_src=icon_src[1],
                        selected_img_src=select_icon_src[1],
                        text=nav_text[1],
                        nav_cell_index=1,
                        is_active=True if self.select_index == 1 else False,
                        on_click=on_click,

                    ),
                ]
            )
        )
        return self.nav

# def main(page: ft.Page):
#     page.title = 'UI工具箱'
#     page.padding = 0
#
#     page.add(Nav())
#
#
# ft.app(target=main, assets_dir='../assets/')
