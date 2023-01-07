from random import *

class Person:
    def __init__(self, name, death):
        self.name = name
        self.death = death
        self.now = 0

#####현재 상황 보고, 게임 리스트 출력
def situlist(mem_list):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for i in range(len(mem_list)):
        print(f'{mem_list[i].name}은(는) 지금까지 {mem_list[i].now}! 치사량까지 {mem_list[i].death - mem_list[i].now}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~ 오늘의 Alcohol GAME ~~~~~~~~~~~~~~~')

    print('1. 아파트 게임')
    print('2. 병뚜껑 게임')
    print('3. 제로 게임')
    print('4. 귀엽고~ 깜찍하게~ 지하철 게임')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

##### 전사자 확인
def die(mem_list):
    for i in range(len(mem_list)):
        if mem_list[i].now == mem_list[i].death:
            print(f'{mem_list[i].name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길 ..zzz')
            return 1

    return 0

##### 1. 아파트 게임
def Game1(mem_list):
    print('아파트 ~ 아파트 ~ 아파트 아파트 몇 층?!?!')
    loser_index = 0

    #양손으로 하는 게임이라 범위는 사용자들의 손의 갯수
    floor = randint(1, len(mem_list)*2)
    hand_list = []

    for i in range(len(mem_list)):
        hand_list.append(mem_list[i].name)
        hand_list.append(mem_list[i].name)
    
    floor_hand = sample(hand_list, len(mem_list)*2)
    
    for i in range(len(floor_hand)):
        print('-------',i+1,'층',floor_hand[i],' hand-------')

    print('정답 공개: ',floor, '층', floor_hand[floor-1])

    for i in range(len(mem_list)):
        if mem_list[i] == floor_hand[floor-1]:
            loser_index = i
            break

    return loser_index
##### 2. 병뚜껑 게임
def Game2(mem_list):
    cap = randint(1,50)

    num = int(input('병뚜껑 숫자를 불러주세요~ (1부터 50까지) : '))
    cap_list = [num]
    #컴퓨터 숫자 할당
    for i in range(len(mem_list) -1): # 사용자는 위에서 지정해서 len - 1
        cap_list.append(randint(1,50)) # 사용자가 인덱스 0이기 때문에 1부터

    #절대값 계산
    abs_list = []
    for i in range(len(mem_list)):
        abs_list.append(abs(cap - cap_list[i]))

    max_num = -999
    for i in range(len(cap_list)):
        if max_num < abs_list[i]:
            max_num = abs_list[i]
            loser_index = i

    print(f'정답 공개: {cap}')
    for i in range(len(mem_list)):
        print(f'{mem_list[i].name}: 선택값 = {cap_list[i]}  절대값 = {abs_list[i]}')

    return loser_index
##### 3. 제로 게임
def Game3(mem_list):
    return
##### 4. 지하철 게임
def Game4(mem_list):
    return
if __name__ == '__main__':
    #1.게임 시작

    print('술게임 시작~~~~~~~')
    yn = input('게임을 진행할까요? (y/n) : ')

    if yn == 'y':
        #2. 사용자의 이름 받기
        player_name = input('오늘 코 삐뚤어질 당신의 이름은? : ')

        #3. 본인의 주량 선택하기

        while True:
            print('~~~~~~~~~~소주 기준 당신의 주량은?~~~~~~~~~~')
            print('1. 소주 반 병 (2잔)')
            print('2. 소주 반 병 ~ 한 병 (4잔)')
            print('3. 소주 한 병 ~ 한 병 반 (6잔)')
            print('4. 소주 한 병 반 ~ 두 병 (8잔)')
            print('5. 소주 두 병 이상 (10잔)')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            death_choice = input('당신의 치사량(주량)은 얼마만큼인가요? (1~5를 선택해주세요): ')

            if not death_choice.isnumeric() or death_choice < '1' or death_choice > '5':
                print('벌써 취한건 아니죠? 잘못된 값을 입력했어요~ 다시 선택해주세요!!')
            else:
                if death_choice == '1':
                    death = int(2)
                    break
                elif death_choice == '2':
                    death = int(4)
                    break
                elif death_choice == '3':
                    death = int(6)
                    break
                elif death_choice == '4':
                    death = int(8)
                    break
                elif death_choice == '5':
                    death = int(10)
                    break

        mem_list = []
        mem_list.append(Person(player_name, death))


        #4. 같이 대결할 사람 초대하기 & 게임 리스트 출력하기
        name_list = ['담희', '정원', '신빈', '환준']

        while True:
            mem_num = input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!): ')

            if not mem_num.isnumeric():
                print('정수를 입력해주세요!')
            elif int(mem_num) > 3:
                print('너무 많은 친구들을 골랐어요! 다시 선택해주세요')
            elif int(mem_num) < 1:
                print('혼자서는 게임을 할 수 없어요 T_T')
            else:
                break

        for i in range(int(mem_num) + 1):
            if name_list[i] == player_name:
                name_list.pop(i)
                break

        l = len(name_list)
        for i in range(int(mem_num)):
            com_name = name_list.pop()
            com_death = randrange(2,11,2)
            print(f'오늘 함께 취할 친구는 {com_name}입니다! (치사량 : {com_death})')
            mem_list.append(Person(com_name,com_death))

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        situlist(mem_list)

        play_turn = 0
        exit = 'a'
        while exit != 'exit':
            if play_turn == 0:
                game_choice = int(input(f'{mem_list[play_turn].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : '))
            else: #컴퓨터 초이스
                game_choice = randint(1,4)
                print(f'{mem_list[play_turn].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : {game_choice}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'{mem_list[play_turn].name}님이 게임을 선택하였습니다!')

            if game_choice == 1:
                loser = Game1(mem_list)
            elif game_choice == 2:
                loser = Game2(mem_list)
            elif game_choice == 3:
                loser = Game3(mem_list)
            elif game_choice == 3:
                loser = Game4(mem_list)

            print(f'{mem_list[loser].name}이(가) 걸림!! 원샷~')

            mem_list[loser].now += 1

            situlist(mem_list)
            check = die(mem_list)
            if check == 1:
                break

            exit = input('술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"를, 계속하고 싶으면 아무키나 입력해주세요! : ')
            play_turn += 1

            #4명 이상이면 다시 처음 플레이어로
            if play_turn > 4:
                play_turn = 0

    else:
        print('다음번엔 참여해주세요.. 꼬옥..!')

    if exit == 'exit':
        print('오늘은 여기까지지만 다음엔 끝까지 달려요~~!!')