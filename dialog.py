import flet as ft
import threading
import time


class Notification:
    def __init__(self, page, message: str, duration: int = 3):
        """
        初始化通知对象
        :param page: Flet 页面对象
        :param message: 通知消息文本
        :param duration: 通知显示时长（秒）
        """
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
            animate_opacity=200,  # 设置透明度动画时长
            animate_offset=ft.animation.Animation(duration=200, curve=ft.AnimationCurve.EASE),  # 设置位置动画时长和效果
            height=48,
            alignment=ft.alignment.center,
            margin=24,
        )

    def show(self):
        """显示通知"""

        # 添加通知容器到页面 overlay 中
        self.page.overlay.append(self.notification)
        self.page.update()  # 确保控件已添加到页面

        # 延时调用动画效果
        def animate_show():
            self.notification.offset = ft.transform.Offset(0, 0)  # 移动到顶部
            self.notification.opacity = 1.0  # 设置为不透明
            self.notification.update()  # 更新通知控件

        # 启动动画显示
        threading.Timer(0.1, animate_show).start()

        # 在子线程中等待指定时间后隐藏通知
        def hide_after_delay():
            try:
                time.sleep(self.duration)  # 等待指定的秒数

                # 隐藏通知
                def animate_hide():
                    self.notification.offset = ft.transform.Offset(0, -1)
                    self.notification.opacity = 0.0
                    self.notification.update()  # 更新通知控件
                    time.sleep(0.3)  # 等待动画完成
                    self.page.overlay.remove(self.notification)  # 从页面移除通知
                    self.page.update()  # 更新页面
                    self.dispose()  # 销毁 Notification 实例

                # 启动隐藏动画
                threading.Timer(0.1, animate_hide).start()
            except RuntimeError:
                pass

        # 启动一个子线程来隐藏通知，以免阻塞主线程
        thread = threading.Thread(target=hide_after_delay)
        thread.daemon = True  # 将线程设为守护线程，当程序退出时结束线程
        thread.start()

    def dispose(self):
        """清理对象的引用，便于垃圾回收"""
        self.page = None
        self.notification = None


# def main(page: ft.Page):
#     # 定义按钮的点击事件，点击时显示通知
#     def on_button_click(e):
#         notification = Notification(page, "这是一个通知消息", duration=3)
#         notification.show()
#
#     # 创建按钮并将其添加到页面
#     show_button = ft.ElevatedButton("显示通知", on_click=on_button_click)
#     page.add(show_button)
#
#
# ft.app(target=main)
