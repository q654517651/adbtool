import os
import subprocess
import platform
from PIL import Image
import io
# from dialog import Notification

screenshot_path = os.path.join('', 'screenshot', 'screenshot.png')


def image_to_clipboard(image_path):
    file_url = f"file://{os.path.abspath(image_path)}"
    # 使用 macOS 的 "osascript" 命令将 PNG 图片复制到剪切板
    if check_platform() == 0:
        subprocess.run([
            "osascript", "-e",
            f'set the clipboard to (read (POSIX file "{file_url}") as «class PNGf»)'
        ])
    elif check_platform() == 1:
        import win32clipboard as clipboard
        # 打开图片并将其转换为BMP格式
        image = Image.open(image_path)
        output = io.BytesIO()
        image.convert('RGB').save(output, 'BMP')

        # 去掉BMP文件的前14个字节（DIB header不需要）
        bmp_data = output.getvalue()[14:]

        # 打开剪切板并将图片数据放入其中
        clipboard.OpenClipboard()
        clipboard.EmptyClipboard()
        clipboard.SetClipboardData(clipboard.CF_DIB, bmp_data)
        clipboard.CloseClipboard()


def check_platform():
    system_name = platform.system()
    if system_name == "Darwin":
        return 0
    elif system_name == "Windows":
        return 1


class AdbShell:
    def __init__(self):
        self.platform_id = check_platform()
        self.win_path = os.path.join('./', 'adb_environment', 'win', 'adb.exe')
        self.mac_path = os.path.join('./', 'adb_environment', 'mac', 'adb')
        # 0==macos  1==win
        self.path = self.win_path if self.platform_id == 1 else self.mac_path

    # 在使用adb shell setprop debug.layout true启用了显示布局边界之后
    # 我们必须戳戳SystemProperties以查看显示布局边界QS块所做的更改：

    def layout_boundaries_on(self):
        output = subprocess.run([self.path, 'shell', 'setprop debug.layout true'],
                                capture_output=True,
                                text=True)
        # print(output.stdout)
        output = subprocess.run([self.path, 'shell', 'service call activity 1599295570'], capture_output=True,
                                text=True)
        # print(output.stdout)

    def layout_boundaries_off(self):
        output = subprocess.run([self.path, 'shell', 'setprop debug.layout false'],
                                capture_output=True,
                                text=True)
        # print(output.stdout)
        output = subprocess.run([self.path, 'shell', 'service call activity 1599295570'],
                                capture_output=True,
                                text=True)
        # print(output.stdout)

    def check_devices(self):
        output = subprocess.run([self.path, 'devices'], capture_output=True, text=True)
        # print(output)
        # print(output.stdout)
        return output

    def apk_install(self):
        output = subprocess.run([self.path, 'install', 'apk/app.apk'],
                                capture_output=True,
                                text=True)
        print(output.stdout)

    def screenshot_pull(self):
        with open(screenshot_path, 'wb') as screenshot_file:
            subprocess.run([self.path, 'exec-out', 'screencap', '-p'], stdout=screenshot_file, check=True)
        image_to_clipboard(screenshot_path)

# a = AdbShell(0)
# a.apk_install()
# image_to_clipboard(screenshot_path)

# output = subprocess.run([mac_path, 'devices'], capture_output=True, text=True)
# print(output)
# args命令
# returncode 返回状态码
# stdout 终端输出
# stderr 执行结果
