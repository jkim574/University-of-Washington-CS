


from drawingpanel import *


panel = DrawingPanel(650, 400, "gray")
MORTAR = 2

#x: initial x position
#y: initial y position
#num: number of paris
#size: size of each box
#offset: a certain distance in the x direction relative to the first
#MORTAR : space between layers of each rows

 #function for drawing single row
def single_row(x, y, num, size):
    for boxes in range(0, num):
        print('%dx, %dy, %dnum, %dsize, %dboxes' % (x, y, num, size, boxes))
        panel.canvas.create_rectangle(x + 2 * boxes * size, y, x + 2 * boxes * size + size, y + size, fill = "black")
        panel.canvas.create_rectangle(x + 2 * boxes * size + size, y, x + 2 * size + 2 * boxes * size ,y + size, fill = "white")
        panel.canvas.create_line(x + 2 * boxes * size, y, x + 2 * boxes * size + size, y + size, fill = "blue")
        panel.canvas.create_line(x + 2 * boxes * size, y + size, x + size + 2 * boxes * size, y, fill = "blue")

#function for drawing multiple rows, combined as grid
def grid(x, y, num, size, offset):
    for i in range(0, num * 2):
        print('%di, %dx, %dy, %dnum, %dsize, %doffset' % (i, x, y, num, size, offset))
        single_row(x - (offset * pow(-1, i)) / 2, y + i * (size + MORTAR), num, size)
        print()


if __name__ == "__main__":

    # single_row(0,0,4,20)
    # single_row(50,70,5,30)

    grid(10, 150, 4, 25, 0)
    # grid(250,200,3,25, 10)
    # grid(425,180,5,20, 10)
    # grid(400,20,2,35, 35)

    panel.mainloop()
