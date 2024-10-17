import os.path
import flet as ft
from nav import Nav
from page1_install import InstallMenu
from page2 import Page2
import subprocess



def ensure_adb_permissions(adb_path):
    # 检查 ADB 是否具有可执行权限
    if os.access(adb_path, os.X_OK):
        print(f"{adb_path} 已具有可执行权限。")
    else:
        try:
            subprocess.run(['chmod', '+x', adb_path], check=True)
            print(f"已设置 {adb_path} 的执行权限。")
        except subprocess.CalledProcessError as e:
            print(f"设置权限失败: {e}")


class MainPage(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.bgcolor = "F7F9FC"
        self.expand = True
        self.content = ft.Row(
            [
                Nav(self.build_content, page),

                InstallMenu(), Page2()

                # InstallMenu(),
            ],
            spacing=0,
            expand=True,
        )


    def build_content(self, index):
        # match index:
        #     case 0:
        #         self.content.controls[1] = InstallMenu()
        #         self.update()
        #     case 1:
        #         self.content.controls[1] = Page2()
        #         self.update()
        match index:
            case 0:
                self.content.controls[1].visible = True
                self.content.controls[2].visible = False
                self.update()
            case 1:
                self.content.controls[1].visible = False
                self.content.controls[2].visible = True
                self.update()


def main(page: ft.Page):
    ensure_adb_permissions(adb_path='./adb_environment/mac/adb')
    page.title = 'UI工具箱'
    page.padding = 0
    page.spacing = 0
    page.add(MainPage(page))


ft.app(target=main, assets_dir='assets/')
