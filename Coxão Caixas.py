from tkinter import *

newClient = 0; numClients = 0; plus = 0
moneyClient = 0.0; moneyDay = 0.0

def Menu():
  global numClients; global moneyDay; global newClient
  global moneyClient; global plus; global message
  global clientes; global faturamento; global pagar
  global entrada; global botao1; global botao2; global botao3

  message["text"] = 'CAIXA ABERTO'

  clientes['text'] = 'CLIENTES: %d' %(numClients)  

  faturamento['text'] = 'FATURAMENTO: R$%.2f' %(moneyDay)  

  botao1 = Button(window, text="NOVO CLIENTE", command=Client)
  botao1.place(height=50,width=100,x=350,y=400)

  entrada.destroy()
  botao2.destroy()
  botao3.destroy()
  pagar.destroy()

def Client():
  global numClients; global moneyDay; global newClient
  global moneyClient; global plus; global message
  global clientes; global faturamento; global pagar
  global entrada; global botao1; global botao2; global botao3

  numClients = (numClients + 1)
  moneyClient = 0
  pagar = Label(window, text="VALOR A PAGAR: R$",background='#FFAE6B', font='arial 20')
  pagar['text']= 'VALOR A PAGAR: R$%.2f' %(moneyClient)
  pagar.pack()
  
  entrada = Entry(window, font='arial 15')
  entrada.place(height=20,width=100,x=350,y=300)

  message["text"] = 'DIGITE O VALOR DOS PRODUTOS'

  botao1 = Button(window, text="ADICIONAR",background='grey',font='arial 9 bold', command=Prices)
  botao1.place(height=50,width=100,x=350,y=400)

  botao2 = Button(window, text="PAGAR",font='arial 9 bold', command=Payment)
  botao2.place(height=50,width=100,x=200,y=400)

  botao3 = Button(window, text="CANCELAR",background='red',font='arial 9 bold', command=Cancelar)
  botao3.place(height=50,width=100,x=500,y=400)

def Prices():  
  global numClients; global moneyDay; global newClient
  global moneyClient; global plus; global message
  global clientes; global faturamento;global pagar
  global entrada; global botao1; global botao2; global botao3

  plus = int(entrada.get())
  moneyClient = moneyClient + plus
  pagar['text']= 'VALOR A PAGAR: R$%.2f' %(moneyClient)
  entrada.delete(0,'end')
  clientes['text'] = 'CLIENTES: %d' %(numClients)
  plus = 0

def Payment():
  global numClients; global moneyDay; global newClient
  global moneyClient; global plus; global message
  global clientes; global faturamento; global pagar
  global entrada; global botao1; global botao2; global botao3
  
  moneyDay = (moneyDay + moneyClient)
  entrada.delete(0,'end')
  clientes['text'] = 'Clientes: %d' %(numClients)
  Menu()

def Cancelar():
  global numClients; global moneyDay; global newClient
  global moneyClient; global plus; global message
  global clientes; global faturamento; global pagar
  global entrada; global botao1; global botao2; global botao3

  moneyClient = 0
  numClients = numClients - 1
  Menu()

window = Tk()
window.title('Coxão Caixas')
window.configure(background='#FFAE6B')
window.resizable(width = False, height = False)
window.minsize(width = 800, height = 600) 
window.iconbitmap("coxinha.ico")

message = Label(window, text='CAIXA ABERTO',background='#FFAE6B', font='arial 30 bold')
message.pack()

clientes = Label(window, text="CLIENTES: ",background='#FFAE6B', font='arial 15 bold')
clientes['text'] = 'CLIENTES: %d' %(numClients)  
clientes.place(x=10,y=530)

pagar = Label(window, text="Valor a pagar: R$", font='arial 20')

faturamento = Label(window, text="FATURAMENTO: R$",background='#FFAE6B', font='arial 15 bold')
faturamento['text'] = 'FATURAMENTO: R$%.2f' %(moneyDay)  
faturamento.place(x=10,y=560)

entrada = Entry(window, font='arial 15')

botao1 = Button(window, text="NOVO CLIENTE", command=Client, font='arial 9 bold')
botao1.place(height=50,width=100,x=350,y=400)

botao2 = Button(window, text="PAGAR",font='arial 9 bold', command=Payment)

botao3 = Button(window, text="CANCELAR",background='red',font='arial 9 bold', command=Cancelar)

window.mainloop()