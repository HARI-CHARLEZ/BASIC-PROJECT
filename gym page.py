from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.geometry('925x500+300+200')
root.title('login')
root.resizable(False, False)
root.configure(bg='black')
#------------logic--------------------#
#its for age 12 to 18-----------------
def submit():
    age=entry.get()
    weight=entry1.get()
    if('40' <= weight <= '70' and '12'<=age <='18'):
        response = messagebox.askquestion("Confirmation", "Are you sure?")
        if response == 'yes':
            screen = Toplevel(root)
            screen.title("Your guide")
            screen.geometry('925x500+300+200')
            screen.config(bg='black')
            screen_=Label(screen,text='ITS A PERFECT WORKOUT FOR YOU ',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen1 = Label(screen, text='1. Cardiovascular Exercise (3-5 times per week)',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen2 = Label(screen, text='2. Strength Training (2-3 times per week)',bg='black',fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen3 = Label(screen, text='3.Cardiovascular Exercise (3-5 times per week)- 30-60 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen4 = Label(screen, text='4,Strength Training (2-3 times per week)- 45-60 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen5 = Label(screen, text='5.Flexibility and Stretching (Daily) - 10-15 minute',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen_.place(x=300,y=50)
            screen1.place(x=250,y=100)
            screen2.place(x=250,y=150)
            screen3.place(x=250,y=200)
            screen4.place(x=250,y=250)
            screen5.place(x=250,y=300)

    #its for age 18 to 25--------------------------
    elif('50' <= weight <= '80' and '18'<=age <='25'):
        response = messagebox.askquestion("Confirmation", "Are you sure?")
        if response == 'yes':
            screen = Toplevel(root)
            screen.title("Your guide")
            screen.geometry('925x500+300+200')
            screen.config(bg='black')
            screen_=Label(screen,text='ITS A PERFECT WORKOUT FOR YOU ',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen1 = Label(screen, text='1. Cardiovascular Exercise (3-5 times per week)',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen2 = Label(screen, text='2. High-Intensity Interval Training (HIIT) (1-2 times per week) - 20-30 minutes',bg='black',fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen3 = Label(screen, text='3. Strength Training (3-4 times per week) - 45-60 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen4 = Label(screen, text='4. Flexibility and Mobility Training (2-3 times per week) - 15-30 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen5 = Label(screen, text='5. Active Recreation or Sports (1-2 times per week) - Varies',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen_.place(x=300,y=50)
            screen1.place(x=250,y=100)
            screen2.place(x=250,y=150)
            screen3.place(x=250,y=200)
            screen4.place(x=250,y=250)
            screen5.place(x=250,y=300)   
    #its for age 25 to 40

    elif( '60' <= weight <='90' and '25'<=age <='40'):
        response = messagebox.askquestion("Confirmation", "Are you sure?")
        if response == 'yes':
            screen = Toplevel(root)
            screen.title("Your guide")
            screen.geometry('925x500+300+200')
            screen.config(bg='black')
            screen_=Label(screen,text='ITS A PERFECT WORKOUT FOR YOU ',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen1 = Label(screen, text='1. Cardiovascular Exercise (3-5 times per week) - 30-60 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen2 = Label(screen, text='2. High-Intensity Interval Training (HIIT) or Circuit Training (1-2 times per week) - 20-30 minutes',bg='black',fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen3 = Label(screen, text='3. Yoga or Pilates (1-2 times per week) - 30-45 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen4 = Label(screen, text='4. Flexibility and Mobility Training (2-3 times per week) - 15-30 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen5 = Label(screen, text='5.Outdoor Activities or Sports (1-2 times per week)',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen_.place(x=300,y=50)
            screen1.place(x=250,y=100)
            screen2.place(x=250,y=150)
            screen3.place(x=250,y=200)
            screen4.place(x=250,y=250)
            screen5.place(x=250,y=300)   

    elif('50' <=weight<='90' and '40'<=age <='60'):
        response = messagebox.askquestion("Confirmation", "Are you sure?")
        if response == 'yes':
            screen = Toplevel(root)
            screen.title("Your guide")
            screen.geometry('925x500+300+200')
            screen.config(bg='black')
            screen_=Label(screen,text='ITS A PERFECT WORKOUT FOR YOU ',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen1 = Label(screen, text='1. Cardiovascular Exercise (3-5 times per week) - 30-60 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen2 = Label(screen, text='2. Low-Impact Aerobic Exercise (2-3 times per week) - 20-45 minutes',bg='black',fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen3 = Label(screen, text='3. Functional Training and Balance Exercises (2-3 times per week) - 30-45 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen4 = Label(screen, text='4. Mind-Body Exercises (e.g., Tai Chi, Yoga) (1-2 times per week) - 30-60 minutes',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen5 = Label(screen, text='5. Rest and Recovery - Varies (Ensure at least 1-2 rest days per week)',bg='black', fg='green', font=('microsoft YaHei UI Light', 0, 'bold'))
            screen_.place(x=300,y=50)
            screen1.place(x=250,y=100)
            screen2.place(x=250,y=150)
            screen3.place(x=250,y=200)
            screen4.place(x=250,y=250)
            screen5.place(x=250,y=300)   
    
    
    
    else:
        messagebox.showerror('invalid','check the weight and age')

#-------------------------------------#

#------------design------------------#
def clear_entry(event, entry):
    entry.delete(0, 'end')

def reset_entry(event, entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)

label=tk.Label(root,text='GYM GUIDE',fg='green',bg='black',font=('microsoft YaHei UI Light',18,'bold')).place(x=400,y=100)
entry=tk.Entry(root, width=30, fg="black", border=0, bg='white', font=('microsoft YaHei UI Light', 11))
entry.place(x=350,y=180)
entry.insert(0,'ENTER YOUR AGE')
entry.bind('<FocusIn>', lambda event: clear_entry(event, entry))
entry.bind('<FocusOut>', lambda event: reset_entry(event, entry, 'ENTER YOUR AGE'))

entry1=tk.Entry(root, width=30, fg="black", border=0,bg='white', font=('microsoft YaHei UI Light', 11))
entry1.place(x=350,y=250)
entry1.insert(0,'ENTER YOUR WEIGHT')
entry1.bind('<FocusIn>', lambda event: clear_entry(event, entry1))
entry1.bind('<FocusOut>', lambda event: reset_entry(event, entry1, 'ENTER YOUR WEIGHT'))

mybutton=tk.Button(root,text='submit',fg='white', border=0, bg='green', padx=100, pady=10,command=submit).place(x=350,y=320)
#------------------------------------#
root.mainloop()