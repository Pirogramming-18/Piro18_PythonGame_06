from Game4 import *
import random


class Person:
    def __init__(self, name, death):
        self.name = name
        self.death = death
        self.now = 0

# 현재 상황 보고, 게임 리스트 출력


def situ(mem_list):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for i in range(len(mem_list)):
        print(
            f'{mem_list[i].name}은(는) 지금까지 {mem_list[i].now}! 치사량까지 {mem_list[i].death - mem_list[i].now}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def game_list():
    print('~~~~~~~ 🍾오늘의 Alcohol GAME🍾 ~~~~~~~~~~~~~~~')

    print('🍾 1. 아파트 게임')
    print('🍾 2. 병뚜껑 게임')
    print('🍾 3. 제로 게임')
    print('🍾 4. 귀엽고~ 깜찍하게~ 지하철 게임')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




def startIntro():
    introStart = """
 ▄▄▄       ██▓     ▄████▄   ██░ ██  ▒█████   ██░ ██  ▒█████   ██▓         ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
▒████▄    ▓██▒    ▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒▓██░ ██▒▒██▒  ██▒▓██▒        ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▒██  ▀█▄  ▒██░    ▒▓█    ▄ ▒██▀▀██░▒██░  ██▒▒██▀▀██░▒██░  ██▒▒██░       ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
░██▄▄▄▄██ ▒██░    ▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░░▓█ ░██ ▒██   ██░▒██░       ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
 ▓█   ▓██▒░██████▒▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░░▓█▒░██▓░ ████▓▒░░██████▒   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
 ▒▒   ▓▒█░░ ▒░▓  ░░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▓  ░    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
  ▒   ▒▒ ░░ ░ ▒  ░  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░ ▒  ░     ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
  ░   ▒     ░ ░   ░         ░  ░░ ░░ ░ ░ ▒   ░  ░░ ░░ ░ ░ ▒    ░ ░      ░ ░   ░   ░   ▒   ░      ░      ░   
      ░  ░    ░  ░░ ░       ░  ░  ░    ░ ░   ░  ░  ░    ░ ░      ░  ░         ░       ░  ░       ░      ░  ░
                  ░                                                                                        
"""
    print(introStart)

# 전사자 확인


def die(mem_list):
    for i in range(len(mem_list)):
        if mem_list[i].now == mem_list[i].death:
            outroStr = """
-----------------------------------------------------------------------------------------------------------------------
            
                      (`-')  _ <-. (`-')  (`-')  _                     (`-')(`-')  _   (`-')          
                .->   (OO ).-/    \(OO )_ ( OO).-/         .->        _(OO )( OO).-/<-.(OO )          
             ,---(`-')/ ,---.  ,--./  ,-.|,------.    (`-')----. ,--.(_/,-.(,------.,------,)         
            '  .-(OO )| \ /`.\ |   `.'   ||  .---'    ( OO).-.  '\   \ / (_/|  .---'|   /`. '         
            |  | .-, \'-'|_.' ||  |'.'|  (|  '--.     ( _) | |  | \   /   /(|  '--. |  |_.' |         
            |  | '.(_(|  .-.  ||  |   |  ||  .--'      \|  |)|  |_ \     /_)|  .--' |  .   .'         
            |  '-'  | |  | |  ||  |   |  ||  `---.      '  '-'  '\-'\   /   |  `---.|  |\  \  ,-.,-.,-. 
             `-----'  `--' `--'`--'   `--'`------'       `-----'     `-'    `------'`--' '--  '-''-''-' 

-----------------------------------------------------------------------------------------------------------------------
            """
            print(outroStr)
            print(f'{mem_list[i].name}이(가) 전사했습니다...😵 꿈나라에서는 편히 쉬시길 ..zzz😴')
            return 1

    return 0

# 1. 아파트 게임

def Intro1():
    introStr = """
--------------------------------------------------------------------------------------------------------------------------------------------------------
____________________________________________________________________     _______________________________     
7  _  77     77  _  77  _  77      77        77     77     77      7     7     77  _  77        77     7     
|  _  ||  -  ||  _  ||    _|!__  __!|  _  _  ||  ___!|  _  |!__  __!     |   __!|  _  ||  _  _  ||  ___!     
|  7  ||  ___!|  7  ||  _ \   7  7  |  7  7  ||  __|_|  7  |  7  7       |  !  7|  7  ||  7  7  ||  __|_     
|  |  ||  7   |  |  ||  7  |  |  |  |  |  |  ||     7|  |  |  |  |       |     ||  |  ||  |  |  ||     7     
!__!__!!__!   !__!__!!__!__!  !__!  !__!__!__!!_____!!__!__!  !__!       !_____!!__!__!!__!__!__!!_____!    

--------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    print(introStr)
    print('아파트🏢 ~ 아파트🏬 ~ 아파트🏢 아파트🏬 몇 층🔢?!?!')


def Game1(mem_list):
    Intro1()
    loser_index = 0

    # 양손으로 하는 게임이라 범위는 사용자들의 손의 갯수
    floor = randint(1, len(mem_list)*2)
    hand_list = []

    for i in range(len(mem_list)):
        hand_list.append(mem_list[i].name)
        hand_list.append(mem_list[i].name)

    floor_hand = sample(hand_list, len(mem_list)*2)

    for i in range(len(floor_hand)):
        print('-------', i+1, '층', floor_hand[i], ' hand-------')

    print('정답 공개: ', floor, '층', floor_hand[floor-1])

    for i in range(len(mem_list)):
        if mem_list[i].name == floor_hand[floor-1]:
            loser_index = i
            break

    return loser_index

# 2. 병뚜껑 게임


def Intro2():
    introStr = """
--------------------------------------------------------------------------------------------------------------------------------------------------------

  ______       __        _______       _____  ___  ____  ____ ___      ___ _______   _______  _______        _______      __      ___      ___  _______  
 /" _  "\     /""\      |   __ "\     (\"   \|"  \("  _||_ " |"  \    /"  |   _  "\ /"     "|/"      \      /" _   "|    /""\    |"  \    /"  |/"     "| 
(: ( \___)   /    \     (. |__) :)    |.\\   \    |   (  ) : |\   \  //   (. |_)  :|: ______):        |    (: ( \___)   /    \    \   \  //   (: ______) 
 \/ \       /' /\  \    |:  ____/     |: \.   \\  (:  |  | . )/\\  \/.    |:     \/ \/    | |_____/   )     \/ \       /' /\  \   /\\  \/.    |\/    |   
 //  \ _   //  __'  \   (|  /         |.  \    \. |\\ \__/ //|: \.        (|  _  \\ // ___)_ //      /      //  \ ___ //  __'  \ |: \.        |// ___)_  
(:   _) \ /   /  \\  \ /|__/ \        |    \    \ |/\\ __ //\|.  \    /:  |: |_)  :|:      "|:  __   \     (:   _(  _/   /  \\  \|.  \    /:  (:      "| 
 \_______|___/    \___|_______)        \___|\____\|__________)___|\__/|___(_______/ \_______)__|  \___)     \_______|___/    \___)___|\__/|___|\_______) 
                                                                                                                                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    print(introStr)
    print("🍻병뚜껑 숫자는 몇 번~? 몇 번!!🔢 숫자를~ 맞춰라~! 🎯")


