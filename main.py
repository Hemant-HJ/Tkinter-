import tkinter 
from tkinter import *
import sys
import os
import config

if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', '6080')
    print('Display variable changed.')



root = Tk()
root.title('test')

root.mainloop()