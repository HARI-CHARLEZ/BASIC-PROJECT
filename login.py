from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('925x500+300+200')
root.title('login')
root.resizable(False, False)
root.configure(bg='white')

#img = PhotoImage(file='img.jpg')
#image1 = Label(root, image=img, bg='white')
#image1.place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=500, y=50)

def signin():
    username = user.get()
    password = user1.get()
    if username == "admin" and password == "1234":
        response = messagebox.askquestion("Confirmation", "Are you sure?")
        if response == 'yes':
            screen = Toplevel(root)
            screen.title("Your secret")
            screen.geometry('925x500+300+200')
            screen.config(bg='white')
            screen1 = Label(screen, text='Hello everyone!', bg='#fff', font=('poppins', 50, 'bold'))
            screen1.pack(expand=True)

def clear_entry(event, entry):
    entry.delete(0, 'end')

def reset_entry(event, entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)

user = Entry(root, width=25, fg="black", border=0, bg='white', font=('microsoft YaHei UI Light', 11))
user.place(x=550, y=180)
user.insert(0, 'username')
user.bind('<FocusIn>', lambda event: clear_entry(event, user))
user.bind('<FocusOut>', lambda event: reset_entry(event, user, 'username'))

user1 = Entry(root, width=25, fg="black", border=0, bg='white', font=('microsoft YaHei UI Light', 11))
user1.place(x=550, y=240)
user1.insert(0, 'password')
user1.bind('<FocusIn>', lambda event: clear_entry(event, user1))
user1.bind('<FocusOut>', lambda event: reset_entry(event, user1, 'password'))

Frame(root, width=295, height=2, bg='black').place(x=550, y=210)
Frame(root, width=295, height=2, bg='black').place(x=550, y=265)

Button(root, text='Submit', fg='white', border=0, bg='#57a1f8', padx=125, pady=10, command=signin).place(x=550, y=310)

Label(root, text='Sign in', bg='white', fg='#57a1f8', font=('microsoft YaHei UI Light', 23, 'bold')).place(x=630, y=50)

root.mainloop()