def Game2(mem_list):
    Intro2()
    cap = randint(1, 50)

    while True:
        num = input('병뚜껑 숫자를 불러주세요~ (1부터 50까지) : ')
        if num.isdigit() and 1 <= int(num) <= 50:
            num = int(num)
            break

    cap_list = [num]
    # 컴퓨터 숫자 할당
    for i in range(len(mem_list) - 1):  # 사용자는 위에서 지정해서 len - 1
        cap_list.append(randint(1, 50))  # 사용자가 인덱스 0이기 때문에 1부터

    # 절대값 계산
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
# 3. 제로 게임


def Intro3():
    introStr = """

███████╗███████╗██████╗  ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
  ███╔╝ █████╗  ██████╔╝██║   ██║    ██║  ███╗███████║██╔████╔██║█████╗  
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
███████╗███████╗██║  ██║╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                         
                                                                
"""
    print(introStr)


def Game3(mem_list):
    print()
    Intro3()
    print("본인이 선택한 숫자와 본인을 포함한 다른 모든 인원이 들어올린 엄지 개수의 합이 똑같으면 한 잔!")
    print("-------------------------Game Start!----------------------------")
    count = 0
    while (True):
        randomList = []
        add = 0

        while True:
            num1 = input("들어 올릴 엄지손가락 수를 입력하세요(최대: 2): ")
            if num1.isdigit() and 0 <= int(num1) <= 2:
                num1 = int(num1)
                break

        print()
        randomList.append(num1)  # 사용자 인덱스 0번

        if count == 0:
            while True:
                num2 = input("당신 차례! 당신이 고를 숫자를 입력해주세요(최대: 인원수x2): ")
                if num2.isdigit() and 0 <= int(num2) <= len(mem_list)*2:
                    num2 = int(num2)
                    break
            print()
        for i in range(len(mem_list)-1):  # 컴퓨터 엄지개수 입력, 이 시점에서 mem과 random길이 같음
            randomNum = randint(0, 2)
            randomList.append(randomNum)

        for i in range(len(randomList)):
            print("{}: 엄지 수 {}!".format(
                mem_list[i].name, randomList[i]))  # 손가락 개수 각각 출력
            add = add + randomList[i]  # 손가락 개수 다 합치기
        print()
        if count == 0:
            if num2 == add:
                print("{}: {} 선택!".format(mem_list[0].name, add))
                print("{} 당첨! 한 잔 하세요".format(mem_list[0].name))
                print()
                loser_index = 0
                return loser_index
            else:
                print("{}: {} 선택!".format(mem_list[0].name, num2))
                print()
                count = count + 1
        else:
            choice = randint(0, len(mem_list)*2)
            print("{}: {} 선택!".format(mem_list[count].name, choice))
            print()
            if add == choice:
                print("{} 당첨! 한 잔 하세요".format(mem_list[count].name))
                print()
                loser_index = count
                return loser_index
            else:
                count = count + 1
        if count == len(randomList):
            count = 0
