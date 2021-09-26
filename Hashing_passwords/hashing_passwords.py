# import argparse
import hashlib
from tkinter import *
 
root = Tk()
root.title("HASHING PASSWORDS")
root.geometry('944x344')
root.configure(background="white")

# #textbox
# f2 = Frame(root, width=300, height=500, bd=8, bg="white")
# f2.pack(side=TOP)

Label(root, text=" Hashing Password", font="comicsansms 25 bold").grid(row=0, column=1)


passwor = Label(root, text="Enter the Name")
Option = Label(root, text="Enter Option 0-sha256 1-sha512 2-md5")

passwor.grid(row=3, column=1)
Option.grid(row=6, column=1)

#to store value
passwor= StringVar()
Option = StringVar()

#Entries 
nameentry = Entry(root, textvariable=passwor,font=('arial', 10, 'bold'), bd=5, width=22,justify='left')
optionentry = Entry(root, textvariable=Option,font=('arial', 10, 'bold'),bd=5, width=22,justify='left')

#packing the entries
nameentry.grid(row=3, column=2)
optionentry.grid(row=6, column=2)


# parsing
# parser = argparse.ArgumentParser(description='hashing given password')
# parser.add_argument('password', help='input password you want to hash')
# parser.add_argument('-t', '--type', default='sha256',choices=['sha256', 'sha512', 'md5'] )
# args = parser.parse_args() 

# hashing given password
# password = args.password
# hashtype = args.type
def Password():
    #password = input("Enter Hashing Given Password\n")
    list = ['sha256','sha512','md5']
    # print("Options are",list)
    # type = int(input("Enter your option"))
    password=passwor.get()
    hashtype=list[int(Option.get())]
    
    m = getattr(hashlib,hashtype)()
    m.update(password.encode())

    # output
    #print("< hash-type : " + hashtype + " >")
    #print(m.hexdigest())
    txt.insert(END,"HASH PASSWORD\n" + m.hexdigest())

def Reset():
    passwor.set("")
    Option.set("")
    txt.delete('1.0',END)

#Buttons
Button(text="Generate Hash", command=Password).grid(row=15, column=2)
Button(text="Reset", command=Reset).grid(row=17, column=2)

txt = Text(root, height=5, width=35, bd=16, font=('arial', 13, 'bold'), fg="black", bg="white")
txt.grid(row=25, column=1)



root.mainloop()
