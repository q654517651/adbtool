import flet as ft
import asyncio

class Notification:
    def __init__(self, page, message: str, duration: int = 3):
        self.page = page
        self.message = message
        self.duration = duration

        # 创建通知的容器
        self.notification = ft.Container(
            content=ft.Text(self.message, color="white"),
            padding=10,
            bgcolor="blue",
            border_radius=5,
            opacity=0.0,  # 初始透明度为 0（不可见）
            offset=ft.transform.Offset(0, -1),  # 初始位置在页面顶部之外
            animate_opacity=300,  # 设置透明度动画时长
            animate_offset=ft.animation.Animation(duration=300, curve=ft.AnimationCurve.EASE),  # 设置位置动画时长和效果
            height=100,
            alignment=ft.alignment.top_center,
            margin=24,
        )

        # 添加通知容器到页面 overlay 中
        self.page.overlay.append(self.notification)

    async def show(self):
        """显示通知"""
        # 将通知移入页面并设置为完全不透明
        self.notification.offset = ft.transform.Offset(0, 0)
        self.notification.opacity = 1.0
        self.page.update()

        # 等待显示时长
        await asyncio.sleep(self.duration)
        await self.hide()

    async def hide(self):
        """隐藏通知"""
        # 将通知移回页面之外并设置为透明
        self.notification.offset = ft.transform.Offset(0, -1)
        self.notification.opacity = 0.0
        self.page.update()

def main(page: ft.Page):
    # 定义按钮的点击事件，点击时显示通知
    async def on_button_click(e):
        notification = Notification(page, "这是一个通知消息", duration=3)
        await notification.show()

    # 创建按钮并将其添加到页面
    show_button = ft.ElevatedButton("显示通知", on_click=lambda e: asyncio.run(on_button_click(e)))
    page.add(show_button)

ft.app(target=main)
