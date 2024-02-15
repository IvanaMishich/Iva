import requests
from bs4 import BeautifulSoup
user_id = 166905197
url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/1/#list' % (user_id)
head = {
	'Cookie': 'profile_button=main; gdpr=0; _ym_uid=1706710359807003631; yuidss=7744706041698934135; yandex_login=IvanaMis; i=KU1HJY33Qo/eoSqZtUfxg7kILW1umOBlxkHt2HYWzpAaJnaPjy1S74LwobIQNQthh8NvUuGykD8Oj1hrnAaI/rD78+Q=; yandexuid=7744706041698934135; L=XlNkXAJtBn5Wb2d9Z2pAaUgDXXBRVXVUcRsrAyw+DT4=.1706710379.15605.346458.1b8d796b8a5a2fa991c4bdffb797d450; my_perpages=%5B%5D; mobile=no; mda_exp_enabled=1; PHPSESSID=eef49afc25c7174bc9a6e0b21a016875; user_country=ru; yandex_gid=213; tc=1; uid=166905197; _csrf_csrf_token=-S3wIEnOz56ZKMuo81EcTrCowT-HnOvZ8zNOeU2DDuI; desktop_session_key=6eff432f79614cbb044859b717a154ed5b78b93785b1848de78c768df658ccadb03f77ff51577fcfed2da3bf974196ca69c2de940abbca7842b0a6d7df5cf5e7b622978f52396912597a7c1f74d64bf6e0980d56ee06cef46b138ec2d31cfa62; desktop_session_key.sig=ChIopUHB31I5xkZ4EnDGlE2Nm6E; _yasc=wUvxZqXHfEPHEY7534ofJALbZC3PC7uBinpbdda9kpmiKCYerRk5yUlzaSVbED33; _ym_isad=2; yp=1706958275.yu.7744706041698934135; ymex=1709463875.oyu.7744706041698934135; ya_sess_id=3:1706871875.5.0.1706710379495:tWDqWw:85.1.2:1|1509767378.0.2.3:1706710379|30:10222305.130320.HWXfSfw9Enb28sReD43qQiqKXIg; sessar=1.1186.CiDKB6HHshlZ1mjtOC3ZI8zlMdj9NodbU9QF5Qdb57gGxw.woc04WLZ3H-ivo3YMEnOrieRIAZTfP86-BS_33c8Sm8; ys=udn.cDpJdmFuYU1pcw%3D%3D#c_chck.4159833070; mda2_beacon=1706871875173; sso_status=sso.passport.yandex.ru:synchronized; _ym_visorc=b; _ym_d=1706872588; cycada=OdJSheD0LjA/LzWo5faT20zuArNgq1lsEHlPhgK/85k=',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

r = requests.get(url, headers = head)
r.encoding = 'utf-8'
src = r.text
parser = open('test.html', 'w', encoding="utf-8").write(src)
soup = BeautifulSoup(src, 'lxml')
title = soup.title.string
print(title)