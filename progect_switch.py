import flet as ft
from custom_controls import Btn1, Btn2


class Project(ft.Container):
    def __init__(self, src, text, project_key, current_project_key, chane_project):
        super().__init__()
        self.border_radius = 12
        self.padding = ft.padding.symmetric(vertical=16, horizontal=16)
        self.bgcolor = '#ffffff'
        self.expand = True
        self.project_key = project_key
        self.chane_project = chane_project
        self.content = ft.Column(
            [
                ft.Image(src=src, height=40, width=40, border_radius=8),
                ft.Text(value=text, size=14, color='#000000'),
                self.btn(current_project_key),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        )

    def click(self):
        self.chane_project(self.project_key)

    def btn(self, current_project_key):
        if self.project_key == current_project_key:
            return Btn2(text='切换', on_click=None)
        else:
            return Btn1(text='切换', on_click=lambda e: self.click())


class ProjectSwitch(ft.Container):
    def __init__(self, current_project_key, chane_project):
        super().__init__()
        self.padding = ft.padding.symmetric(vertical=0, horizontal=16)
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        Project(
                            src='images/project_logo/Mico.png',
                            text='Mico',
                            project_key=0,
                            current_project_key=current_project_key,
                            chane_project=chane_project,
                        ),
                        Project(
                            src='images/project_logo/Xena.png',
                            text='Xena',
                            project_key=1,
                            current_project_key=current_project_key,
                            chane_project=chane_project,
                        ),
                        Project(
                            src='images/project_logo/YoHo.png',
                            text='YoHo',
                            project_key=2,
                            current_project_key=current_project_key,
                            chane_project=chane_project,
                        ),
                    ],
                    # expand=True
                ),
                ft.Row(
                    [
                        Project(
                            src='images/project_logo/ChatChill.png',
                            text='HiYoo',
                            project_key=3,
                            current_project_key=current_project_key,
                            chane_project=chane_project,
                        ),
                        Project(
                            src='images/project_logo/Dopa.png',
                            text='Dopa',
                            project_key=4,
                            current_project_key=current_project_key,
                            chane_project=chane_project,
                        ),
                        Project(src='images/project_logo/DramaBite.png',
                                text='DramaBite',
                                project_key=5,
                                current_project_key=current_project_key,
                                chane_project=chane_project,
                                ),
                    ],
                    # expand=True
                ),
                ft.Row(
                    [
                        Project(
                            src='images/project_logo/FalChat.png',
                            text='FalChat',
                            project_key=6,
                            current_project_key=current_project_key,
                            chane_project=chane_project,
                        ),
                        Project(
                            src='images/project_logo/Mico.png',
                            text='TopTop',
                            project_key=7,
                            current_project_key=current_project_key,
                            chane_project=chane_project,
                        ),
                        ft.Container(expand=True)
                    ],
                    # expand=True
                )
            ],
        )

# def main(page: ft.Page):
#     page.add(ProjectSwitch())
#
#
# ft.app(target=main, assets_dir='./assets')
