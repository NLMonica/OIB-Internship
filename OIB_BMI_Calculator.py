import customtkinter
from tkinter import *
from tkinter import messagebox
import sqlite3 
from matplotlib import pyplot as plt

app = customtkinter.CTk()
app.title('BMI Calculator')
app.geometry('400x400')
app.config(bg="#C8A2C8")
height = 0
weight = 0
name = ''


conn = sqlite3.connect('Records.db') 
cursor = conn.cursor() 


def check_table_exist(name):
    table_query = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(table_query)
    tables_list = []

    for tables in cursor.fetchall():
        tables_list.append(tables[0])

    if name in tables_list:
        print("Table exists")
    else:
        table = f"CREATE TABLE {name} (height REAL, weight REAL, bmi REAL);"
        cursor.execute(table)



def insert_into_table(name, height,weight, bmi):
    check_table_exist(name)
    insert_query = f"INSERT INTO {name} VALUES ({height},{weight},{bmi});"
    cursor.execute(insert_query)
    debug_query = f"SELECT * FROM {name};"
    cursor.execute(debug_query)
    for i in cursor.fetchall():
        print(i) 
    conn.commit()



def plot_graph():
    print("PLOTTING THE GRAPH")
    data = f"SELECT * FROM {name}"
    cursor.execute(data)
    x = []
    y = []
    for i in cursor.fetchall():
        x.append(i[0])
        y.append(i[1])
    plt.plot(x,y)
    plt.show()


def calculate_bmi():
    try:
        global height
        global weight
        global name
        height = float(height_data.get())
        weight = float(weight_data.get())
        name = name_data.get()

        bmi = round(weight/(height*height),2)
        result.configure(text=f"Your BMI is :{str(bmi)}")
        if bmi < 18.5:
            x = 'Underweight'
        if bmi>=18.5 and bmi<25:
            x = "Normal"
        if bmi >= 25 and bmi < 30:
            x = 'Overweight'
        if bmi >= 30:
            x = 'Obese'
        category.configure(text=f"You are :{x}")
        insert_into_table(name,height,weight,bmi)
    
    except ValueError:
        messagebox.showerror(ValueError,"Enter a valid number!")
    except ZeroDivisionError:
        messagebox.showerror('Error','value cannot be 0!')
    
    

heading_label = customtkinter.CTkLabel(app,text="Welcome to BMI Calculator!!!",text_color='#000',font=('sitika',14,'bold'),bg_color="#C8A2C8")
heading_label.place(x=20,y=20)

weight_label = customtkinter.CTkLabel(app,text="Enter Your Weight in Kgs",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
weight_label.place(x=20,y=90,)

height_label = customtkinter.CTkLabel(app,text="Enter Your Height in Mtr",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
height_label.place(x=20,y=130)

name_label = customtkinter.CTkLabel(app, text="Enter Your Name",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
name_label.place(x=20, y=50)

weight_data = customtkinter.CTkEntry(app)
weight_data.place(x=200,y=90)

height_data = customtkinter.CTkEntry(app)
height_data.place(x=200,y=130)

name_data = customtkinter.CTkEntry(app)
name_data.place(x=200,y=50)

calulate_button =customtkinter.CTkButton(app,command=calculate_bmi,text="Calculate BMI", font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
calulate_button.place(x=30,y=230)

graph_button = customtkinter.CTkButton(app,text="Show Graph",command=plot_graph, font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
graph_button.place(x=30,y=350)

category=customtkinter.CTkLabel(app,text="",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
category.place(x=30,y=280)

result = customtkinter.CTkLabel(app,text="",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
result.place(x=20,y=320)



app.mainloop()




#{"Monica":{weight:[128,78,213],height:[1290,3687,398],bmi_res:[12,45,67]}}

#Monica, weight, height -> calculate -> in parallel to display result, add height weight and bmi_res to dictionary, write this disctionary to json file.
#When yuo want to see the BMI graph, click see BMI graph button, read the json file, get the data for name specified in input box.
#Plot the graog for data you read.
