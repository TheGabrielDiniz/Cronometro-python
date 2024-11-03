from tkinter import *
from datetime import datetime


sec = 0
t = 1
janela_aberta = False


def tick(validador=False):
    global sec, hr, min, t, janela_aberta
    if validador == False:
        if radio_valor.get() == 1:
            hr = 00
            min = 00
            sec = int(inicio.get())
            btnComecar['state'] = DISABLED
        elif radio_valor.get() == 2:
            hr = 00
            min = int(inicio.get())-1
            sec = 60
            btnComecar['state'] = DISABLED
        elif radio_valor.get() == 3:
            hr = int(inicio.get())-1
            min = 59
            sec = 60
            btnComecar['state'] = DISABLED

    if hr == -1:
        timeText['text'] = 'TEMPO ESGOTADO'
        btnComecar['state'] = NORMAL

        if janela_aberta == False:
            segunda_janela()

    elif sec == -1:
        timeText['text'] = ''
        btnComecar['state'] = NORMAL
    else:
        # sec = sec - 1
        # time_str = f"{hr:02d}:{min:02d}:{sec:02d}"
        # timeText['text'] = time_str
        # timeText.after(1000, lambda: tick(True))
             #print(hr)
        if hr != -1:
            if t == 1:
                horaText['text'] = datetime.now().strftime("%H:%M:%S")
                t -= 1

            sec = sec - 1
            tempo = f"{hr:02d}:{min:02d}:{sec:02d}"
            timeText['text'] = tempo
            timeText.after(1000, lambda: tick(True))
            if tempo != "00:00:00":
                timeText['text'] = tempo
            else:
                timeText['text'] = tempo
                horaFinalText['text'] = datetime.now().strftime("%H:%M:%S")
                hr = -1
            if min == 0:
                if sec == 0:
                    if hr > 0:
                        min = 2
                        hr = hr - 1
            if sec == 0:
                if min > 0:
                    min = min - 1
                sec = 3


def teck():
    global sec, janela_aberta
    janela_aberta = False
    sec = -1
    inicio.delete(0, len(inicio.get()))
    timeText['text'] = ''
    horaText['text'] = ''
    btnComecar['state'] = NORMAL


def segunda_janela():
    global janela_aberta
    janela_aberta = True
    janela_secundaria = Toplevel()
    janela_secundaria.geometry("{0}x{1}+0+0".format(janela_secundaria.winfo_screenwidth(), janela_secundaria.winfo_screenheight()))

    janela_secundaria.title("Segunda Janela")

    mensagem = Label(janela_secundaria, fg='black', text='Acabou o Tempo!!!', font="Arial 100 bold")
    mensagem.pack(fill='both', expand=True)

    janela_secundaria.after(10000, janela_secundaria.destroy)
    janela_aberta = False


root = Tk()
root.attributes("-top", 1)

# Objeto IntVar dos botões
radio_valor = IntVar()
radio_valor.set(1)  # Para a primeira opção ficar marcada

# meus btns
btnSegundos = Radiobutton(root, text='Segundos', state=NORMAL, activeforeground="red", variable=radio_valor, value=1)
btnMinutos = Radiobutton(root, text='Minutos', state=NORMAL, activeforeground="red", variable=radio_valor, value=2)
btnHoras = Radiobutton(root, text='Horas', state=NORMAL, activeforeground="red", variable=radio_valor, value=3)
# posições
btnSegundos.grid(row=1, column=0, padx=10, pady=5)
btnMinutos.grid(row=1, column=1, padx=10, pady=5)
btnHoras.grid(row=1, column=2, padx=10, pady=5)

# ---------------------------------------------------------------------------------------

#label = Label(root, text="Quanto tempo você tem para realizar suas  tarefas?")
#label.grid(row=0, column=0)

inicio = Entry(root)
inicio.grid(row=2, column=0)

timeText = Label(root, fg='green')
timeText.grid(row=3, column=0)

horaTextIndicador = Label(root, fg='green')
horaTextIndicador.grid(row=2, column=1)
horaTextIndicador['text'] = "Começo:"

horaFinalTextIndicador = Label(root, fg='green')
horaFinalTextIndicador.grid(row=2, column=2)
horaFinalTextIndicador['text'] = "Fim:"

horaText = Label(root, fg='green')
horaText.grid(row=3, column=1)

horaFinalText = Label(root, fg='green')
horaFinalText.grid(row=3, column=2)


btnComecar = Button(root, fg='blue', text='Start', command=tick, state=NORMAL)
btnComecar.grid(row=4, column=0, padx=5, pady=2)

btnZerar = Button(root, fg='blue', text='Zerar', command=teck, state=NORMAL)
btnZerar.grid(row=4, column=1, padx=5, pady=2)

root.mainloop()