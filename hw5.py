def read_number(num):
    hundreds = num // 100
    tens = (num - hundreds * 100) // 10
    ones = num % 10

    return hundreds, tens, ones

def read_singe_digit(num):
    if num == 0:
        return("영")
    elif num == 1:
        return("일")
    elif num == 2:
        return("이")
    elif num == 3:
        return("삼")
    elif num == 4:
        return("사")
    elif num == 5:
        return("오")
    elif num == 6:
        return("육")
    elif num == 7:
        return("칠")
    elif num == 8:
        return("팔")
    elif num == 9:
        return("구")

num = int(input("세 자리 정수 입력: "))
hundreds, tens, ones = read_number(num)
print(read_singe_digit(hundreds), read_singe_digit(tens), read_singe_digit(ones))
