def efficient_change_money(money: int) -> int:
    return (money//10) + ((money%10)//5) + (money%5)

if (__name__ == '__main__'):
    money = int(input())
    print(efficient_change_money(money))
