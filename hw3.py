def get_fixed_price(discount_rate, discount_price):
    fixed_price = discount_price * 100 / (100- discount_rate)
    return fixed_price

discount_rate = int(input("할인율은? "))
discount_price_A = (int(input("A 상품의 할인된 가격은? ")))
discount_price_B = (int(input("B 상품의 할인된 가격은? ")))  

fixed_price_A = get_fixed_price(discount_rate, discount_price_A)
print("A 상품의 정가는", fixed_price_A, " 원")

fixed_price_B = get_fixed_price(discount_rate, discount_price_B)
print("B 상품의 정가는", fixed_price_B, " 원")
