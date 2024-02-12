from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

cServ = wd.ChromeService('C:/Users/user/chromedriver-win64/chromedriver.exe')
browser = wd.Chrome(service = cServ)
browser.get('https://www.kinopoisk.ru')

search = browser.find_element(By.NAME, 'kp_query')
search.send_keys("Эмили в Париже")
search.send_keys(Keys.ENTER)
browser.implicitly_wait(3)

soup = BeautifulSoup(browser.page_source, 'lxml')
all_publications = soup.find_all('div', class_='search_results')

for link in all_publications:
    href = link.a.get('href')
    print('www.kinopoisk.ru'+href)