# 4. 지하철 게임


# def Game4(mem_list):
#     return


if __name__ == '__main__':
    # 1.게임 시작

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    startIntro()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('안주 먹을 시간이 없어요😟🤑😵‍💫🤮🤢마시면서 배우는 술게임🍻🍺🍷🍸')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    yn = input('게임을 진행할까요? (y/n) : ')

    if yn == 'y':
        # 2. 사용자의 이름 받기
        player_name = input('오늘 코 삐뚤어질 당신의 이름은?😘 : ')

        # 3. 본인의 주량 선택하기

        while True:
            print('~~~~~~~~~~ 🍾소주 기준 당신의 주량은? 🍾 ~~~~~~~~~~')
            print('🍾 1. 소주 반 병 (2잔)')
            print('🍾 2. 소주 반 병 ~ 한 병 (4잔)')
            print('🍾 3. 소주 한 병 ~ 한 병 반 (6잔)')
            print('🍾 4. 소주 한 병 반 ~ 두 병 (8잔)')
            print('🍾 5. 소주 두 병 이상 (10잔)')
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

        # 4. 같이 대결할 사람 초대하기 & 게임 리스트 출력하기
        name_list = ['담희', '정원', '신빈', '환준']

        while True:
            mem_num = input(
                '함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!): ')

            if not mem_num.isnumeric():
                print('정수를 입력해주세요!')
            elif int(mem_num) > 3:
                print('너무 많은 친구들을 골랐어요! 다시 선택해주세요')
            elif int(mem_num) < 1:
                print('혼자서는 게임을 할 수 없어요 T_T')
            else:
                break

        for i in range(len(name_list)):
            if name_list[i] == player_name:
                name_list.pop(i)
                break

        l = len(name_list)
        for i in range(int(mem_num)):
            com_name = random.choice(name_list)
            name_list.remove(com_name)
            com_death = randrange(2, 11, 2)
            print(f'오늘 함께 취할 친구는 {com_name}입니다! (치사량 : {com_death})')
            mem_list.append(Person(com_name, com_death))

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        situ(mem_list)
        game_list()

        play_turn = 0
        exit = 'a'
        while exit != 'exit':
            if play_turn == 0:
                while True:
                    game_choice = input(f'{mem_list[play_turn].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : ')
                    if game_choice.isdigit() and 1 <= int(game_choice) <= 4:
                        game_choice = int(game_choice)
                        break
            else:  # 컴퓨터 초이스
                game_choice = randint(1, 4)
                print(
                    f'{mem_list[play_turn].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : {game_choice}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'{mem_list[play_turn].name}님이 게임을 선택하였습니다!')

            if game_choice == 1:
                loser = Game1(mem_list)
            elif game_choice == 2:
                loser = Game2(mem_list)
            elif game_choice == 3:
                loser = Game3(mem_list)
            elif game_choice == 4:
                loser = Game4(mem_list)

            print(f'언제까지😵‍💫 어깨 춤을 추게 할거야~~🤯 {mem_list[loser].name}~~!! 원샷~')

            mem_list[loser].now += 1

            situ(mem_list)
            check = die(mem_list)
            if check == 1:
                break

            game_list()
            exit = input(
                '술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"를, 계속하고 싶으면 아무키나 입력해주세요! : ')
            play_turn += 1

            # play_turn이 게임 참여자 수와 같으면 다시 처음 플레이어로 돌아가기
            if play_turn == len(mem_list):
                play_turn = 0

    else:
        print('다음번엔 참여해주세요.. 꼬옥..!😥')

    if exit == 'exit':
        print('오늘은 여기까지지만 다음엔 끝까지 달려요~~!!')
