shopping_bag = {}
item = 'd'

while not item == '':
    item = input("상품명은? ")

    if item != '':
        n = int(input("수량은? "))
        shopping_bag[item] = n
        print(f'장바구니에 {item} {n}개가 담겼습니다.')
    print("")

print(">>> 장바구니 보기: ", shopping_bag)
print("")
print("[검색]")
a = input("장바구니에서 확인하고자 하는 상품은? ")
print(f'{a}은(는) {shopping_bag[a]}개 담겨있습니다.')

