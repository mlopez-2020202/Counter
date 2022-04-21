import tkinter

index = tkinter.Tk()
index.title('Counter')
index.geometry('650x400')
#Funciones
lblNumero = tkinter.Label(index, text=0, font='Centurty 35', fg='black')
lblNumero.place(x=310, y=120)

def incrementar():
    valor = int(lblNumero['text'])
    lblNumero['text'] = f'{valor + 1}'
    valor = int(lblNumero['text'])
    color(valor)
def disminuir():
    valor = int(lblNumero['text'])
    lblNumero['text'] = f'{valor - 1}'
    valor = int(lblNumero['text'])
    color(valor) 
def reiniciar():
    valor = int(lblNumero['text'])
    lblNumero['text'] = f'{valor * 0}'
    valor = int(lblNumero['text']) 
    color(valor) 


def color(valor):  
    if(valor > 0):
        lblNumero['fg'] = fg='green'
    elif(valor< 0):
        lblNumero['fg'] = fg='red'
    elif(valor== 0):
        lblNumero['fg'] = fg='black'

#Interfaz
btnAumentar = tkinter.Button(index, text='Encrease', font='Arial 15', bg='green', width=15, height=3, command=incrementar)
btnAumentar.place(x=30, y=280)
btnDisminuir = tkinter.Button(index, text='Decrease',font='Arial 15', bg='Red', width=15, height=3, command=disminuir)
btnDisminuir.place(x=450, y=280)
btnReiniciar = tkinter.Button(index, text='Reset',font='Arial 15', bg='Gray', width=15, height=3, command=reiniciar)
btnReiniciar.place(x=240, y=280)
lblName = tkinter.Label(index, text='Counter',font='Century 35')
lblName.place(x=240,y=10)

index.mainloop()