import tkinter as tk
from time import gmtime, strftime
from tkinter import messagebox


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0


def check_acc_nmb(num):
    try:
        fpin = open(num + ".txt", 'r')
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Credentials!\nTry Again!")
        return 0
    fpin.close()
    return


def home_return(master):
    master.destroy()
    Main_Menu()


def write(master, name, oc, pin):
    if ((is_number(name)) or (is_number(oc) == 0) or (is_number(pin) == 0) or name == ""):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1 = open("Accnt_Record.txt", 'r')
    accnt_no = int(f1.readline())
    accnt_no += 1
    f1.close()

    f1 = open("Accnt_Record.txt", 'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet = open(str(accnt_no) + ".txt", "w")
    fdet.write(pin + "\n")
    fdet.write(oc + "\n")
    fdet.write(str(accnt_no) + "\n")
    fdet.write(name + "\n")
    fdet.close()

    frec = open(str(accnt_no) + "-rec.txt", 'w')
    frec.write("Date                                            Credit             Debit            Balance\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + oc + "              " + oc + "\n")
    frec.close()

    messagebox.showinfo("Details", "Your Account Number is:" + str(accnt_no))
    master.destroy()
    return


def crdt_write(master, amt, accnt, name):
    if (is_number(amt) == 0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    fdet = open(accnt + ".txt", 'r')
    pin = fdet.readline()
    camt = int(fdet.readline())
    fdet.close()
    amti = int(amt)
    cb = amti + camt
    fdet = open(accnt + ".txt", 'w')
    fdet.write(pin)
    fdet.write(str(cb) + "\n")
    fdet.write(accnt + "\n")
    fdet.write(name + "\n")
    fdet.close()
    frec = open(str(accnt) + "-rec.txt", 'a+')
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + str(amti) + "              " + str(cb) + "\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!", "Amount Credited Successfully!!")
    master.destroy()
    return


def debit_write(master, amt, accnt, name):
    if (is_number(amt) == 0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    fdet = open(accnt + ".txt", 'r')
    pin = fdet.readline()
    camt = int(fdet.readline())
    fdet.close()
    if (int(amt) > camt):
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        amti = int(amt)
        cb = camt - amti
        fdet = open(accnt + ".txt", 'w')
        fdet.write(pin)
        fdet.write(str(cb) + "\n")
        fdet.write(accnt + "\n")
        fdet.write(name + "\n")
        fdet.close()
        frec = open(str(accnt) + "-rec.txt", 'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + "              " + str(amti) + "              " + str(cb) + "\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
        master.destroy()
        return


def Cr_Amt(accnt, name):
    creditwn = tk.Tk()
    creditwn.geometry("1600x1000")
    creditwn.title("Credit Amount")
    creditwn.configure(bg="light coral")
    fr1 = tk.Frame(creditwn, bg="blue")
    l_title = tk.Message(creditwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,fg="pink", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Sitka text", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(creditwn, relief="raised", font=("Times", 26), text="Enter Amount to be credited: ",bd="3")
    e1 = tk.Entry(creditwn, relief="raised",font=("Times", 16),bg="green yellow",bd="5")
    l1.pack(side="top")
    l1.place(x=700, y=200)
    e1.pack(side="top")
    e1.place(x=700, y=250)
    b = tk.Button(creditwn, text="Credit", font=("Sitka text", 16), relief="raised",command=lambda: crdt_write(creditwn, e1.get(), accnt, name))
    b.pack(side="top")
    b.place(x=700, y=300)
    #creditwn.bind("<Return>", lambda x: crdt_write(creditwn, e1.get(), accnt, name))
    #imgw = tk.PhotoImage(file="crediticon.png")
    #labelw = tk.Label(creditwn,image=imgw)
    #labelw.pack()
    #labelw.place(x=340, y=240)
    creditwn.mainloop()
    creditwn.bind("<Return>", lambda x: crdt_write(creditwn, e1.get(), accnt, name))

def De_Amt(accnt, name):
    debitwn = tk.Tk()
    debitwn.geometry("1600x1000")
    debitwn.title("Debit Amount")
    debitwn.configure(bg="light coral")
    fr1 = tk.Frame(debitwn, bg="blue")
    l_title = tk.Message(debitwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,fg="pink", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Sitka text", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(debitwn, relief="raised", font=("Times", 26), text="Enter Amount to be debited: ",bd="3")
    e1 = tk.Entry(debitwn, relief="raised",font=("Times", 16),bg="green yellow",bd="5")
    l1.pack(side="top")
    e1.pack(side="top")
    l1.place(x=700, y=200)
    e1.place(x=700, y=250)
    b = tk.Button(debitwn, text="Debit", font=("Sitka text", 16), relief="raised",command=lambda: debit_write(debitwn, e1.get(), accnt, name))
    b.pack(side="top")
    b.place(x=700,y=300)
    debitwn.bind("<Return>", lambda x: debit_write(debitwn, e1.get(), accnt, name))


def disp_bal(accnt):
    fdet = open(accnt + ".txt", 'r')
    fdet.readline()
    bal = fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance", bal)


def disp_tr_hist(accnt):
    disp_wn = tk.Tk()
    disp_wn.geometry("1600x1000")
    disp_wn.title("Transaction History")
    disp_wn.configure(bg="light coral")
    fr1 = tk.Frame(disp_wn, bg="blue")
    l_title = tk.Message(disp_wn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,fg="pink", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Sitka text", "50", "bold"))
    l_title.pack(side="top")
    fr1 = tk.Frame(disp_wn)
    fr1.pack(side="top")
    l1 = tk.Message(disp_wn, text="Your Transaction History:", font=("Sitka text", 16), padx=100, pady=20, width=1000,bg="blue4", fg="pink", relief="raised")
    l1.pack(side="top")
    fr2 = tk.Frame(disp_wn)
    fr2.pack(side="top")
    frec = open(accnt + "-rec.txt", 'r')
    for line in frec:
        l = tk.Message(disp_wn, anchor="w", text=line, relief="raised", width=2000,padx="70",bg='yellow')
        l.pack(side="top")
    b = tk.Button(disp_wn, text="QUIT",anchor="center", font=("Sitka text",16,"bold"),  bg="purple", fg="pink",relief="raised", command=disp_wn.destroy)
    b.pack(side="top")
    b.place(x=600,y=400)
    frec.close()


def logged_in_menu(accnt, name):
    rootwn = tk.Tk()
    rootwn.geometry("1600x1000")
    rootwn.title("Bank Management System | Welcome - " + name)
    rootwn.configure(background='light coral')
    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")
    l_title = tk.Message(rootwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,fg="pink", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Sitka text", "50", "bold"))
    l_title.pack(side="top")
    label = tk.Label(text="Logged in as: " + name, relief="raised", font=("Sitka text", 16), fg="blue4",anchor="center", justify="center")
    label.pack(side="top")
    label.place(x=550,y=100)
    img2 = tk.PhotoImage(file="credit.gif")
    myimg2 = img2.subsample(2, 2)
    img3 = tk.PhotoImage(file="debit.gif")
    myimg3 = img3.subsample(2, 2)
    img4 = tk.PhotoImage(file="balance1.gif")
    myimg4 = img4.subsample(2, 2)
    img5 = tk.PhotoImage(file="transaction-1.gif")
    myimg5 = img5.subsample(2, 2)
    b2 = tk.Button(image=myimg2, command=lambda: Cr_Amt(accnt, name))
    b2.image = myimg2
    b3 = tk.Button(image=myimg3, command=lambda: De_Amt(accnt, name))
    b3.image = myimg3
    b4 = tk.Button(image=myimg4, command=lambda: disp_bal(accnt))
    b4.image = myimg4
    b5 = tk.Button(image=myimg5, command=lambda: disp_tr_hist(accnt))
    b5.image = myimg5
    imga = tk.PhotoImage(file="adminLogin1.png")
    label = tk.Label(image=imga)
    label.pack( side="left", anchor="center")
    label.place(x=550,y=230)
    img6 = tk.PhotoImage(file="271-2715210_logout-button-icon-png.png")
    myimg6 = img6.subsample(4, 4)
    b6 = tk.Button(image=myimg6, relief="raised", command=lambda: logout(rootwn))
    b6.image = myimg6

    b2.place(x=100, y=230)
    b3.place(x=100, y=330)
    b4.place(x=900, y=230)
    b5.place(x=900, y=330)
    b6.place(x=570, y=430)
    rootwn.mainloop()

def logout(master):
    messagebox.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()


def check_log_in(master, name, acc_num, pin):
    f = open(acc_num + '.txt', 'r')
    l = []
    for i in f:
        l.append(i)
    if l[0][:-1] == pin:
        if l[2][:-1] == acc_num:
            if l[3][:-1] == name:
                master.destroy()
                logged_in_menu(acc_num, name)
                return
            else:
                messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
                master.destroy()
                Main_Menu()
        else:
            messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
            master.destroy()
            Main_Menu()
    else:
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()


def log_in(master):
    master.destroy()
    loginwn = tk.Tk()
    loginwn.geometry("1600x1000")
    loginwn.title("Log in")
    loginwn.configure(bg="light coral")
    fr1 = tk.Frame(loginwn, bg="yellow")
    l_title = tk.Message(loginwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                         fg="pink", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Sitka text", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(loginwn, text="Enter your Name", font=("Times", 19), relief="raised",bd="3")
    l1.pack(side="top")
    l1.place(x=700,y=200)
    e1 = tk.Entry(loginwn,font=('calibre',16,'normal'),bg="green yellow",bd="5")
    e1.pack(side="top")
    e1.place(x=700, y=240)
    l2 = tk.Label(loginwn, text="Enter account number", font=("Times", 19), relief="raised",bd="3")
    l2.pack(side="top")
    l2.place(x=700, y=300)
    e2 = tk.Entry(loginwn,font=('calibre',16,'normal'),bg="green yellow",bd="5")
    e2.pack(side="top")
    e2.place(x=700, y=340)
    l3 = tk.Label(loginwn, text="Enter your PIN", font=("Times", 19), relief="raised",bd="3")
    l3.pack(side="top")
    l3.place(x=700, y=400)
    e3 = tk.Entry(loginwn, show="*",font=("Times", 16),bg="green yellow",bd="5")
    e3.pack(side="top")
    e3.place(x=700, y=440)
    b = tk.Button(loginwn, text="Submit",font=("Sitka text",15,"bold"),fg='green', bg='AntiqueWhite2',command=lambda: check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    b.pack(side="top")
    b.place(x=700, y=490)
    b1 = tk.Button(text="HOME", font=("Sitka text", 20,"bold"), relief="raised", bg="purple", fg="pink",command=lambda: home_return(loginwn))
    b1.pack(side="top")
    b1.place(x=750, y=560)
    loginwn.bind("<Return>", lambda x: check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    imgu = tk.PhotoImage(file="userlogin.png")
    labelu = tk.Label(image=imgu)
    labelu.pack()
    labelu.place(x=340,y=240)
    loginwn.mainloop()

def Create():
    crwn = tk.Tk()
    crwn.geometry("1600x1000")
    crwn.title("Create Account")
    crwn.configure(bg="light coral")
    fr1 = tk.Frame(crwn, bg="blue")
    l_title = tk.Message(crwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0, fg="pink",bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Sitka text", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(crwn, text="Enter your Name", font=("Times", 19), relief="raised",bd="3")
    l1.pack(side="top")
    l1.place(x=550, y=200)
    e1 = tk.Entry(crwn,font=('calibre',16,'normal'),bg="green yellow",bd="5")
    e1.pack(side="top")
    e1.place(x=550, y=240)
    l2 = tk.Label(crwn, text="Enter Opening Credit", font=("Times", 19), relief="raised",bd="3")
    l2.pack(side="top")
    l2.place(x=550, y=300)
    e2 = tk.Entry(crwn,font=('calibre',16,'normal'),bg="green yellow",bd="5")
    e2.pack(side="top")
    e2.place(x=550, y=340)
    l3 = tk.Label(crwn, text="Enter Desired PIN", font=("Times", 19), relief="raised",bd="3")
    l3.pack(side="top")
    l3.place(x=550, y=400)
    e3 = tk.Entry(crwn, show="*",font=('calibre',16,'normal'),bg="green yellow",bd="5")
    e3.pack(side="top")
    e3.place(x=550, y=440)
    b = tk.Button(crwn, text="Submit", font=("Sitka text", 16,"bold"),fg="green",bg="AntiqueWhite2",command=lambda: write(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    b.pack(side="top")
    b.place(x=550, y=500)
    b6 = tk.Button(crwn,text="HOME",font=("Sitka text", 16,"bold"),fg="pink",bg="purple", command=crwn.destroy)
    b6.place(x=640, y=570)
    crwn.bind("<Return>", lambda x: write(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    crwn.mainloop()
    #log_in()
    #b1 = tk.Button(crwn,text="HOME", font=("Sitka text", 20, "bold"), relief="raised", bg="purple", fg="pink",
     #              command=lambda: log_in())
    #b1.pack(side="top")
    #b1.place(x=750, y=560)
    #crwn.bind("<Return>",b1,lambda : home_return(crwn))
    #return
    """imgc = tk.PhotoImage(file="images.png")
    labelc = tk.Label(crwn,image=imgc)
    labelc.pack()
    labelc.place(x=340, y=240)
    crwn.mainloop()"""
    #crwn.bind("<Return>", font=("Times", 16), command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))



def Main_Menu():
    rootwn = tk.Tk()
    rootwn.geometry("1600x1000")
    rootwn.title("Bank Management System")
    rootwn.configure(background='light coral')
    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")
    l_title = tk.Message(text="BANK MANAGEMENT SYSTEM ", relief="raised", width=2000, padx=600, pady=0, fg="blue3",bg="lightblue", justify="center", anchor="center")
    l_title.config(font=("Verdana", "40", "bold"))
    l_title.pack(side="top")
    imgc1 = tk.PhotoImage(file="createaccount-button-png-hi.png")
    imglo = tk.PhotoImage(file="login-Button-PNG-Picture.png")
    imgb=tk.PhotoImage(file="banktrans.png")
    label=tk.Label(image=imgb)
    label.pack(ipadx="60",ipady="80",side="left", anchor="center")
    #label.pack(anchor="")
    imgc = imgc1.subsample(3, 3)
    imglog = imglo.subsample(3, 3)
    #background=tk.PhotoImage(file="My project.png")
    b1 = tk.Button(image=imgc,relief="raised" ,command=Create)
    b1.image = imgc
    b2 = tk.Button(image=imglog,relief="raised" ,command=lambda: log_in(rootwn))
    b2.image = imglog
    img6 = tk.PhotoImage(file="quit-1.gif")
    myimg6 = img6.subsample(2, 2)
    """bg=tk.PhotoImage(file="My project.png")
    canvas = tk.Canvas(rootwn, width=1000, height=1600)
    canvas.create_image(0,0,image=bg,anchor="nw")"""
    b6 = tk.Button(image=myimg6,relief="raised", command=rootwn.destroy)
    b6.image = myimg6
    b1.place(x=500, y=335)
    b2.place(x=500, y=250)
    b6.place(x=540, y=480)
    labelw1=tk.Label(text="MISSION",font=("Times",16,"bold"),fg="pink",bg="cornsilk4",relief="groove",bd="3")
    labelw1.place(x=810,y=200)
    labelw2=tk.Label(text="Promote the financial integrity and operational efficiency\n"
                          "through exceptional accounting, financing, collections,\n"
                          "payments and the shared services.",font=("Times",15,"bold"),fg="black",relief="flat",bg="light coral",bd="3")
    labelw2.place(x=800,y=230)
    labelw3 = tk.Label(text="VISION", font=("Times", 16, "bold"), fg="pink", bg="cornsilk4", relief="groove", bd="3")
    labelw3.place(x=810, y=320)
    labelw4 = tk.Label(text="We will create products and services that help our customers\n"
                            "achieve their goals.We will go beyond the call of duty to make\n"
                            "our customers feel valued. We will be of service even in the \n"
                            "remotest part of our country. We will offer excellence in services\n"
                            "to those abroad as much as we do to those in India."
                            , font=("Times", 15, "bold"), fg="black", relief="flat", bg="light coral",
                       bd="3")
    labelw4.place(x=800, y=350)
    labelw5 = tk.Label(text="VALUES", font=("Times", 16, "bold"), fg="pink", bg="cornsilk4", relief="groove", bd="3")
    labelw5.place(x=810, y=490)
    labelw6 = tk.Label(text="We are guided by our commitment to integrity, collabration,\n"
                            "accountability, learning and excellence in our dealings with\n"
                            "each other and with those we support and serve.\n"
                       , font=("Times", 15, "bold"), fg="black", relief="flat", bg="light coral",
                       bd="3")
    labelw6.place(x=800, y=520)

    rootwn.mainloop()


Main_Menu()