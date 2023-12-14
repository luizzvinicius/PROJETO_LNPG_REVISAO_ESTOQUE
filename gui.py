from tkinter import *
from tkinter import ttk
import estoque

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

v0 = BooleanVar()
v0.set(False)
check_gelado = ttk.Checkbutton(janela_inicial, text="Produto gelado", variable=v0)
check_gelado.pack()

lbl_erro = ttk.Label(janela_inicial, text='')
lbl_erro.pack()


def create_product():
    name = en_nome.get()
    quantidade = en_quantity.get()
    preco = en_price.get() 
    check_gelado = v0.get()
    print(check_gelado)
    if '' in [name, quantidade, preco]:
        lbl_erro.configure(text='Algum campo está vazio')
        return
    if preco <= '0':
        lbl_erro.configure(text='Preço inválido')
        return
    estoque.write(name, quantidade, preco, check_gelado)


def clean_form(): 
    en_nome.delete(0, END)
    en_quantity.delete(0, END)
    en_price.delete(0, END)


btn_create = ttk.Button(janela_inicial, text='Criar Produto', command=create_product)
btn_create.pack()
btn_create = ttk.Button(janela_inicial, text='Limpar formulário', command=clean_form)
btn_create.pack()

tr = ttk.Treeview(janela_inicial, columns=("Nome", "Quantidade", "Preco", "Produto gelado"), show="headings")
tr.column("Nome", minwidth=10, width=80, )
tr.column("Quantidade", minwidth=10, width=80, )
tr.column("Preco", minwidth=10, width=120, )
tr.column("Produto gelado", minwidth=30, width=160)
tr.heading("Nome", text="Nome")
tr.heading("Quantidade", text="Quantidade")
tr.heading("Preco", text = "Preço")
tr.heading("Produto gelado", text="Produto gelado")
tr.pack()

def listar():
    for i in tr.get_children():
            tr.delete(i)
    produtos = estoque.read()
    
    for item in produtos:
            item = item.split("|")
            gelado = 'Sim' if item[3] else 'Não'
            tr.insert("", "end", values=[item[0], item[1], item[2], gelado])
    

btn_create = ttk.Button(janela_inicial, text='listar produtos', command=listar)
btn_create.pack()

janela_inicial.mainloop()
