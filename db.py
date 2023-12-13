from tkinter import *
from tkinter import ttk

janela_inicial = Tk()
janela_inicial.geometry('600x600')
janela_inicial.title('Estoque')
janela_inicial.resizable(False, False)

lbl_nome = ttk.Label(janela_inicial, text='Nome do Produto')
lbl_nome.pack()
en_nome = ttk.Entry(janela_inicial, name='n_produto', width=40)
en_nome.pack()

lbl_quantity = ttk.Label(janela_inicial, text='quantidade')
lbl_quantity.pack()
en_quantity = ttk.Entry(janela_inicial, name='quantidade', width=40)
en_quantity.pack()

lbl_price = ttk.Label(janela_inicial, text='Preço do Produto')
lbl_price.pack()
en_price = ttk.Entry(janela_inicial, name='preco', width=40)
en_price.pack()

lbl_gelado = ttk.Label(janela_inicial, text='Produto Gelado? ')
lbl_gelado.pack()
en_gelado = ttk.Entry(janela_inicial, name='gelado', width=40)
en_gelado.pack()

lbl_erro = ttk.Label(janela_inicial, text='')
lbl_erro.pack()

def create_product():
    name = en_nome.get()
    quantidade = en_quantity.get()
    preco = en_price.get() 
    produtogelado = en_gelado.get()
    if '' in [name, quantidade, preco, produtogelado]:
        lbl_erro.configure(text='Algum campo está vazio')
    if int(preco) <=  0:
        lbl_erro.configure(text='Preço invalido')

def clean_form(): 
    pass 


btn_create = ttk.Button(janela_inicial, text='Criar Produto', command=create_product)
btn_create.pack()
btn_create = ttk.Button(janela_inicial, text='Limpar formulário', command=clean_form)
btn_create.pack()

janela_inicial.mainloop()
