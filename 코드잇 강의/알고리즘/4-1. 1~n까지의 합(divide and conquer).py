def consecutive_sum(start, end):
    #base case 구하기(start와 end가 같을 때)
    if start == end:
        return start
    #divide and conquer의 세 단계 해결하기
    #1. Divide: 주어진 문제를 반으로 나누어 두 개의 부분 문제로 나눈다.
    mid = (start + end) // 2
    #2. Conquer: 두 부분 문제를 재귀적으로 구한다.
    #3. Combine: 계산한 두 부분 문제의 답을 더한다.
    return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)

print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))