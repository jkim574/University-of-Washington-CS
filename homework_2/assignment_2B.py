#assignment#2

SIZE = 3

def head_tail():
    for line in range(1, 2 * SIZE):
        print((2 * SIZE - line) * " " + line * "/" + "**" + line * "\\" + (2 * SIZE - line) * " ")

def midLine():
    print("+" + 2 * SIZE * "=*" + "+")

def firstHalf_top():
    for line in range(1, SIZE + 1):
        print("|" + (SIZE -line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + "|")

def firstHalf_bottom():
    for line in range(SIZE, 0, -1):
        print("|" + (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + "|")

def secondHalf_top():
    for line in range(SIZE, 0, -1):
        print("|" + (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "\/" + \
              (SIZE - line) * "." + "|")

def secondHalf_bottom():
    for line in range(1, SIZE + 1):
        print("|" + (SIZE -line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + \
              (SIZE - line) * "." + \
              line * "/\\" + \
              (SIZE - line) * "." + "|")


head_tail()
midLine()
firstHalf_top()
firstHalf_bottom()
midLine()
secondHalf_top()
secondHalf_bottom()
midLine()
head_tail()
