from random import choice

def trial():
    occupied = [False] * 100
    seat_remained = [i for i in range(100)]
    for i in range(100):
        seat_num = choice(seat_remained) if i==0 or occupied[i] == True else i
        occupied[seat_num] = True
        seat_remained.remove(seat_num)
    
    return True if seat_num == 99 else False

# 100명이 탈 수 있는 자리가 있다
# 1번 부터 100번까지 순서대로 탈 것이다
# 1번 사람이 술에 취해 랜덤으로 아무 자리에 앉는다
# 2번 부터는 다시 규칙대로 앉는다
# 내자리가 비어있으면 해당 자리에 앉고
# 누가 내 자리에 앉으면 랜덤으로 자리에 앉는다
# 결과로는 100번 좌석표를 가진 사람이 자신의 좌석
# 100번 좌석에 앉을 확률을 구하시오