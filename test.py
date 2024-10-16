import flet as ft
import base64
from custom_controls import ToolAnimation


def load_lottie(src):
    with open(src, "r", encoding="utf-8") as json_file:
        json_data = json_file.read()
        json_base64 = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    return json_base64


bg_loop = load_lottie(src='assets/lottie/bg_loop.json')
tool_loop = load_lottie(src='assets/lottie/tool_loop.json')
tool_done = load_lottie(src='assets/lottie/tool_done.json')


def main(page: ft.Page):
    a = ToolAnimation()
    # def change_lottie(e):
    #     page.controls[0].src_base64 = tool_done
    #     page.controls[0].repeat = False
    #     print(page.controls[0].src_base64)
    #     page.controls[0].update()

    page.add(
        a,
        ft.ElevatedButton(text='change', on_click=lambda e: a.change_animation(0)),
        ft.ElevatedButton(text='change', on_click=lambda e: a.change_animation(1)),
        ft.ElevatedButton(text='change', on_click=lambda e: a.change_animation(2)),
    )


ft.app(target=main, assets_dir="assets")
