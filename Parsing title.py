import requests
from bs4 import BeautifulSoup
user_id = 1234567
url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/1/#list' % (user_id)
head = {
	'Cookie': '*secret information*',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

r = requests.get(url, headers = head)
r.encoding = 'utf-8'
src = r.text
parser = open('test.html', 'w', encoding="utf-8").write(src)
soup = BeautifulSoup(src, 'lxml')
title = soup.title.string
print(title)
