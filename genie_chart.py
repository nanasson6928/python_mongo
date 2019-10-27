# --- Scraping 기본 세팅 ----------------------
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191019', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.

soup = BeautifulSoup(data.text, 'html.parser')

# ---------------------------------------------

# selector를 이용해서 tr들을 불러오기 (table row = list)
musics = soup.select('div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr')

rank = 1
# musics(list)의 반복문 돌리기
for music in musics:
    # musics에서 'a'태그 내용 불러오기
    a_tag = music.select_one('td.info > a')
    title = music.select_one('td.info > a.title.ellipsis').text.strip()
    artist = music.select_one('td.info > a.artist.ellipsis').text
    # print(rank, title, artist)
    rank += 1
