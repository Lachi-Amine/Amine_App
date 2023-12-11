import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import sqlite3
import hashlib
from tkinter import font
from typing import TypeVar
import os
import sys

# connect the py file with the database
connection = sqlite3.connect("DB.db")
# create the road cursur between the db and the py file
cursur = connection.cursor()
cursur.execute(
    ''' create table if not exists accounts(user text,password text)''')  # // use it when the db deleted//

# white window
page = Tk()
# page.config(bg="....") // bg color //
# height & width // and place of desplay//
page.geometry("720x450+270+100")

# Zoom out & Zoom in
page.resizable(False, False)

# the pop up title
page.title("Amine app")

# the pop up icon
page.iconbitmap("C:\\Users\\Twich\\Desktop\\Amine app\\img\\man.ico")

# big title
title = Label(page, text="Amine app", height=1,
              font=("Arial", 24), fg="white", bg="black")

# desplay the title & color the line
title.pack(fill=X)

# cut the window
right_f = Frame(width=250, height=430, bg="#222")
right_f.place(x=470, y=30)

# right Frame labels

label1 = Label(right_f, text="Lachi Mohamed Amine ", fg="white",
               bg="#222", height=1, font=("Arial", 14))
label1.place(x=25, y=10)

btn_label = Label(right_f, text="About us :", fg="white",
                  bg="#222", height=1, font=("Arial", 14))
btn_label.place(x=25, y=150)

# prepare the buttton functions
# facebook function


def facebook():
    webbrowser.open_new(
        "https://www.facebook.com/profile.php?id=100067744867658")
    # instagram function


def instagram():
    webbrowser.open_new("https://www.instagram.com/animeminooo/")
    # email function


def email():
    webbrowser.open_new("https://fr.mail.yahoo.com/d/folders/1")

# right Frame buttons


btn1 = Button(right_f, width=30, height=1, borderwidth=1,
              text="Facebook", command=facebook)
btn1.place(x=18, y=185)

btn2 = Button(right_f, width=30, height=1, borderwidth=1,
              text="Instagram", command=instagram)
btn2.place(x=18, y=220)

btn3 = Button(right_f, width=30, height=1, borderwidth=1,
              text="e-mail", command=email)
btn3.place(x=18, y=255)

btn4 = Button(right_f, width=30, height=1,
              borderwidth=1, text="Exit", command=quit)
btn4.place(x=18, y=380)

# login

# profil image
ph = PhotoImage(file="C:\\Users\\Twich\\Desktop\\Amine app\\img\\profil.png")
pho = Label(page, image=ph)
pho.place(x=175, y=50)

# user name input & image
l = PhotoImage(file="C:\\Users\\Twich\\Desktop\\Amine app\\img\\lock.png")
lock = Label(page, image=l)
lock.place(x=300, y=200)

a = Text()
lock_in = Entry(page, width=16, bg="black", justify="center",
                fg="white", font=("Arial", 12, "bold"), textvariable=a)
lock_in.place(x=140, y=210)


# password input & image
k = PhotoImage(file="C:\\Users\\Twich\\Desktop\\Amine app\\img\\key.png")
key = Label(page, image=k)
key.place(x=300, y=270)

b = Text()
key_in = Entry(page, width=16, bg="black", justify="center",
               fg="white", font=("Arial", 12, "bold"), textvariable=b)
key_in.place(x=140, y=280)

# create new account function


def to_sign():
    if1 = lock_in.get()
    if2 = key_in.get()
    connection = sqlite3.connect("DB.db")
    cursur = connection.cursor()
    if len(if1) != 0 and len(if2) != 0:
        user_name = connection.execute(
            f"""SELECT user FROM accounts where user='{if1}'""").fetchone()
        if user_name != None:
            messagebox.showerror(
                "error", "Sorry!!!, that user name is taken , Please try again")
        else:
            H_if1 = hashlib.sha512(b'{if1}').hexdigest()
            H_if2 = hashlib.sha512(b'{if2}').hexdigest()
            cursur.execute(
                "insert into accounts (user , password) values (? , ?) ", (H_if1, H_if2))
            messagebox.showinfo(
                "correct", "Your account has been created !!!")

    else:
        messagebox.showerror(
            "error", "Your user name or your password is empty")
    connection.commit()


# create new account buttton
signup_bt = Button(page, width=10, height=1, borderwidth=0,
                   text="sign in now", font=("Arial", 12), command=to_sign)
signup_bt.place(x=260, y=342)

# login function


def to_log():
    if1 = lock_in.get()
    if2 = key_in.get()
    connection = sqlite3.connect("DB.db")
    cursur = connection.cursor()
    if len(if1) != 0 and len(if2) != 0:
        H_if1 = hashlib.sha512(b'{if1}').hexdigest()
        H_if2 = hashlib.sha512(b'{if2}').hexdigest()
        user_name = connection.execute(
            f"""SELECT password FROM accounts where user='{H_if1}'""").fetchone()
        if not user_name:
            messagebox.showerror(
                "error", "There is no account with this name")
        elif user_name[0] == H_if2:
            page.command(quit)
            compte = Tk()
            compte.geometry("720x450+270+100")
            compte.resizable(False, False)
            page.title("Your account")
            page.iconbitmap("C:\\Users\\Twich\\Desktop\\Amine app\\img\\man.ico")
            compte.mainloop()
        else:
            messagebox.showerror(
                "error", "The password or the username  is incorrect please try again ")
    else:
        messagebox.showerror(
            "error", "Your user name or your password is empty")
    connection.commit()


# login button
login_bt = Button(page, width=10, height=1, borderwidth=1, text="login", font=(
    "Arial", 16, "bold"), bg="#222", fg="white", command=to_log)
login_bt.place(x=120, y=330)


# cut the window // new bottem frame
left_f = Frame(width=470, height=50, bg="#222")
left_f.place(x=0, y=400)

# do the above commands // or I will kill you //
connection.commit()
#  close the db
connection.close()
# will close the window if I want
page.mainloop()
