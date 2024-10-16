import flet as ft

from button import Btn3
from config import color
from custom_controls import BtnOutline, BtnBack, ToolAnimation
from historical_version_page import ProjectList
from progect_switch import ProjectSwitch
from download import download_apk


# 返回导航栏类 这个类接受一个切换页面的函数build_content
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


# 页面默认导航栏类，这个类接受一个切换页面的函数build_content，和当前项目名称 project_name
class Page1NavBar(ft.Container):
    def __init__(self, build_content, project_name):
        super().__init__()
        # 传入页面函数
        self.build_content = build_content
        self.padding = ft.padding.symmetric(vertical=0, horizontal=16)
        self.height = 56
        self.content = ft.Row([
            ft.Text(value=f'当前项目{project_name}', size=14),
            ft.Row([
                BtnOutline(
                    icon_src='images/page/history.svg',
                    text='历史包',
                    on_click=lambda e: self.build_content(1),
                ),
                BtnOutline(
                    icon_src='images/page/more.svg',
                    text='切换项目',
                    on_click=lambda e: self.build_content(2),
                )
            ]),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, )


# 安装apk页面类
class InstallPage(ft.Container):
    def __init__(self, src):
        super().__init__()
        self.expand = True
        self.tool_animation = ToolAnimation()
        self.content = ft.Row([ft.Column([
            # ft.Image(src=f'images/page/install_animation.png', width=240, height=240),
            self.tool_animation,
            ft.Text(value='text', color=color['light']['text1'], size=16, font_family='微软雅黑'),
            Btn3('一键安装最新',
                 lambda e: download_apk(src, self.update_download_state, self.tool_animation.change_animation)),
        ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        )], expand=True)

    def update_download_state(self, text):
        # print(self.content.controls[0].controls[1].value)
        self.content.controls[0].controls[1].value = text
        self.content.controls[0].controls[1].update()


# 最终的页面类
class InstallMenu(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = '#F7F9FC'

        # 各个项目的代码以及排序
        # mico = 0
        # xena = 1
        # Yoho = 2
        # hiyoo = 3
        # dopa = 4
        # dramabite = 5
        # falchat = 6
        # top  = 7

        # 当前项目key
        self.current_project_key = 0
        # 当前项目名称
        self.current_name = 'Mico'
        # 当前项目地址
        self.current_src = 'https://apphost.micoworld.net/apps/4/plats/3'
        # 页面结构
        self.content = ft.Column([
            Page1NavBar(self.build_content, self.current_name),
            InstallPage(self.current_src),
        ])

    def build_content(self, index):
        match index:
            case 0:
                self.content.controls[0] = Page1NavBar(self.build_content, self.current_name)
                self.content.controls[1] = InstallPage(self.current_src)
                self.update()
            case 1:
                self.content.controls[0] = Page1BackBar(self.build_content)
                self.content.controls[1] = ProjectList(index=self.current_project_key, url=self.current_src)
                self.update()
            case 2:
                self.content.controls[0] = Page1BackBar(self.build_content)
                self.content.controls[1] = ProjectSwitch(self.current_project_key, self.change_project)
                self.update()

    # 根据索引切换当前项目 并变更索引值
    def change_project(self, index):
        match index:
            case 0:
                self.current_src = 'https://apphost.micoworld.net/apps/4/plats/3'
                # self.current_src = 'https://download.appmeta.cn/apps/66bb40dff94548480460330b/install?download_token=8ece1cd0bd67332ad6262e25e2d5973f'
                self.current_name = 'Mico'
                self.current_project_key = 0
            case 1:
                self.current_src = 'https://apphost.micoworld.net/apps/11/plats/13'
                self.current_name = 'Xena'
                self.current_project_key = 1
            case 2:
                self.current_src = 'https://apphost.micoworld.net/apps/18/plats/26'
                self.current_name = 'Yoho'
                self.current_project_key = 2
            case 3:
                self.current_src = 'https://apphost.micoworld.net/apps/20/plats/34'
                self.current_name = 'Hiyoo'
                self.current_project_key = 3
            case 4:
                self.current_src = 'https://apphost.micoworld.net/apps/23/plats/40'
                self.current_name = 'Dopa'
                self.current_project_key = 4
            case 5:
                self.current_src = 'https://apphost.micoworld.net/apps/24/plats/48'
                self.current_name = 'DramaBite'
                self.current_project_key = 5
            case 6:
                self.current_src = 'https://apphost.micoworld.net/apps/28/plats/80'
                self.current_name = 'FalChat'
                self.current_project_key = 6
            case 7:
                self.current_src = 'https://apphost.micoworld.net/apps/35/plats/96'
                self.current_name = 'TopTop'
                self.current_project_key = 7
        # print(self.current_project_key, self.current_name, self.current_src)
        self.build_content(0)

# def main(page: ft.Page):
#     page.add(InstallMenu())
#
#
# ft.app(target=main, assets_dir='./assets')
