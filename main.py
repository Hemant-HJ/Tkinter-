from tkinter import *
from tkinter import ttk, messagebox
import sys
import os

from Mysql.data import Database
import config

mysql_data = Database()

if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', '6080')
    print('Display variable changed.')

if not config.STARTED:
    root = Tk()
    def connect():
        data = mysql_data.setup(username.get(), password.get(), host.get())
        if not data:
            messagebox.showerror(title = 'Configuration Error.', message = 'There was a error while connecting to the database.\nPlease check the credintials and Try again.')
        else:
            changed_data = {
                'username': username.get(),
                'password': password.get(),
                'host': host.get(),
                'started': True
            }
            data = config.file_write(changed_data)
            if data:
                messagebox.showinfo(title = 'Configuration Completed', message = 'Configuration is completed and now you can use the app.\nPlease start the application again.')
                root.destroy()


    root.title('Configuration Window.')
    root.geometry('300x200')
    frame = ttk.Frame(root).pack()

    username = StringVar()
    password = StringVar()
    host = StringVar()

    l_user = ttk.Label(frame, text = 'username').pack(fill = 'x', expand = True)
    e_user = ttk.Entry(frame, textvariable = username).pack(fill = 'x', expand = True)

    l_pass = ttk.Label(frame, text = 'password').pack(fill = 'x', expand = True)
    e_pass = ttk.Entry(frame, textvariable = password, show = '*').pack(fill = 'x', expand = True)

    l_host = ttk.Label(frame, text = 'host').pack(fill = 'x', expand = True)
    e_host = ttk.Entry(frame, textvariable = host).pack(fill = 'x', expand = True)

    connect_button = ttk.Button(frame, text = 'Connect', command = connect).pack(fill = 'x', expand = True)
    root.mainloop()
else:
    print(True)