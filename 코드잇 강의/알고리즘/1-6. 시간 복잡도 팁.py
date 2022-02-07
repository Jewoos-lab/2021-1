# O(1), O(lg n), O(n), O(n lg n), O(n^2), O(n^3)
# 나름의 팁은 반복문이 없으면 대체로 O(1)
# 반복문이 3번 나와도 결국 O(3n) = O(n)이다.

# 반복문 안에 반복문(즉 2중for문 같은경우)엔 O(n^2)
# 3중포문 O(n^3)

# O(lg n) 함수
# 2의 거듭제곱을 출력하는 함수
# (이번에는 인풋이 리스트가 아니라 그냥 정수입니다)
def print_powers_of_two(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2
# 위 코드인 경우엔 O(lg n)

def print_powers_of_two_repeatedly(n):
    for i in range(n): # 반복횟수: n에 비례
        j = 1
        while j < n: # 반복횟수: lg n에 비례
            print(i, j)
            j = j * 2
# 위 코드인 경우엔 O(n lg n)