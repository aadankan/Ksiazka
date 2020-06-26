from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Hi")
root.iconbitmap(r'C:\Users\aadan\Desktop\2.ico')
root.geometry("400x400")

conn = sqlite3.connect('addres_book.db')

c = conn.cursor()
'''
c.execute("""CREATE TABLE addresses (
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""") 
'''

def delete():
    conn = sqlite3.connect('addres_book.db')

    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    conn.commit()

    conn.close()

def submit():
    conn = sqlite3.connect('addres_book.db')

    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),
              })

    conn.commit()

    conn.close()


    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    conn = sqlite3.connect('addres_book.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()

    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="ID")
delete_box_label.grid(row=9, column=0, pady=5)

submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)


conn.commit()

conn.close()


mainloop()
