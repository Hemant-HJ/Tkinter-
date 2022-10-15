import tkinter 
from tkinter import *
import sys
import os

if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', '6080')

root = Tk()
root.title('test')

root.mainloop()