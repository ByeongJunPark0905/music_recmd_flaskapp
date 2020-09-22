from bs4 import BeautifulSoup
from pprint import pprint
from time import localtime, strftime
import requests
import model
from time import localtime, strftime




def get_weather():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('div', {'class':'weather_box'})
    find_address = data1.find('span', {'class':'btn_select'}).text
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    temp_ = find_currenttemp+'℃'
    WeatherCast = soup.find('p', {'class' : 'cast_txt'}).text

    return [find_address, temp_, WeatherCast, find_currenttemp]




def timeZone():
    data = strftime("%H:%M", localtime())
    hour = data.split(':')[0]
    if 12 > int(hour) >= 6:
        return '오전'
    elif 18 > int(hour) >= 12:
        return '오후'
    elif 22 > int(hour) >= 18:
        return '저녁'
    elif 24 >= int(hour) >= 22 or 6 > int(hour) >= 0:
        return '밤'
    # elif 6 > int(hour) >= 2:
    #     return '새벽'




def weather():
    w = get_weather()[2].split(',')
    # w[0]의 종류
    # 맑음, 구름조금, 구름많음, 흐림, 비, 소낙비, 눈, 소낙눈, 눈비, 뇌우/폭우, 안개, 황사

    if w[0][:2] == '구름':
        w[0] = '흐림'
    elif w[0] == '소낙비':
        w[0] = '비'
    elif w[0] == '소낙눈':
        w[0] = '눈'
    elif w[0][:2] == '뇌우' or w[0][:2] == '폭우':
        w[0] = '비'
    elif w[0] == '눈비':
        season_ = season() # 겨울이면 눈, 여름이면 비
        if season_ == '겨울':
            w[0] == '눈'
        else:
            w[0] == '비'
    elif w[0] == '안개':
        w[0] == '흐림' # <---- 임시
    elif w[0] == '황사':
        w[0] == '흐림' # <---- 임시
    return w[0]




def season():
    mon = strftime("%m", localtime())
    if mon=='03' or mon=='04' or mon=='05':
        return '봄'
    elif mon=='06' or mon=='07' or mon=='08':
        return '여름'
    elif mon=='09' or mon=='10' or mon=='11':
        return '가을'
    elif mon== '12' or mon=='01' or mon=='02':
        return '겨울'

def get_weather_tag():
    t = int(get_weather()[3])
    weather_ = weather()
    # season_ = season()
    time_ = timeZone()
    # temp_ = feelTemp(t)
    return [weather_,time_]

#climate_dic = {'맑음': 1, '흐림': 3, '비': 2, '눈': 0}
#time_dic = {'오전': 1, '오후': 2, '저녁': 3, '밤': 0}

def get_weather_theme(weather_=weather(),time_=timeZone()):

    weather_theme = {'비오후':'rainyaftn','비밤':'rainy','맑음오후':'sunny_day','흐림오후':'sunny_day','맑음오전':'sunny_day','맑음밤':'latenight'}
    current_ = weather_ + time_
    try:
        return weather_theme[current_]
    except(KeyError):
        return 'rainyaftn'


