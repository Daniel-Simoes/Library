from tkinter import ttk
from tkinter import*

import sqlite3


class Book:

    db_name = 'database.db'

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

        ttk.Button(frame, text='Register').grid(
            row=5, columnspan=2, stick=W+E)

        self.tree = ttk.Treeview(height=10, columns=("#0", "#1", "#2"))
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Title')
        self.tree.heading('#1', text='Author')
        self.tree.heading('#2', text='Genre')
        self.tree.heading('#3', text='Status')

        self.viewing_records()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
            return query_result

    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM book ORDER BY title DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])


if __name__ == "__main__":
    window = Tk()
    application = Book(window)
    window.mainloop()
