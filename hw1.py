def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(a):
    print('반지름이' ,a , '인 원의 넓이 =','3.14 x', a, ( 'x' ), a, "=", 3.14*int(a)*int(a))

a = input_prompt = input('넓이를 구하고자 하는 원의 반지름은? ')
get_circle_area(a)
