import time
import requests
from get_html_content import get_list
from adb_shell import AdbShell


def download_apk(url, update_download_state, change_animation):
    adb_shell = AdbShell(platform_id=0)
    print(f'收到项目地址{url}')
    output_path = './apk/app.apk'

    # 修改首页动画为安装中
    change_animation(1)

    try:
        project_url = get_list(url)[0]['download_link']
        print(f'收到下载地址{project_url}')

        # 发送GET请求获取文件内容
        response = requests.get(project_url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        # 获取文件的总大小（字节）
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        last_update_time = time.time()
        last_downloaded_size = 0

        # 以写入二进制文件的方式保存
        with open(output_path, 'wb') as apk_file:
            for data in response.iter_content(chunk_size=1024):
                if not data:
                    break  # 如果没有数据，退出循环

                apk_file.write(data)
                downloaded_size += len(data)

                # 计算当前进度
                progress = downloaded_size / total_size * 100

                # 获取当前时间
                current_time = time.time()
                time_diff = current_time - last_update_time

                # 每秒更新一次进度和下载速度
                if time_diff >= 1:
                    speed = (downloaded_size - last_downloaded_size) / time_diff
                    last_downloaded_size = downloaded_size

                    # 调用进度更新函数
                    update_progress(progress, speed, update_download_state)

                    last_update_time = current_time
                    print('更新下载速度')

        update_download_state('下载成功')
        adb_shell.apk_install()
        update_download_state('安装完成')

        change_animation(2)

    except requests.exceptions.RequestException as e:
        update_download_state(f'下载失败: {e}')
        change_animation(0)  # 设置为静止状态


def update_progress(progress, speed, update_download_state):
    update_download_state(text=f"当前下载进度: {progress:.2f}%, 下载速度: {speed / 1024:.2f} KB/s")
    print(f"当前下载进度: {progress:.2f}%, 下载速度: {speed / 1024:.2f} KB/s")

    # 在这里可以将 progress 和 speed 值传递给 Flet UI 控件

# download_apk(url='https://apphost.micoworld.net/uploads/pkg/file/19918/app-gp-alpha.apk')
