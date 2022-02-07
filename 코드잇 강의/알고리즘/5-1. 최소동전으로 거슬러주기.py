def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    min_coin = 0
    coin_list = sorted(coin_list, reverse=True)

    for i in coin_list:
        coin = value // i
        min_coin += coin
        value = value - i * coin
    return min_coin


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))