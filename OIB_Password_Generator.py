import customtkinter
from tkinter import *
import string
import random


app = customtkinter.CTk()
app.title('Random Password Generator')
app.geometry('650x300')
app.config(bg="#C8A2C8")

words = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation
selection_list = words + numbers + special_chars
password = ''
def pass_word():
    password_len = int(new_data.get())
    print(password_len)
    global password
    if password_len>12 or password_len<5:
        check_label.configure(text="*the password length min = 5 and max = 12*")
    else:
        check_label.configure(text="")
        for _ in range(int(password_len)):
            password+= ''.join(random.choice(selection_list))
            result.configure(text=f"Your Password is: {password}")
    
    

label1 = customtkinter.CTkLabel(app,text="Welcome to Random Password Generator!!!",text_color='#000',font=('sitika',14,'bold'),bg_color="#C8A2C8")
label1.place(x=20,y=20)

label2 = customtkinter.CTkLabel(app,text="Kindly enter the length of the password you need:",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
label2.place(x=20,y=80)

new_data = customtkinter.CTkEntry(app)
new_data.place(x=430,y=80)

check_label = customtkinter.CTkLabel(app,text="",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
check_label.place(x=300,y=160)

calulate_button =customtkinter.CTkButton(app,command=pass_word, text="Generate Password", font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
calulate_button.place(x=30,y=160)

result = customtkinter.CTkLabel(app,text="",font=('sitika',14,'bold'),text_color='#000',bg_color="#C8A2C8")
result.place(x=30,y=260)


app.mainloop()


