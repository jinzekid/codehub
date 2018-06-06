#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python
'''
import sys
from tkinter import *
widget = Button(None, text='Hello widget world', command=sys.exit)
widget.pack()
widget.mainloop()
'''

import sys
from tkinter import *
def quit():
    print('Hello, I must be going...')
    widget_label = Label(text='I press button!').pack(expand=YES, fill=BOTH)
    mainloop()
    #sys.exit()

widget = Button(None, text='Hello widget event world', command=quit)
widget.pack()
widget.mainloop()

