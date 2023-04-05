def draw_line_string(name):
    msg1 = "Hello " + name + ","
    msg2 = "Welcome to Seoul."

    def rep_char():
        nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

        print("-" * nstr)
        print(msg1)
        print(msg2)
        print("-" * nstr)

    rep_char()

name = input("Input his/her name: ")
draw_line_string(name)
