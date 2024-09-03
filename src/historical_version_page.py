import flet as ft

from custom_controls import Btn1
from get_lise_download import get_list


class ProjectCellList(ft.Container):
    def __init__(self, time, build_id, download_link):
        super().__init__()
        self.time = time
        self.build_id = build_id
        self.download_link = download_link
        self.border_radius = 12
        self.padding = ft.padding.symmetric(vertical=12, horizontal=16)
        self.bgcolor = '#ffffff'
        self.content = ft.Row(
            [
                ft.Image(src='images/project_logo/ChatChill.png', height=40, width=40),
                ft.Row([
                    ft.Column(
                        [
                            ft.Text(value=f'ChatChill{self.build_id}', size=14, color='#000000'),
                            ft.Text(value=self.time, size=12, color='#4d4d4d')
                        ]
                    ),
                ], expand=True),
                Btn1(text='安装', on_click=None),
            ]
        )


class ProjectList(ft.Container):
    def __init__(self):
        super().__init__()
        # 从网络获取项目列表
        self.project_list = get_list()
        # 将列表存入变量
        self.controls = self.add_row()
        # 将列表装入容器
        self.content = ft.Column(controls=self.controls, scroll=ft.ScrollMode.AUTO)

        self.padding = ft.padding.symmetric(vertical=0, horizontal=16)

    def add_row(self):
        # 创建空列表
        items = []
        # 循环项目列表并创建ft实例
        for project in self.project_list:
            items.append(
                ProjectCellList(build_id=project['build_id'], time=project['time'],
                                download_link=project['download_link']))
        return items
