# drawingpanel.py

from Tkinter import *
import time

'''
DrawingPanel objects represent a simple interface for creating
graphical windows in Python.

Author : Marty Stepp (stepp AT cs.washington.edu)
Version: 2008/10/13
'''
class DrawingPanel(Tk):
    '''
    Constructs a panel of the given width, height, and optional background color.

    Keyword arguments:
    width -- width of the DrawingPanel in pixels (default 500)
    height -- height of the DrawingPanel in pixels (default 500)
    background -- background color of the DrawingPanel (default "white")
    '''
    def __init__(self, width=500, height=500, background="white"):
        Tk.__init__(self)
        self.width = width
        self.height = height
        self.title("DrawingPanel")
        self.canvas = Canvas(self, width = width + 1, height = height + 1)
        self.canvas["bg"] = background
        self.canvas.pack({"side": "top"})
        self.wm_resizable(0, 0)
        self.update()

    '''
    Sets the panel's background color to be the given color.

    Keyword arguments:
    color -- the color to set, as a string such as "yellow" or "black"
    '''
    def set_background(self, color):
        self.canvas["bg"] = color

    '''
    Causes the DrawingPanel to pause for the given number of milliseconds.
    Useful for creating simple animations.

    Keyword arguments:
    ms -- number of milliseconds to pause
    '''
    def sleep(self, ms):
        try:
            self.update()
            time.sleep(ms / 1000.0)
            self.update()
        except Exception:
            pass
