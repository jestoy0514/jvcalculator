#!/usr/bin/env python3


from tkinter import *
from tkinter.ttk import *

from jvparser import JVParser


class MainWindow:

    def __init__(self, master, st):
        self.master = master
        self.st = st
        self.appgui()

    def appgui(self):
        self.st.configure('TButton',
                          foreground='green',
                          font=("Helvetica", 15, "bold")
                          )
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.filemenu = Menu(self.menubar)
        self.helpmenu = Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.filemenu.add_command(label="Quit", command=self.master.destroy)
        self.frame1 = Frame(self.master)
        self.frame1.pack(fill='both', padx=10, pady=10)
        self.frame2 = Frame(self.master)
        self.frame2.pack(padx=10, pady=10)

        self.display = Entry(self.frame1,
                             justify='right',
                             font=("Helvetica", 17, "bold"))
        self.display.pack(fill='both')
        self.display.insert(END, "0")
        self.display.focus_set()
        self.display.bind("<KeyPress>", self.check_char)
        self.master.protocol("WM_DELETE_WINDOW", self.master.destroy)
        self.list_buttons = ("C", "/", "*", "\u21e6",
                             "7", "8", "9", "-",
                             "4", "5", "6", "+",
                             "1", "2", "3", "=",
                             "0", "."
                             )

        r = 0
        c = 0
        for elem in self.list_buttons:
            if c == 4:
                c = 0
                r += 1
            button = Button(self.frame2, text=elem, style='TButton')
            if elem == "=":
                button.grid(row=r, column=c, rowspan=2, sticky='nesw')
            elif elem == "0":
                button.grid(row=r, column=c, columnspan=2, sticky='nesw')
            elif elem == ".":
                button.grid(row=r, column=c+1)
            else:
                button.grid(row=r, column=c)
            button.configure(command=lambda
                             value=elem:
                             self.calc_result(value)
                             )
            c += 1

    def calc_result(self, value):
        #  Check if the default string is "0" or "0.0"
        #  If so delete the "0" and replace by empty "".
        check_zero = self.display.get()
        if check_zero == "0" or check_zero == "0.0":
            self.display.delete(0, END)
        #  Check which button the user press.
        #  If so insert the value for the
        #  corresponding button or do the
        #  calculation if it press "=" char.
        if value == self.list_buttons[0]:
            self.display.delete(0, END)
            self.display.insert(END, "0")
        elif value == self.list_buttons[1]:
            self.display.insert(END, "/")
        elif value == self.list_buttons[2]:
            self.display.insert(END, "*")
        elif value == self.list_buttons[3]:
            temp_char = self.display.get()
            temp_char = temp_char[0:-1]
            self.display.delete(0, END)
            self.display.insert(END, temp_char)
        elif value == self.list_buttons[4]:
            self.display.insert(END, value)
        elif value == self.list_buttons[5]:
            self.display.insert(END, value)
        elif value == self.list_buttons[6]:
            self.display.insert(END, value)
        elif value == self.list_buttons[7]:
            self.display.insert(END, value)
        elif value == self.list_buttons[8]:
            self.display.insert(END, value)
        elif value == self.list_buttons[9]:
            self.display.insert(END, value)
        elif value == self.list_buttons[10]:
            self.display.insert(END, value)
        elif value == self.list_buttons[11]:
            self.display.insert(END, value)
        elif value == self.list_buttons[12]:
            self.display.insert(END, value)
        elif value == self.list_buttons[13]:
            self.display.insert(END, value)
        elif value == self.list_buttons[14]:
            self.display.insert(END, value)
        elif value == self.list_buttons[15]:
            string_inp = self.display.get()
            result = JVParser(string_inp).calculate()
            self.display.delete(0, END)
            self.display.insert(END, str(result))
            self.display.focus_set()
        elif value == self.list_buttons[16]:
            self.display.insert(END, value)
        elif value == self.list_buttons[17]:
            self.display.insert(END, value)

    def check_char(self, event):
        #  Check whether the display value is 0 or 0.0
        #  If so delete the display before entering any
        #  numbers.
        if self.display.get() == "0" or self.display.get() == "0.0":
            self.display.delete(0, END)
        #  Check if the return key is press.
        #  If so return the computed value in the display.
        if event.keycode == 13:
            string_inp = self.display.get()
            result = JVParser(string_inp).calculate()
            self.display.delete(0, END)
            self.display.insert(END, str(result))
            self.display.focus_set()
        #  Check if character is not in numerical, if so
        #  delete the character so that error will be minimize.
        elif event.char not in ".0123456789*/+-":
            temp_str = self.display.get()
            temp_str = temp_str[0:-1]
            self.display.delete(0, END)
            self.display.insert(END, temp_str)


def main():
    app = Tk()
    #  Declare the styling.
    s = Style()
    MainWindow(app, s)
    app.title("JVCalculator")
    app.mainloop()


if __name__ == "__main__":
    main()
