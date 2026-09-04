import tkinter as tk
import events as event
root = tk.Tk()
root.title("Mi primera ventana")

label = tk.Label(root, text="Hola Mundo").grid(row=0, column=0)
#label.pack()

labelFirstName = tk.Label(root, text="First name").grid(row=1, column=0)
labelLastName = tk.Label(root, text="Last name").grid(row=2, column=0)

entryFirstName = tk.Entry(root).grid(row=1, column=1)
entryLastName = tk.Entry(root).grid(row=2, column=1)

varMaleRB = tk.IntVar()
varFemaleRB = tk.IntVar()

rbMale=tk.Radiobutton(root, text="Male", variable=varMaleRB, value="M").grid(row=3, sticky=tk.W)
rbFemale=tk.Radiobutton(root, text="Female", variable=varFemaleRB, value="F").grid(row=4, sticky=tk.W)

varHobby1 = tk.IntVar()
varHobby2 = tk.IntVar()

tk.Checkbutton(root, text="Running", variable=varHobby1).grid(row=5, sticky=tk.W)
tk.Checkbutton(root, text="Swimming", variable=varHobby2).grid(row=6, sticky=tk.W)

lb = tk.Listbox(root)
lb.insert(1, "Python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any other")

lb.grid(row=7, column=0, rowspan=1, sticky=tk.W)

button = tk.Button(root, text="Submit", width=25, command=event.on_click_event).grid(row=8, column=0)

button = tk.Button(root, text="Stop", width=25, command=root.destroy, bg="red", fg="white").grid(row=7, column=0)
#button.pack()

root.mainloop()