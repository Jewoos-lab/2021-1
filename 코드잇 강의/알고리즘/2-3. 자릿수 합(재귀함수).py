def sum_digits(n):
    str_n = str(n)
    if len(str_n) == 1:
        return int(str_n[0])
    elif len(str_n) != 1:
        return int(str_n[0]) + sum_digits(int(str_n[1:]))




# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


# def sum_digits(n):
#     # base case
#     if n < 10:
#         return n
#     # n이 한자리 수 일때 그냥 n 리턴해라
#
#     # recursive case
#     return n % 10 + sum_digits(n // 10)
#
# print(sum_digits(22541))
# print(sum_digits(92130))
# print(sum_digits(12634))
# print(sum_digits(704))
# print(sum_digits(3755))