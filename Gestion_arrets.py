# import modules
from tkinter import *
from datetime import date
import datetime as dt
import time as tm
import sqlite3
import tkinter.messagebox
# DB connection
conn = sqlite3.connect('database.db')

# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []



class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='grey')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=600, height=720, bg='grey')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="BASE DONNEES DES ARRETS-SERVICE ELECTRIQUE", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.heading.place(x=0, y=0)
        # NATURE MACHINE
        self.natureMachine = Label(self.left, text="Nature Machine/Système", font=(
            'georgia 13 bold'), fg='black', bg='grey')
        self.natureMachine.place(x=0, y=100)

        # NUMERO MACHINE
        self.numMachine = Label(self.left, text="N*Machine", font=(
            'georgia 13 bold'), fg='black', bg='grey')
        self.numMachine.place(x=0, y=140)

        # DATE ENTREE
        self.dateEntree = Label(self.left, text="DATE-ENTREE", font=(
            'georgia 13 bold'), fg='black', bg='grey')
        self.dateEntree.place(x=0, y=180)


        # DATE SORTIE
        self.dateSortie = Label(self.left, text="DATE-SORTIE", font=(
            'georgia 13 bold'), fg='black', bg='grey')
        self.dateSortie.place(x=0, y=220)

        # PERMANENCIER
        self.permanencier = Label(self.left, text="Permanencier", font=(
            'georgia 13 bold'), fg='black', bg='grey')
        self.permanencier.place(x=0, y=260)

        # LIBELLE DEFAUT
        self.libelleDefaut = Label(self.left, text="Libelle Defaut", font=(
            'georgia 13 bold'), fg='black', bg='grey')
        self.libelleDefaut.place(x=0, y=300)

        # Entries for all labels============================================================
        self.natureMachine_ent = Entry(self.left, width=30)
        self.natureMachine_ent.place(x=250, y=100)
        self.natureMachine_ent.focus()

        self.numMachine_ent = Entry(self.left, width=30)
        self.numMachine_ent.place(x=250, y=140)

        self.dateEntree_ent = Entry(self.left, width=30)
        self.dateEntree_ent.place(x=250, y=180)
        self.dateEntree_ent.insert(END, str(f"{dt.datetime.now():%d/%m/%Y}" + f"{tm.strftime('--%H:%M:%S')}"))

        self.dateSortie_ent = Entry(self.left, width=30)
        self.dateSortie_ent.place(x=250, y=220)
        self.dateSortie_ent.insert(END, str(f"{dt.datetime.now():%d/%m/%Y}" + f"{tm.strftime('--%H:%M:%S')}"))

        self.permanencier_ent = Entry(self.left, width=30)
        self.permanencier_ent.place(x=250, y=260)

        self.libelleDefaut_ent = Entry(self.left, width=30)
        self.libelleDefaut_ent.place(x=250, y=300)

        # button to perform a command
        self.submit = Button(self.left, text="AJOUTER", width=20,
                             height=2, bg='white', command=self.add_accident)
        self.submit.place(x=300, y=340)

        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM ARRETS "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="HISTORIQUE", font=(
            'georgia 28 bold'), fg='black', bg='grey')
        self.logs.place(x=70, y=10)

        self.box = Text(self.right, width=150, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "TOTAL DES ARRETS JUSQU'A " +str(f"{dt.datetime.now():%d/%m/%Y}"
               +f"{tm.strftime('--%H:%M:%S')}") +"-- SONT:"+
                        str(self.final_id) + " \n")
    # funtion to call when the submit button is clicked

    def add_accident(self):
        # getting the user inputs
        self.val1 = self.natureMachine_ent.get()
        self.val2 = self.numMachine_ent.get()
        self.val3 = self.dateEntree_ent.get()
        self.val4 = self.dateSortie_ent.get()
        self.val5 = self.permanencier_ent.get()
        self.val6 = self.libelleDefaut_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "REMPLISSEZ TOUT LES CHAMPS SVP")
        else:
            # now we add to the database
            sql = "INSERT INTO 'ARRETS' (NATUREMACHINE, NUMMACHINE, DATEENTREE, DATESORTIE, PERMANENCIER, LIBELLEDEFAUT) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3,
                            self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo(
                "Success", "ARRET ==> " + str(self.val1) + " ENREGISTRE")
            self.box.insert(END, 'ARRET DOCUMENTE : ' +
                            str(self.val6) + ' A ' + str(self.val3))



# creating the object
root = Tk()
root.title("OCP Group - Mine Beni Amir - GESTION DES ARRETS - SERVICE ELECTRIQUE")
b = Application(root)

# resolution of the window
root.geometry("1366x768")

# preventing the resize feature
root.resizable(False, False)

lbl = Label(root, text="GESTION DES ARRETS - SERVICE ELECTRIQUE OIK/MB/ME/855",fg="green", bg="white", font=("helvetica",25))
lbl.place(height=25,width=1050,anchor=N,x=550)

imgLogo = PhotoImage(file="OcpLogo.png")
imgLogolabel = Label(root, image=imgLogo, width=100, height=100).place(height=125,width=110,anchor=N,x=100,y=620)

root.iconbitmap("D:\Downloads\OcpLogo1.bmp")
z = Label(root, text=f"{tm.strftime('%H:%M:%S')}", fg="white", bg="black", font=("helvetica", 25))
z.place(height=35,width=200,anchor=N,x=550,y=580)
w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 20))
w.place(height=40,width=500,anchor=N,x=550,y=620)


# end the loop
root.mainloop()
