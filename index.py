from tkinter import ttk
from tkinter import*

import sqlite3


class Book:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title("MyLibrary")

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

        ttk.Button(frame, text='Register', command=self.adding).grid(
            row=5, columnspan=2, stick=W+E)
        self.message = Label(text='', fg='red')
        self.message.grid(row=2, column=0)

        self.tree = ttk.Treeview(height=10, columns=("#0", "#1", "#2"))
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Title', anchor=W)
        self.tree.heading('#1', text='Author', anchor=W)
        self.tree.heading('#2', text='Genre', anchor=W)
        self.tree.heading('#3', text='Status', anchor=W)

        ttk.Button(frame, text='Delete', command=self.deleting).grid(
            row=7, column=0)
        ttk.Button(frame, text='Edit', command=self.editing).grid(
            row=7, column=1)

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
        query = 'SELECT * FROM books'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 2, text=row[1], values=(
                row[2], row[3], row[4]))

    def validation(self):
        return len(self.title.get()) != 0 and len(self.author.get()) != 0 and len(self.genre.get()) != 0 and len(self.status.get()) != 0

    def adding(self):

        if self.validation():
            query = 'INSERT INTO books VALUES (NULL, ?, ?, ?, ?)'
            parameters = (self.title.get(), self.author.get(),
                          self.genre.get(), self.status.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Book {} added'.format(
                self.title.get())
            self.title.delete(0, END)
            self.author.delete(0, END)
            self.genre.delete(0, END)
            self.status.delete(0, END)
        else:
            self.message['text'] = 'Sorry, all fields are required!'
        self.viewing_records()

    def deleting(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'please, you need chosen a book to delete:'
            return
        self.message['text'] = ''
        title = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM books WHERE title=?'
        self.run_query(query, (title,))
        self.message['text'] = 'The Book {} was deleted'.format(title)

        self.viewing_records()

    def editing(self):

        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'please, you need chosen a book to edit'
            return
        title = self.tree.item(self.tree.selection())['text']
        old_status = self.tree.item(self.tree.selection())['text'][0]

        self.edit_wind = Toplevel()
        self.edit_wind.title('Edit status')

        screen_width = self.edit_wind.winfo_screenwidth()
        screen_height = self.edit_wind.winfo_screenheight()
        width = 350
        height = 200

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)

        self.edit_wind.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.edit_wind.resizable(0, 0)

        self.edit_wind.configure(bg='Snow2')

        Label(self.edit_wind, text='Book:', bg='Snow2').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
                                                     value=title), state='readonly').grid(row=0, column=2)
        new_title = Entry(self.edit_wind)
        new_title.grid(row=1, column=2)

        Label(self.edit_wind, text='Status:', bg='Snow2').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=DoubleVar(self.edit_wind,
                                                     value=old_status), state='readonly').grid(row=2, column=2)
        new_status = Entry(self.edit_wind)
        new_status.grid(row=3, column=2)

        ttk.Button(self.edit_wind, text='Update', command=lambda: self.edit_records(
            new_title.get(), title, new_status.get(),  old_status)).grid(row=4, column=2, sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, new_title, new_status, title, old_status):
        query = 'UPDATE books SET title=?,status=? WHERE title=? AND status=?'
        parameters = (new_title, new_status, title, old_status)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Status {} book was UPDATED'.format(title)
        self.viewing_records()


if __name__ == "__main__":
    window = Tk()
    application = Book(window)
    window.mainloop()
