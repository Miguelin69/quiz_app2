from tkinter import *
from tkinter import messagebox , ttk


def terminar():
    messagebox.showinfo("   " , "Deseas terminar ?")
    

ventana_principal = Tk()


ventana_principal.title("INFORME")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0, 0)

ventana_principal.config(bg="white")

kf = ["Hombre", "Mujer"]
kf_selected = StringVar()


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white" , width=480 , height=180)
frame_entrada.place(x=10 , y=10)

cmb_kf = ttk.Combobox(frame_entrada, textvariable=kf_selected, values=kf, font=("Helvetica", 12))
cmb_kf.place(x=80, y=125 , width=80 , height=20)


lb_titulo = Label(frame_entrada, text="REGISTROS MEDICO Y ACADEMICO")
lb_titulo.config(bg="white" , fg="red" , font=("Helvetica", 10))
lb_titulo.place(x=150 , y=10)

lb_subtitulo = Label(frame_entrada, text="DATOS MEDICOS")
lb_subtitulo.config(bg="white" , fg="red" , font=("Helvetica", 10))
lb_subtitulo.place(x=50 , y=35)


lb_subtitulo = Label(frame_entrada, text="DATOS ACADEMICOS")
lb_subtitulo.config(bg="white" , fg="red" , font=("Helvetica", 10))
lb_subtitulo.place(x=290 , y=35)


lb_peso  = Label(frame_entrada , text="Peso: ")
lb_peso.config(bg="white" , fg="black" , font=("arial", 14))
lb_peso.place(x=20 , y=60)

entry_peso = Entry(frame_entrada, textvariable=lb_peso)
entry_peso.config(bg="white" , fg="green" , font=("Courier", 12))
entry_peso.focus_set()
entry_peso.place(x=80 , y=65 , width=50 , height=20)

lb_altura  = Label(frame_entrada , text="Altura: ")
lb_altura.config(bg="white" , fg="black" , font=("arial", 14))
lb_altura.place(x=18 , y=90)

entry_altura = Entry(frame_entrada, textvariable=lb_altura)
entry_altura.config(bg="white" , fg="green" , font=("Courier", 12))
entry_altura.focus_set()
entry_altura.place(x=80 , y=95 , width=50 , height=20)


lb_sexo  = Label(frame_entrada , text="Sexo: ")
lb_sexo.config(bg="white" , fg="black" , font=("arial", 14))
lb_sexo.place(x=20 , y=120)


lb_altura  = Label(frame_entrada , text="Edad: ")
lb_altura.config(bg="white" , fg="black" , font=("arial", 14))
lb_altura.place(x=18 , y=150)

entry_edad = Entry(frame_entrada, textvariable=lb_altura)
entry_edad.config(bg="white" , fg="green" , font=("Courier", 12))
entry_edad.focus_set()
entry_edad.place(x=80 , y=155 , width=50 , height=20)


bt_terminar= Button(ventana_principal , text="terminar" , command=terminar)
bt_terminar.place(x=200 , y=450 , width=100 , height=30)


ventana_principal.mainloop()