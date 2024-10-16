import urllib.request
import ssl
from lxml import etree

url = 'https://apphost.micoworld.net/apps/24/plats/48'

headers = {'User-Agent': 'Mozilla/5.0 (Windows'}

req = urllib.request.Request(url, headers=headers)

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

response = urllib.request.urlopen(req, context=context)

content = response.read().decode('utf-8')

tree = etree.HTML(content)

app_list = tree.xpath("//div[@class = 'col-md-12 cell']")

# for apps in div_list:
#
#
# print(div_list)
