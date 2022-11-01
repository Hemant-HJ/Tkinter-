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

    l_user = ttk.Label(frame, text = 'Username').pack()
    e_user = ttk.Entry(frame, textvariable = username).pack()

    l_pass = ttk.Label(frame, text = 'Password').pack()
    e_pass = ttk.Entry(frame, textvariable = password, show = '*').pack()

    l_host = ttk.Label(frame, text = 'Host').pack()
    e_host = ttk.Entry(frame, textvariable = host).pack()

    connect_button = ttk.Button(frame, text = 'Connect', command = connect).pack()
    root.mainloop()
else:
    class MainWindow(Tk):
        def __init__(self):
            super().__init__()
            self.title('Management')
            self.geometry('300x250')
            self.resizable(False, False)

            frame = ttk.Frame().pack()

            l_insert = ttk.Label(frame , text = 'Insert Data').place(x = 20, y = 40)
            b_insert = ttk.Button(frame, text = 'Insert', command = self.open_insert_window).place(x = 140, y = 40)

            l_update = ttk.Label(frame, text = 'Update Data').place(x = 20, y = 80)
            b_update = ttk.Button(frame, text = 'Update', command = self.open_update_window).place(x = 140, y = 80)

            l_delete = ttk.Label(frame, text = 'Delete Data').place(x = 20, y = 120)
            b_delete = ttk.Button(frame, text = 'Delete', command = self.open_delete_window).place(x = 140, y = 120)

            l_select = ttk.Label(frame, text = 'Selete Data').place(x = 20, y = 160)
            b_delete = ttk.Button(frame, text = 'Select', command = self.open_select_window).place(x = 140, y = 160)

            c_close = ttk.Button(frame, text = 'Close', command = self.destroy).place(x = 180, y = 200)

        def open_insert_window(self):
            insert_window = InsertWindow(self)
            insert_window.grab_set()

        def open_update_window(self):
            update_window = UpdateWindow(self)
            update_window.grab_set()

        def open_delete_window(self):
            delete_window = DeleteWindow(self)
            delete_window.grab_set()

        def open_select_window(self):
            select_window = SelectWindow(self)

    class InsertWindow(Toplevel):
        def __init__(self, parent):
            super().__init__(parent)

            self.title('Insert Window.')
            self.resizable(False, False)
            self.geometry('400x200')

            self.insert_frame = ttk.Frame(self)
            self.insert_frame.pack()

            ttk.Label(self.insert_frame, text = 'Please select a table').pack(fill = X, padx = 5, pady = 5)

            self.table_selected = StringVar()

            table = ttk.Combobox(self.insert_frame, textvariable = self.table_selected)
            table['state'] = 'readonly'
            table['values'] = mysql_data.query.tables
            table.pack(fill = X, padx = 5, pady = 5)
            table.bind('<<ComboboxSelected>>', self.table_select)

        def table_button_Item(self):
            if '' in [self.item_name_var.get(), self.item_desc_var.get(), self.item_pric_var.get()]:
                messagebox.showerror(title = 'Value Error', message = 'Any of the value cannot be empty.')
                return
            else:
                data = mysql_data.insert(self.table_name.lower(), [self.item_name_var.get(), self.item_cate_var.get(), self.item_desc_var.get(), self.item_pric_var.get()])
                if data == True:
                    messagebox.showinfo(title = 'Success', message = f'Added the item with {self.item_name_var.get().title()}')
                    self.destroy()
                else:
                    messagebox.showerror(title = 'Error', message = f'{data}')
                    self.destroy()

        def table_button_Inv(self):
            if '' in [self.item_code_var.get(), self.item_stock_var.get()]:
                messagebox.showerror(title = 'Value Error', message = 'Any of the value cannot be empty.')
                return
            else:
                data = mysql_data.insert(self.table_name.lower(), [self.item_code_var.get(), self.item_stock_var.get()])
                if data == True:
                    messagebox.showinfo(title = 'Success', message = f'Added the item stock for {self.item_code_var.get()}')
                    self.destroy()
                else:
                    messagebox.showerror(title = 'Error', message = f'{data}')
                    self.destroy()

        def table_button_Cust(Self):
            if '' in [self.cust_name_var.get(), self.cust_addr_var.get(), self.cust_phon_var.get(), self.cust_mail_var.get()]:
                messagebox.showerror(title = 'Value Error', message = 'Any of the value cannot be empty.')
                return
            else:
                data = mysql_data.insert(self.table_name.lower(), [self.cust_name_var.get(), self.cust_addr_var.get(), self.cust_phon_var.get(), self.cust_mail_var.get()])
                if data == True:
                    messagebox.showinfo(title = 'Success', message = f'Added the Customer {self.cust_name_var.get().title()}')
                    self.destroy()
                else:
                    messagebox.showerror(title = 'Error', message = f'{data}')
                    self.destroy()

        def table_button_Sale(self):
            if '' in [self.sale_item_var.get(), self.sale_cust_var.get(), self.sale_price_var.get()]:
                messagebox.showerror(title = 'Value Error', message = 'Any of the value cannot be empty.')
                return
            else:
                data = mysql_data.insert(self.table_name.lower(), [self.sale_item_var.get(), self.sale_cust_var.get(), self.sale_price_var.get()])
                if data == True:
                    messagebox.showinfo(title = 'Success', message = f'Added Sale Entry for customer {self.sale_cust_var.get().title()}')
                    self.destroy()
                else:
                    messagebox.showerror(title = 'Error', message = f'{data}')
                    self.destroy()

        def table_button_Adv(self):
            if '' in [self.adv_cust_var.get(), self.adv_loan_var.get()]:
                messagebox.showerror(title = 'Value Error', message = 'Any of the value cannot be empty.')
                return
            else:
                data = mysql_data.insert(self.table_name.lower(), [self.adv_cust_var.get(), self.adv_loan_var.get()])
                if data == True:
                    messagebox.showinfo(title = 'Success', message = f'Added Loan for customer with {self.adv_cust_var.get()} id.')
                    self.destroy()
                else:
                    messagebox.showerror(title = 'Error', message = f'{data}')
                    self.destroy()

        def table_select(self, event):
            self.table_name = self.table_selected.get()
            for widget in self.insert_frame.winfo_children():
                widget.destroy()
            
            if self.table_name == 'Item':
                self.item_name_var = StringVar()
                self.item_cate_var = StringVar()
                self.item_desc_var = StringVar()
                self.item_pric_var = StringVar()

                l_item_name = ttk.Label(self.insert_frame, text = 'Item Name').pack()
                e_item_name = ttk.Entry(self.insert_frame, textvariable = self.item_name_var).pack()

                l_item_cate = ttk.Label(self.insert_frame, text = 'Item Category').pack()
                c_item_cate = ttk.Combobox(self.insert_frame, textvariable = self.item_cate_var)
                c_item_cate['state'] = 'readonly'
                c_item_cate['values'] = ['General', 'Stationary', 'Metal', 'Food']
                c_item_cate.pack()

                l_item_desc = ttk.Label(self.insert_frame, text = 'Item Description').pack()
                e_item_desc = ttk.Entry(self.insert_frame, textvariable = self.item_desc_var).pack()

                l_item_pric = ttk.Label(self.insert_frame, text = 'Item Price').pack()
                e_item_pric = ttk.Entry(self.insert_frame, textvariable = self.item_pric_var).pack()

                confirm = ttk.Button(self.insert_frame, text = 'Confirm', command = self.table_button_Item).pack()

            elif self.table_name == 'Inventory':
                self.item_code_var = StringVar()
                self.item_stock_var = StringVar()

                l_item_code = ttk.Label(self.insert_frame, text = 'Item Code').pack()
                e_item_code = ttk.Entry(self.insert_frame, textvariable = self.item_code_var).pack()

                l_item_stock = ttk.Label(self.insert_frame, text = 'Item Stock').pack()
                e_item_stock = ttk.Entry(self.insert_frame, textvariable = self.item_stock_var).pack()

                confirm = ttk.Button(self.insert_frame, text = 'Confirm', command = self.table_button_Inv).pack()

            elif self.table_name == 'Customer':
                self.cust_name_var = StringVar()
                self.cust_addr_var = StringVar()
                self.cust_phon_var = StringVar()
                self.cust_mail_var = StringVar()

                l_cust_name = ttk.Label(self.insert_frame, text = 'Customer Name').pack()
                e_cust_name = ttk.Entry(self.insert_frame, textvariable = self.cust_name_var).pack()

                l_cust_addr = ttk.Label(self.insert_frame, text = 'Customer Address').pack()
                e_cust_addr = ttk.Entry(self.insert_frame, textvariable = self.cust_addr_var).pack()
                
                l_cust_phon = ttk.Label(self.insert_frame, text = 'Customer Phone no').pack()
                e_cust_phon = ttk.Entry(self.insert_frame, textvariable = self.cust_phon_var).pack()

                l_cust_mail = ttk.Label(self.insert_frame, text = 'Customer Email').pack()
                e_cust_mail = ttk.Entry(self.insert_frame, textvariable = self.cust_mail_var).pack()

                confirm = ttk.Button(self.insert_frame, text = 'Confirm', command = self.table_button_Cust).pack()

            elif self.table_name == 'Sales':
                self.sale_item_var = StringVar()
                self.sale_cust_var = StringVar()
                self.sale_price_var = StringVar()

                l_sale_item = ttk.Label(self.insert_frame, text = 'Item Code').pack()
                e_sale_item = ttk.Entry(self.insert_frame, textvariable = self.sale_item_var).pack()

                l_sale_cust = ttk.Label(self.insert_frame, text = 'Customer Name').pack()
                e_sale_cust = ttk.Entry(self.insert_frame, textvariable = self.sale_cust_var).pack()
                
                l_sale_price = ttk.Label(self.insert_frame, text = 'Item Price').pack()
                e_sale_price = ttk.Entry(self.insert_frame, textvariable = self.sale_price_var).pack()

                confirm = ttk.Button(self.insert_frame, text = 'Confirm', command = self.table_button_Sale).pack()

            elif self.table_name == 'Advances':
                self.adv_cust_var = StringVar()
                self.adv_loan_var = StringVar()
                
                l_adv_cust = ttk.Label(self.insert_frame, text = 'Customer Code').pack()
                e_adv_cust = ttk.Entry(self.insert_frame, textvariable = self.adv_cust_var).pack()

                l_adv_loan = ttk.Label(self.insert_frame, text = 'Loan Added').pack()
                e_adv_loan = ttk.Entry(self.insert_frame, textvariable = self.adv_loan_var).pack()
                
                confirm = ttk.Button(self.insert_frame, text = 'Confirm', command = self.table_button_Adv).pack()

    class UpdateWindow(Toplevel):
        def __init__(self, parent):
            super().__init__(parent)

            self.title('Update Window.')
            self.geometry('400x200')
    
    class DeleteWindow(Toplevel):
        def __init__(self, parent):
            super().__init__(parent)

            self.title('Delete Window.')
            self.geometry('400x200')
            self.delete_frame = ttk.Frame(self)
            self.delete_frame.pack()

            ttk.Label(self.delete_frame, text = 'Tables').pack()

            self.table_selected = StringVar()
            table = ttk.Combobox(self.select_frame, textvariable = self.table_selected)
            table['state'] = 'readonly'
            table['values'] = mysql_data.query.tables
            table.pack()
            table.bind('<<ComboboxSelected>>', self.table_select)

        def table_select(self, event):
            self.table_name = self.table_selected.get()

            window = self.Selected_Table(self, self.table_name)

        class SelectedTable(Toplevel):
            def __init__(self, parent, table):
                self.table = table.lower()
                super().__init__(parent)

                self.title(self.table)
                self.selected_table_f = ttk.Frame(self)
                self.selected_table_f.pack()

                columns = mysql_data.query.table_attributes(self.table.lower())

                tree = ttk.Treeview(self.selected_table_f, columns = columns, show = 'headings')
                for column in columns:
                    tree.heading(column, text = column.title())

                data = mysql_data.select(self.table.lower())
                if type(data) == type([]):
                    for entry in data:
                        tree.insert('', END, values = entry)
                else:
                    messagebox.showerror(title = 'Error', message = data)

                tree.bind('<<TreeviewSelect>>', self.data_select)
                self.tree = tree

            def data_select(self, event):
                if self.table == 'item':
                    self.delete_key = 'icode'
                elif self.table == 'inventory':
                    self.delete_key = 'icode'
                elif self.table == 'customer':
                    self.delete_key = 'ccode'
                elif self.table == 'sales':
                    self.delete_key = 'scode'
                elif self.table == 'advances':
                    self.delete_key = 'ccode'

                self.delete_key_id = []
                
                for data in self.tree.selection():
                    record_id = self.tree.item(data)['values'][self.delete_key]
                    self.delete_key_id.append(record_id)
                messagebox.showwarning(title = 'Warning', message = 'You are about to delete the selected items.')
                for id in self.delete_key_id:
                    mysql_data.delete(self.table, id)

                for data in self.tree.selection():
                    self.tree.delete(data)


    class SelectWindow(Toplevel):
        def __init__(self, parent):
            super().__init__(parent)

            self.title('Select Window.')
            self.geometry('400x200')
            self.select_frame = ttk.Frame(self)
            self.select_frame.pack()

            ttk.Label(self.select_frame, text = 'Tabel').pack()

            self.table_selected = StringVar()

            table = ttk.Combobox(self.select_frame, textvariable = self.table_selected)
            table['state'] = 'readonly'
            table['values'] = mysql_data.query.tables
            table.pack()
            table.bind('<<ComboboxSelected>>', self.table_select)

        def table_select(self, event):
            self.table_name = self.table_selected.get()

            window = self.SelectedTable(self, self.table_name)

        class SelectedTable(Toplevel):
            def __init__(self, parent, table):
                self.table = table
                super().__init__(parent)

                self.title(self.table)
                self.selected_table_f = ttk.Frame(self)
                self.selected_table_f.pack()

                ttk.Label(self.selected_table_f, text = 'Data').pack()

                columns = mysql_data.query.table_attributes(self.table.lower())

                tree = ttk.Treeview(self.selected_table_f, columns = columns, show = 'headings')
                for column in columns:
                    tree.heading(column, text = column.title())

                data = mysql_data.select(self.table.lower())
                if type(data) == type([]):
                    for entry in data:
                        tree.insert('', END, values = entry)
                else:
                    messagebox.showerror(title = 'Error', message = data)

    
    mainWindow = MainWindow()
    mainWindow.mainloop()