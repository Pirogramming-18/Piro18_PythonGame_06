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

if __name__ == '__main__':
    #1.게임 시작

    print('술게임 시작~~~~~~~')
    #yn = input('게임을 진행할까요? (y/n) : ')
    yn = 'y'
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

    else:
        print('다음번엔 참여해주세요.. 꼬옥..!')