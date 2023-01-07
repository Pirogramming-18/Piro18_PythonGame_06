##### 병뚜껑 게임 : 자신의 숫자 - 병뚜껑 숫자의 절대값 숫자가 가장 큰 사람이 벌칙!!
#mem = 본인 제외한 참여자 리스트 (컴퓨터)
def Game2(mem_list):
    cap = randint(1,50)

    num = int(input('병뚜껑 숫자를 불러주세요~ (1부터 50까지) : '))
    cap_list = [num]
    #컴퓨터 숫자 할당
    for i in range(len(mem_list) -1): # 사용자는 위에서 지정해서 len - 1
        cap_list[i + 1] = randint(1, 50) # 사용자가 인덱스 0이기 때문에 1부터

    #절대값 계산
    for i in range(len(mem_list)):
        cap_list[i] = abs(cap - cap_list[i])

    max_num = -999
    for i in range(len(cap_list)):
        if max_num < cap_list[i]:
            loser_index = i

    return loser_index