from tkinter import *

window = Tk()

window.geometry("600x300")
window.configure(bg="#fff")
window.title("Mi primera ventana")

lblNombre = Label(window, text="Nombre", font=("Arial", 14), bg="#111", fg="#fff")
#lblMensaje.place(x=100, y=40)
lblNombre.grid(row=0, column=0)

txtNombre = Entry(window, text = "Escriba su nombre")
txtNombre.grid(row=0, column=1)

btnAceptar = Button(window, text="Aceptar")
btnAceptar.grid(row=1, column=0, columnspan=2)

window.mainloop()