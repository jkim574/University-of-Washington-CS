from drawingpanel import*

panel = DrawingPanel(500, 300)

for line in file("cities.txt"):
    parts = line.split()
    x= int(round(float(parts[0])))
    y= int(round(float(parts[1])))
    panel.canvas.create_rectangle(x, y, x, y)

panel.mainloop()
