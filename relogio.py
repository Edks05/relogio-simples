###cores utilizadas
cor1 = "#454545"
cor2 = "#ffffff"


#importação dos sistema de janela###
from tkinter import *
janela = Tk()
janela.title("Relogio")
janela.geometry("440x210")
janela.configure(bg=cor1)
janela.iconbitmap("relogio.ico")
#cores utilizados###########

###############config
from datetime import datetime

def relogio():
    tempo=datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia = tempo.day
    ano = tempo.strftime("%Y")
    mes = tempo.strftime("%b")
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + str(dia) + " /" + str(mes) + "/" + str(ano))


l1=Label(janela, text="", font=("Ariel 80"), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2=Label(janela, text="", font=("Ariel 20"), bg=cor1, fg=cor2)
l2.grid(row=15, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()
