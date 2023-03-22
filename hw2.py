def exchange(money):
    n500 = money // 500
    n100 = (money - n500*500) // 100
    n50 = (money - n500*500 - n100*100) // 50
    n10 = (money - n500*500 - n100*100 - n50*50) // 10
    print("500원 동전의 개수 :", n500)
    print("100원 동전의 개수 :", n100)
    print("50원 동전의 개수 :", n50)
    print("10원 동전의 개수 :", n10)

def get_integer(m):
    money = int(input(m))
    return money

money = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(money)
