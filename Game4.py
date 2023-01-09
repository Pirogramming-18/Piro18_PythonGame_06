import requests
from bs4 import BeautifulSoup as bs
import json
from pprint import pprint
from random import *


# class Person:
#     def __init__(self, name, death):
#         self.name = name
#         self.death = death
#         self.now = 0


def get_emoticons():
    url = "https://snskeyboard.com/emoticon/"
    response = requests.get(url)

    soup = bs(response.content.decode('utf-8', 'replace'), "html.parser")

    raw_categories = soup.select(
        '#data > div.service_result_area.pkg_pre_itemsContainer > div')

    category = []

    for raw_category in raw_categories:
        category.append(raw_category.get("id"))

    category = category[:24]

    emoticons = [[] for i in range(24)]
    idx = 0
    # happy > div.box-C > div > pre: nth-child(1)
    for raw_category in raw_categories:
        raw_emoticons = raw_category.select('#'+category[idx]+' pre')
        for raw_emoticon in raw_emoticons:
            emoticons[idx].append(raw_emoticon.string)
        idx += 1
        if idx >= 24:
            break

    return emoticons


def get_subway(line_num):
    url = 'http://openapi.seoul.go.kr:8088/4f7778796373706138316f52626d47/json/SearchSTNBySubwayLineInfo/1/800/'
    response = requests.get(url)
    jsondata = json.loads(response.text)
    raw_data = jsondata['SearchSTNBySubwayLineInfo']['row']
    stations = [[] for i in range(len(line_num) + 2)]
    for raw_info in raw_data:
        stations[line_num.index(raw_info['LINE_NUM'])].append(
            raw_info['STATION_NM'])

    return stations


def Intro4():
    introStr = """
-----------------------------------------------------------------------------------------------------------------------

 _______                                ______       _                          _______
(_______)        _                     / _____)     | |                        (_______)
 _       _   _ _| |_ _____    _____   ( (____  _   _| |__  _ _ _ _____ _   _    _   ___ _____ ____  _____
| |     | | | (_   _) ___ |  (_____)   \____ \| | | |  _ \| | | (____ | | | |  | | (_  (____ |    \| ___ |
| |_____| |_| | | |_| ____|            _____) ) |_| | |_) ) | | / ___ | |_| |  | |___) / ___ | | | | ____|
 \______)____/   \__)_____)           (______/|____/|____/ \___/\_____|\__  |   \_____/\_____|_|_|_|_____)
                                                                      (____/

-----------------------------------------------------------------------------------------------------------------------
    """
    print(introStr)
    print("귀엽고~~😆 깜찍하게~~😝 지하철~ 지하철🚃 지하철~ 지하철🚊 몇호선~ 몇호선🚎 몇호선~ 몇호선🚉")


def inputLine():
    while True:
        print("--------------------------------------------------------------------------------")
        print("1호선 ~ 9호선 : 1 ~ 9 입력")
        print("10: 김포도시철도    11: 의정부경전철    12: 인천선    13: 인천2호선")
        print("14: 경춘선    15: 경의선    16: 공항철도    17: 수인분당선    18: 신분당선")
        print("19: 경강선    20: 용인경전철    21: 우이신설경전철    22: 서해선    23: 신림선")
        print("--------------------------------------------------------------------------------")
        line = input('호선을 입력해주세요 : ')
        try:
            int(line)
        except ValueError:
            print("벌써 취한건 아니죠? 1 ~ 23의 정수를 입력하세요!")
            continue
        line = int(line)
        if 1 <= line <= 23:
            return line
        else:
            print("벌써 취한건 아니죠? 1 ~ 23의 정수를 입력하세요!")


def Transfer(cur_line, change_cnt, change_line, stations, line_num):
    while True:
        will_transfer = input("환승 여부를 골라주세요! (y/n) : ")
        if will_transfer == 'y':
            next_line = inputLine()
            if (cur_line == next_line) or (next_line not in change_line) or (change_cnt < 1) or (len(stations[next_line]) == 0):
                print("환승할 수 없는 호선입니다!😅")
                return -1
            else:
                print(line_num[next_line], "으로 환승!🚊")
                return next_line
        elif will_transfer == 'n':
            return cur_line
        else:
            print("y와 n 중에 선택해주세요!😅")


