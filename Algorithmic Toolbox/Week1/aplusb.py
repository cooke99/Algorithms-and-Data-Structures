def aplusb(a: int, b: int):
    return a + b

if __name__ == '__main__':
    str_in = input().split()
    a, b = int(str_in[0]), int(str_in[1])
    print(aplusb(a,b))
