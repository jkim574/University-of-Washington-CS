#assignment#2

SIZE = 6



def head_tail():
    for line in range(1, 2 * SIZE):
        print((2 * SIZE - line) * " " + line * "/" + "**" + line * "\\" + (2 * SIZE - line) * " ")


def mid_line():
    print("+" + 2 * SIZE * "=*" + "+")


def first_half_top():
    for line in range(1, SIZE + 1):
        print("|" + (SIZE -line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + "|")


def first_half_bottom():
    for line in range(SIZE, 0, -1):
        print("|" + (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + "|")


def second_half_top():
    for line in range(SIZE, 0, -1):
        print("|" + (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + "|")


def second_half_bottom():
    for line in range(1, SIZE + 1):
        print("|" + (SIZE -line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + "|")



if __name__ == "__main__":
    head_tail()
    mid_line()
    first_half_top()
    first_half_bottom()
    mid_line()
    second_half_top()
    second_half_bottom()
    mid_line()
    head_tail()