def printRandomEmo(emoticons):
    good_idx = [0, 2, 5, 9, 10, 18, 19, 20, 21, 22, 23]
    bad_idx = [1, 3, 4, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17]
    # 5%의 확률로 부정적 이모티콘
    if randint(1, 1000) < 50:
        idx = choice(bad_idx)
        print(emoticons[idx][randint(0, len(emoticons[idx]) - 1)])
        print("귀엽고 깜찍하지 않아요😰😨😱😫🤢🤮")
        return -1
    else:
        idx = choice(good_idx)
        print(emoticons[idx][randint(0, len(emoticons[idx]) - 1)])
        return 1


def Game4(mem):
    emoticons = get_emoticons()
    line_num = ['00호선', '01호선', '02호선', '03호선', '04호선', '05호선', '06호선', '07호선', '08호선', '09호선', '김포도시철도', '의정부경전철',
                '인천선', '인천2호선', '경춘선', '경의선', '공항철도', '수인분당선', '신분당선', '경강선', '용인경전철', '우이신설경전철', '서해선', '신림선']
    stations = get_subway(line_num)
    whole_stations = stations
    Intro4()
    cur_line = inputLine()
    tmp = list(range(1, len(mem)))
    shuffle(tmp)
    order = [0] + tmp
    order_idx = 0
    while True:
        # 사람 플레이어
        if order_idx == 0:
            print(
                "--------------------------------------------------------------------------------")
            cur_station = input(
                mem[order[order_idx]].name + "님, 역 이름을 입력해주세요 : ")
            # emoticon 출력
            if printRandomEmo(emoticons) == -1:
                return order[order_idx]
            change_cnt = 0
            if cur_station in stations[cur_line]:
                # 환승 가능 호선 체크, 선택한 역 삭제
                change_line = []
                for i in range(len(stations)):
                    if cur_station in stations[i]:
                        if i != cur_line:
                            change_cnt += 1
                            change_line.append(i)
                        stations[i].remove(cur_station)
                # 환승 여부 물어보기
                cur_line = Transfer(cur_line, change_cnt,
                                    change_line, stations, line_num)

            else:
                print("해당 호선의 역이 아니거나 이미 언급된 역입니다ㅠㅠㅠ😅")
                return order[order_idx]

            if cur_line == -1:
                return order[order_idx]

        # 컴퓨터 플레이어
        else:
            cur_station = ""
            # 5%의 확률로 잘못된 호선과 역 선택
            if randint(1, 1000) <= 50:
                while True:
                    cur_station = choice(
                        whole_stations[choice(list(range(0, len(stations))))])
                    if cur_station not in stations[cur_line]:
                        break
                print(mem[order[order_idx]].name + "님이 선택한 역 : " + cur_station)
                # emoticon 출력
                if printRandomEmo(emoticons) == -1:
                    return order[order_idx]
                print("해당 호선의 역이 아니거나 이미 언급된 역입니다ㅠㅠㅠ😅")
                return order[order_idx]
            else:
                cur_station = choice(stations[cur_line])
                print(mem[order[order_idx]].name + "님이 선택한 역 : " + cur_station)
                # emoticon 출력
                if printRandomEmo(emoticons) == -1:
                    return order[order_idx]
                # 환승 가능 호선 체크, 선택한 역 삭제
                change_cnt = 0
                change_line = []
                for i in range(len(stations)):
                    if cur_station in stations[i]:
                        if i != cur_line:
                            change_cnt += 1
                            change_line.append(i)
                        stations[i].remove(cur_station)
                # 60%의 확률로 환승
                if change_cnt > 0 and randint(1, 1000) <= 600:
                    cur_line = choice(change_line)
                    print(line_num[cur_line], "으로 환승!🚊")

        order_idx += 1
        order_idx %= len(mem)


# Game4([Person('담희', 10), Person('정원', 10), Person('환준', 10), Person('신빈', 10)])
