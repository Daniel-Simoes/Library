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
        self.title = Entry(frame)
        self.title.grid(row=1, column=1)

        Label(frame, text='Author :').grid(row=2, column=0)
        self.author = Entry(frame)
        self.author.grid(row=2, column=1)

        Label(frame, text='Genre :').grid(row=3, column=0)
        self.genre = Entry(frame)
        self.genre.grid(row=3, column=1)

        Label(frame, text='Status :').grid(row=4, column=0)
        self.status = Entry(frame)
        self.status.grid(row=4, column=1)

        ttk.Button(frame, text='Register').grid(row=5, columnspan=2, stick=W+E)


if __name__ == "__main__":
    window = Tk()
    application = Book(window)
    window.mainloop()
