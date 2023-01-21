def naive_change_money(money: int) -> int:
    num_coins = 0
    while (money > 0):
        if (money >= 10):
            money -= 10
        elif (money >= 5):
            money -= 5
        else:
            money -= 1
        num_coins += 1
    return num_coins

if (__name__ == '__main__'):
    money = int(input())
    print(naive_change_money(money))
