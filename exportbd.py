import mysql.connector
import json
import tkinter as tk

connection = mysql.connector.connect(host="localhost",
                                         database="test",
                                         user="root",
                                         password="root")
window = tk.Tk()
window.minsize(500, 200)

def bd():                                         
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM login")
    result = cursor.fetchall()
    with open('data.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
        for i in range(len(data)): 
                sql = "INSERT INTO login (name, password) VALUES (%s, %s)"
                cursor.execute(sql, (data[i][0], data[i][1]))
                connection.commit()    


button = tk.Button(
    text="export",
    width=20,
    height=5,
    command=bd
    )


button.pack()

window.mainloop()












