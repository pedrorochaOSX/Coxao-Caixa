from tkinter import *

start = False

if(start == False):
  newClient = 0
  numClients = 0
  moneyClient = 0.0
  moneyDay = 0.0

class Caixa:

  def __init__(self, newClient, numClients, moneyClient, moneyDay, start):

    if(start == False):
      self.newClient = newClient
      self.numClients = numClients
      self.moneyClient = moneyClient
      self.moneyDay = moneyDay

    self.message = Label(window, text='CAIXA ABERTO',background='#FFAE6B', font='arial 30 bold')
    self.message.pack()

    self.clients = Label(window, text='CLIENTES: %d' %(self.numClients),background='#FFAE6B', font='arial 15 bold')
    self.clients.place(x=10,y=530)

    self.faturamento = Label(window, text='FATURAMENTO: R$%.2f' %(self.moneyDay),background='#FFAE6B', font='arial 15 bold')
    self.faturamento.place(x=10,y=560)

    self.botao1 = Button(window,text='NOVO CLIENTE',font='arial 9 bold', command=self.Client)
    self.botao1.place(height=50,width=100,x=350,y=400)

    self.botao2 = Button(window, text="PAGAR",font='arial 9 bold', command=self.Payment)

    self.botao3 = Button(window, text="CANCELAR",background='red',font='arial 9 bold', command=self.Cancel)

    self.pagar = Label(window,text='VALOR A PAGAR: R$%.2f' %(self.moneyClient), background='#FFAE6B', font='arial 20')

    self.entrada = Entry(window, font='arial 15')

    self.entrada.destroy()
    self.botao2.destroy()
    self.botao3.destroy()
    self.pagar.destroy()
    

  def Client(self):   
    global start

    start = True

    self.message.destroy()
    self.message = Label(window, text='DIGITE O VALOR DOS PRODUTOS',background='#FFAE6B', font='arial 30 bold')
    self.message.pack()

    self.numClients = (self.numClients + 1)
    self.moneyClient = 0

    self.pagar = Label(window,text='VALOR A PAGAR: R$%.2f' %(self.moneyClient), background='#FFAE6B', font='arial 20')
    self.pagar.pack()

    self.entrada = Entry(window,font='arial 15')
    self.entrada.place(height=20,width=100,x=350,y=300)

    self.botao1 = Button(window, text="ADICIONAR",background='grey',font='arial 9 bold', command=self.Prices)
    self.botao1.place(height=50,width=100,x=350,y=400)

    self.botao2 = Button(window, text="PAGAR",font='arial 9 bold', command=self.Payment)
    self.botao2.place(height=50,width=100,x=200,y=400)

    self.botao3 = Button(window, text="CANCELAR",background='red',font='arial 9 bold', command=self.Cancel)
    self.botao3.place(height=50,width=100,x=500,y=400)

  def Prices(self):   
    self.moneyClient = float(self.entrada.get()) + self.moneyClient

    self.pagar.destroy()
    self.pagar = Label(window,text='VALOR A PAGAR: R$%.2f' %(self.moneyClient), background='#FFAE6B', font='arial 20')
    self.pagar.pack()

    self.entrada.delete(0,'end')
    self.clients = Label(window, text='CLIENTES: %d' %(self.numClients),background='#FFAE6B', font='arial 15 bold')

  def Payment(self):
    self.moneyDay += self.moneyClient
    self.entrada.delete(0,'end')
  
    self.clients.destroy()
    self.faturamento.destroy()
    self.message.destroy()
    self.pagar.destroy()
    self.botao2.destroy()
    self.botao3.destroy()
    self.entrada.destroy()

    self.botao1 = Button(window,text='NOVO CLIENTE',font='arial 9 bold', command=self.Client)
    self.botao1.place(height=50,width=100,x=350,y=400)

    self.faturamento = Label(window, text='FATURAMENTO: R$%.2f' %(self.moneyDay),background='#FFAE6B', font='arial 15 bold')
    self.faturamento.place(x=10,y=560)

    self.message = Label(window, text='CAIXA ABERTO',background='#FFAE6B', font='arial 30 bold')
    self.message.pack()

    self.clients = Label(window, text='CLIENTES: %d' %(self.numClients),background='#FFAE6B', font='arial 15 bold')
    self.clients.place(x=10,y=530)
   
  def Cancel(self):
    self.moneyClient = 0
    self.numClients -= 1

    self.message.destroy()
    self.pagar.destroy()
    self.botao2.destroy()
    self.botao3.destroy()
    self.entrada.destroy()

    self.botao1 = Button(window,text='NOVO CLIENTE',font='arial 9 bold', command=self.Client)
    self.botao1.place(height=50,width=100,x=350,y=400)

    self.faturamento = Label(window, text='FATURAMENTO: R$%.2f' %(self.moneyDay),background='#FFAE6B', font='arial 15 bold')
    self.faturamento.place(x=10,y=560)

    self.message = Label(window, text='CAIXA ABERTO',background='#FFAE6B', font='arial 30 bold')
    self.message.pack()

    self.clients = Label(window, text='CLIENTES: %d' %(self.numClients),background='#FFAE6B', font='arial 15 bold')
    self.clients.place(x=10,y=530)


window = Tk()
window.title('Coxão Caixas')
window.configure(background='#FFAE6B')
window.resizable(width = False, height = False)
window.minsize(width = 800, height = 600) 
window.iconbitmap("coxinha.ico")

caixa = Caixa(newClient, numClients, moneyClient, moneyDay, start)

window.mainloop()