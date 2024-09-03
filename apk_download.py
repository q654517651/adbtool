import os
import requests
from urllib import request


def download_file(url, progress_ring):
    dest_folder = 'apk'
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = os.path.join(dest_folder, url.split("/")[-1])

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    downloaded_size = 0

    with open(filename, 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            downloaded_size += size
            progress_percent = round((downloaded_size / total_size), 2)
            progress_ring.value = progress_percent
