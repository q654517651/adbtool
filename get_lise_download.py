import urllib.request
import ssl
from lxml import etree

url = 'https://apphost.micoworld.net/apps/24/plats/48'
headers = {'User-Agent': 'Mozilla/5.0 (Windows'}


def get_list(url):
    apk_list = []
    req = urllib.request.Request(url, headers=headers)
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    response = urllib.request.urlopen(req, context=context)

    content = response.read().decode('utf-8')

    # 从网络获取html对象
    tree = etree.HTML(content)

    # 从本地加载html对象
    # parser = etree.HTMLParser(encoding='utf-8')
    # tree = etree.parse('48.html', parser=parser)

    div_list = tree.xpath("//div[@class = 'col-md-12 cell']")

    for div in div_list:
        time = div.xpath(".//span[@class = 'date-label tint-text']/text()")[0].strip()
        download_link = div.xpath(".//a[@class = 'download-btn']/@href")[0]
        build_id = div.xpath(".//span[@class = 'tint-text']/text()")[0]
        apk_dict = {'time': time, 'download_link': download_link, 'build_id': build_id}
        apk_list.append(apk_dict)

    return apk_list

# a = get_list(url)
# print(a)