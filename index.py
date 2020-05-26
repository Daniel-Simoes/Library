from tkinter import ttk
from tkinter import*

import sqlite3


class Book:

    def __init__(self, window):
        self.wind = window
        self.wind.title("New Register1")

        frame = LabelFrame(self.wind, text='Register a new book :')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        Label(frame, text='Title :').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

        Label(frame, text='Author :').grid(row=2, column=0)
        self.name = Entry(frame)
        self.name.grid(row=2, column=1)

        Label(frame, text='Genre :').grid(row=3, column=0)
        self.name = Entry(frame)
        self.name.grid(row=3, column=1)

        Label(frame, text='Status :').grid(row=4, column=0)
        self.name = Entry(frame)
        self.name.grid(row=4, column=1)


if __name__ == "__main__":
    window = Tk()
    application = Book(window)
    window.mainloop()
