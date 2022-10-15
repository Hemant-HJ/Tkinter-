import tkinter 
from tkinter import *
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', '6080')
root = Tk()
root.title('test')

root.mainloop()