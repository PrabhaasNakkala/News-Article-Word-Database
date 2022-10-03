import pyodbc
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as a


year = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def read_data(conn, w):                                                         #   gathers all data points from SQL Server and inputs
    cursor = conn.cursor()                                                      #   frequncy of the word by year into the lis array
    cursor.execute(f"select * from Stats where word = '{w}'")
    for r in cursor:
        q = int(r[3])
        m = int(r[1])
        if(q != 2022):
            lis[q-2012] += m


conn = pyodbc.connect(                                                          #   connects to the SQL Server and Table which Data is stored in
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-DH98U9PL\SQLEXPRESS;"
    "Database=hello;"
    "Trusted_Connection=yes;"   
)

root = Tk()
root.geometry("200x100")


w = ''
def getdata():                                                                  #   gets word from the input box and calls the read_data() function
    global w
    w = str(textbox.get("1.0", "end-1c"))
    read_data(conn, w)
    w = ''

    
def graph(year, lis):                                                           #   graphs data in a bar graph to show frequency per year of  word
    a.bar(year,lis)
    a.show()


textbox = Text(root, height=2, width=10)
textbox.pack()
b = Button(root, height=1, width=10, text="Read Data", command=lambda: getdata())
b2 = Button(root, height=1, width=10, text="Graph", command=lambda: graph(year, lis))
b.pack()   
b2.pack()
root.mainloop()


