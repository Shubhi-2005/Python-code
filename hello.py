#from tkinter import *
#window = Tk()
#window.title("Welcome to Adv Python Lab")
#window.geometry("1800x600+100+50")
#label = Label(window, text="today is day 5", font=("Calibri Bold", 50))
#label.config(bg="pink", fg="green")
#label.pack(side="bottom", pady=150, ipady=50)
#window.mainloop()




'''from tkinter import*
from tkinter import messagebox

def login():
    user=username.get()
    pwd=password.get()

    if user=="shubhi" and pwd=="1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid username or password.")

root=Tk()
root.title("NIET Student Login")
root.geometry("300x200")
root.resizable(False, False)

#username label and entry
Label(root, text="Username").pack(pady=5)
username=Entry(root)
username.pack()

#Password label and entry
Label(root, text="Password").pack(pady=5)
password=Entry(root, show="*")
password.pack()

#Login button
Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()'''




'''from tkinter import*
from tkinter import messagebox

def login():
    user=username.get()
    pwd=password.get()

    if user=="shubhi" and pwd=="1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid username or password.")

#create the main window
root=Tk()
root.title("NIET Student Login")
root.geometry("300x200")
root.resizable(False, False)

#username label and entry
Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10, sticky="e")
username=Entry(root)
username.grid(row=0, column=1, padx=10, pady=10)

#Password label and entry
Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10, sticky="e")
password=Entry(root, show="*")  
password.grid(row=1, column=1, padx=10, pady=10)

#Login button
Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=20)

#result label
result_label = Label(root, text="", font=("Arial", 10))
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()'''




from tkinter import *
def press(num):
    entry_var.set(entry_var.get() + str(num))

def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear():
    entry_var.set("")

root = Tk()
root.title("NIET Student Calculator")
root.geometry("500x400")
root.resizable(False,False)

entry_var = StringVar()
entry = Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, relief=RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]
for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4  else 1

    if text == '=':
        Button(root, text=text, height=2, width=32, font=('Arial', 12), command=equal)\
           .grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
    elif text == 'C':
        Button(root, text=text, height=2, width=7, font=('Arial', 12), command=clear)\
            .grid(row=row, column=col, columnspan=colspan, padx=5, pady=5) 
    else:
        Button(root, text=text, height=2, width=7, font=('Arial', 12), command=lambda t=text: press(t))\
            .grid(row=row, column=col, padx=5, pady=5)
        
root.mainloop()