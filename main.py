import requests
from bs4 import BeautifulSoup
import fake_useragent

session = requests.Session()
link = 'http://forum.ru-board.com/misc.cgi?action=login'
user = fake_useragent.UserAgent().random

header = {
    'User-Agent': user
}

data = {
    'action': 'dologin',
    'inmembername': 'Anto734',
    'inpassword': 'sdGzw3',
}

res = session.post(link, data=data, headers=header)
profile_info = 'http://forum.ru-board.com/profile.cgi'
profile_res = session.get(profile_info, headers=header).text


print(profile_res)



