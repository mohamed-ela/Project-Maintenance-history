# update the appointments
from tkinter import *
import tkinter.messagebox
import datetime as dt
import time as tm
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

#LIST OF ALL SEARCHED RESULTS
result_list=[]

class Application:
    def __init__(self, master):
        self.master = master
        self.natureMachine1 = ""
        self.numMachine  = ""
        self.dateEntree  = ""
        self.dateSortie  = ""
        self.permanencier   = ""
        self.libelleDefaut  = ""
        # heading label
        self.heading = Label(master, text="ARRETS ENREGISTRES ",  fg='grey', font=('arial 40 bold'))
        self.heading.place(x=150, y=20)

        # search criteria -->name 
        self.numMachine = Label(master, text="ENTREZ NUMERO MACHINE", font=('arial 15 bold'))
        self.numMachine.place(x=0, y=100)

        # entry for  the name
        self.numMachine_ent = Entry(master, width=30)
        self.numMachine_ent.place(x=299, y=105)
        self.numMachine_ent.focus()

        # search button
        self.search = Button(master, text="CHERCHEZ", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=132)

    # function to search
    def search_db(self):
        self.input = self.numMachine_ent.get()
        # execute sql 
        if self.input == '':
            tkinter.messagebox.showinfo("Warning", "REMPLISSEZ TOUT LES CHAMPS SVP")

        sql = "SELECT * FROM ARRETS WHERE NUMMACHINE LIKE ?"
        self.res = c.execute(sql, (self.input))

        for self.row in self.res:
            self.natureMachine1 = self.row[1]
            self.numMachine = self.row[2]
            self.dateEntree = self.row[3]
            self.dateSortie = self.row[4]
            self.permanencier = self.row[6]
            self.libelleDefaut = self.row[5]



        #SHOWING ALL QUERIED RESULTS IN LOG


        # creating the update form
        self.unatureMachine = Label(self.master, text="Nature Machine/Système", font=('arial 18 bold'))
        self.unatureMachine.place(x=0, y=160)

        self.unumMachine = Label(self.master, text="N*Machine", font=('arial 18 bold'))
        self.unumMachine.place(x=0, y=200)

        self.udateEntree = Label(self.master, text="DATE-ENTREE", font=('arial 18 bold'))
        self.udateEntree.place(x=0, y=240)

        self.ulocation = Label(self.master, text="DATE-SORTIE", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=280)

        self.udateSortie = Label(self.master, text="Permanencier", font=('arial 18 bold'))
        self.udateSortie.place(x=0, y=320)

        self.ulibelleDefaut = Label(self.master, text="Libelle Defaut", font=('arial 18 bold'))
        self.ulibelleDefaut.place(x=0, y=360)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=170)
        self.ent1.insert(END, str(self.natureMachine1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=210)
        self.ent2.insert(END, str(self.numMachine))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=250)
        self.ent3.insert(END, str(self.dateEntree))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=290)
        self.ent4.insert(END, str(self.dateSortie))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=330)
        self.ent5.insert(END, str(self.permanencier))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=370)
        self.ent6.insert(END, str(self.libelleDefaut))

        # button to execute update
        self.update = Button(self.master, text="MODIFIER", width=20, height=2,fg='white', bg='green', command=self.update_db)
        self.update.place(x=400, y=410)

        # button to delete
        self.delete = Button(self.master, text="SUPPRIMER", width=20, height=2,fg='white', bg='red', command=self.delete_db)
        self.delete.place(x=150, y=410)




    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated dateEntree
        self.var4 = self.ent4.get() #updated dateSortie
        self.var5 = self.ent5.get() #updated libelleDefaut
        self.var6 = self.ent6.get() #updated permanencier

        query = "UPDATE ARRETS SET NATUREMACHINE=?, NUMMACHINE=?, DATEENTREE=?, DATESORTIE=?, PERMANENCIER=?, LIBELLEDEFAUT=? WHERE NUMMACHINE LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.numMachine_ent.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM ARRETS WHERE NUMMACHINE LIKE ?"
        c.execute(sql2, (self.numMachine_ent.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
# creating the object
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()