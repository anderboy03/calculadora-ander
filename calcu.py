from tkinter import *
from tkinter import ttk

# Cores
co1 = "#feffff"  # white/branca
co2 = "#38576b"
co3 = "#ECEFF1"
co4 = "#FFAB40"  # Orange/laranja
fundo = "#3b3b3b"  # black/preta

# Função para adicionar texto à tela
def entrar_valor(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

# Função para calcular expressões
def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""

# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Configuração da janela principal
janela = Tk()
janela.title("")
janela.geometry("235x318")
janela.configure(bg=co1)

# Separador horizontal
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

# Frames
frame_tela = Frame(janela, width=300, height=56, bg=co2, pady=0, padx=0, relief="flat")
frame_tela.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340, bg=fundo, pady=0, padx=0, relief="flat")
frame_quadros.grid(row=2, column=0, sticky=NW)

# Label para exibir o texto
valor_texto = StringVar()
app_tela = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor="e",
                 bd=0, justify=RIGHT, font=("Ivy 18 "), bg="#37474F", fg=co1)
app_tela.place(x=0, y=0)

# Botões da calculadora
botoes = [
    ("C", limpar_tela, 0, 0), ("%", lambda: entrar_valor("%"), 0, 118), ("/", lambda: entrar_valor("/"), 0, 177),
    ("7", lambda: entrar_valor("7"), 52, 0), ("8", lambda: entrar_valor("8"), 52, 59), ("9", lambda: entrar_valor("9"), 52, 118),
    ("*", lambda: entrar_valor("*"), 52, 177), ("4", lambda: entrar_valor("4"), 104, 0), ("5", lambda: entrar_valor("5"), 104, 59),
    ("6", lambda: entrar_valor("6"), 104, 118), ("-", lambda: entrar_valor("-"), 104, 177), ("1", lambda: entrar_valor("1"), 156, 0),
    ("2", lambda: entrar_valor("2"), 156, 59), ("3", lambda: entrar_valor("3"), 156, 118), ("+", lambda: entrar_valor("+"), 156, 177),
    ("0", lambda: entrar_valor("0"), 208, 0), (".", lambda: entrar_valor("."), 208, 118), ("=", calcular, 208, 177)
]

for texto, comando, y, x in botoes:
    b = Button(frame_quadros, text=texto, width=5, height=2, bg=co3, fg=fundo, font=("Ivy 13 bold"),
               relief=RAISED, overrelief=RIDGE, command=comando)
    b.place(x=x, y=y)

janela.mainloop()
