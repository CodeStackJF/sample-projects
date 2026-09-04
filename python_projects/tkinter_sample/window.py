import tkinter as tk
from tkinter import DISABLED, ttk
from tkinter import messagebox
from user_database_commands import UserDatabase
from entities.user import User

class App(tk.Tk):
    def __init__(self):
        super().__init__() #llamado de constructor
        self.title("Sample App")
        self.geometry("650x480")
        self.createVariables()
        self.createGui()
        self.userDatabase = UserDatabase()
        self.loadUsers()
        
    def createVariables(self):
        self.id = tk.IntVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.email = tk.StringVar()

    def createGui(self):
        self.labelFirstName = tk.Label(self, text="Id")
        self.labelFirstName.grid(row=0, column=0)  
        self.entryFirstName = tk.Entry(self, textvariable=self.id, state="disabled")
        self.entryFirstName.grid(row=0, column=1, pady=10)
        
        self.labelFirstName = tk.Label(self, text="First Name")
        self.labelFirstName.grid(row=1, column=0)  
        self.entryFirstName = tk.Entry(self, textvariable=self.first_name)
        self.entryFirstName.grid(row=1, column=1, pady=10)
        
        self.labelLastName = tk.Label(self, text="Last Name")
        self.labelLastName.grid(row=2, column=0)       
        self.entryLastName = tk.Entry(self, textvariable=self.last_name)
        self.entryLastName.grid(row=2, column=1, pady=10)
        
        self.labelEmail = tk.Label(self, text="Email")
        self.labelEmail.grid(row=3, column=0)       
        self.entryEmail = tk.Entry(self, textvariable=self.email)
        self.entryEmail.grid(row=3, column=1, pady=10)
        
        self.buttonSave = tk.Button(self, text="Save", command=self.saveData)
        self.buttonSave.grid(row=4, column=0, columnspan=1)
        
        columns = ("id", "first_name", "last_name", "email")
        self.tableUsers = ttk.Treeview(self, columns = columns, show="headings", selectmode='browse')
        
        self.tableUsers.heading("id", text="ID")
        self.tableUsers.heading("first_name", text="First name")
        self.tableUsers.heading("last_name", text="Last name")
        self.tableUsers.heading("email", text="email")
        
        self.tableUsers.column("id", width=50, anchor="center")
        self.tableUsers.column("first_name", width=150, anchor="w")
        self.tableUsers.column("last_name", width=150, anchor="w")
        self.tableUsers.column("email", width=150, anchor="w")
        self.tableUsers.bind("<Double-1>", self.getUser)
        self.tableUsers.grid(row=5, column=1)
        
        self.buttonClearData = tk.Button(self, text="Clear Data", command=self.clearFields)
        self.buttonClearData.grid(row=6, column=1, columnspan=1)
        
        
    def clearFields(self):
        self.id.set(0)
        self.first_name.set("")
        self.last_name.set("")
        self.email.set("")
        self.buttonSave.config(text="Save")
    
    def saveData(self):
        # Here you would typically save the data to a database or file
        
        id = self.id.get()
        first_name = self.first_name.get().strip()
        last_name = self.last_name.get().strip()
        email = self.email.get().strip()
        
        if(self.userDatabase.emailExists(id, email)):
            messagebox.showwarning("Email exists", "This email is registered by another user.")
            return
        
        user = User(
            first_name,
            last_name,
            email
        )
        if id == 0:
            self.userDatabase.save(user)
        else:
            self.userDatabase.update(id, user)
            
        self.buttonSave.config(text="Save")
        self.loadUsers()
        self.clearFields()

    def loadUsers(self):
        users = self.userDatabase.getAll()
        for item in self.tableUsers.get_children():
            self.tableUsers.delete(item)
            
        for row in users:
            self.tableUsers.insert("", tk.END, values=row)
    
    def getUser(self, event):
        selected = self.tableUsers.focus()
        rowData = self.tableUsers.item(selected)
        values = rowData.get("values")
        userId = values[0]
        usuario = self.userDatabase.get(userId)    
        self.id.set(usuario[0]);
        self.first_name.set(usuario[1]);
        self.last_name.set(usuario[2]);
        self.email.set(usuario[3]);
        self.buttonSave.config(text="Update")
        
    #def displayData(self):
    #    messagebox.showinfo("Information", f"First Name: {self.first_name.get().strip()}\nLast Name: {self.last_name.get().strip()}\nEmail: {self.email.get().strip()}")