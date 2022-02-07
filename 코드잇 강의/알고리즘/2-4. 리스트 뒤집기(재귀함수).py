# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    else:
        return some_list[-1:] + flip(some_list[:-1])
        #some_list[-1]이 아니라 [-1:]인 이유는 [-1]만 썼을 땐, 리스트형태가 아니라
        #n처럼 그냥
        #숫자로 나와. 하지만 [-1:]로 했을 땐, [n]처럼 리스트 형태로 뜬다!


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)