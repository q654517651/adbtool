import threading
import flet as ft
import time
from adb_shell import AdbShell

adb_shell = AdbShell()


def is_adb_device_connected():
    result = adb_shell.check_devices()
    devices = result.stdout.strip().split('\n')[1:]
    return any(device.strip() for device in devices)


def monitor_adb_connection(page):
    connected = False
    while True:
        if is_adb_device_connected():
            if not connected:
                connected = True
                # page.controls[0].value = "ADB设备已连接"
                # page.update()
        else:
            if connected:
                connected = False
                # page.controls[0].value = "ADB设备已断开"
                # page.update()
        time.sleep(5)  # 每5秒检查一次连接状态


def main(page: ft.Page):
    page.title = "ADB连接监测"
    status_label = ft.Text("检测ADB设备连接状态中...")
    page.add(status_label)

    # 启动一个新线程来监测ADB连接状态
    monitor_thread = threading.Thread(target=monitor_adb_connection, args=(page,))
    monitor_thread.start()


ft.app(target=main)
