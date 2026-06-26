import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from banco import cadastrar_produto, listar_produtos, excluir_produto

janela = tk.Tk()
janela.title("Saep estoque tactil")
janela.geometry("500x400")

frame_botoes = tk.Frame(janela, bg="#f4f6f8")
frame_botoes.pack(pady=10)

titulo = tk.Label(
    janela,
    text="Saep Estoque Tactil",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)


tabela = ttk.Treeview(
    janela,
    columns=("id", "nome", "categoria", "quantidade", "preco"),
    show="headings"
)

tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("categoria", text="Categoria")
tabela.heading("quantidade", text="Qtd")
tabela.heading("preco", text="Preco")

tabela.column("id", width=50)
tabela.column("nome", width=160)
tabela.column("categoria", width=140)
tabela.column("quantidade", width=80)
tabela.column("preco", width=80)

tabela.pack(pady=10)
def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_categoria.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)



def salvar():
    nome = entrada_nome.get()
    categoria = entrada_categoria.get()
    quantidade = entrada_quantidade.get()
    preco = entrada_preco.get()
    if nome == "" or categoria == "" or quantidade == "" or preco == "":
        messagebox.showwarning("Atençao", "Preencha todos os campos")
        return
    try:
        quantidade = int(quantidade)
        preco = float(preco)
    except ValueError:
        messagebox.showwarning(
          "Atenção",
          "Quantidade deve ser número inteiro e preço deve usar ponto. Exemplo: 2.50"
        )
        return
   
    if quantidade < 0:
      messagebox.showwarning("Atenção", "A quantidade não pode ser negativa.")
      return
   
    if preco <= 0:
      messagebox.showwarning("Atenção", "O preço deve ser maior que zero.")
      return

    cadastrar_produto(nome, categoria, int(quantidade), float(preco))
    messagebox.showinfo("Sucesso", "Produto cadastrar com sucesso!")
    
    entrada_nome.delete(0, tk.END)
    entrada_categoria.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    
    atualizar_tabela()

def excluir():
    item_selecionado = tabela.selection()

    if not item_selecionado:
       messagebox.showwarning("Atenção", "Selecione um produto para excluir.")
       return

    item = tabela.item(item_selecionado)
    id_produto = item["values"][0]

    resposta = messagebox.askyesno(
        "Confirmar exclusão",
       "Deseja realmente excluir o produto selecionado?"
    )

    if resposta:
        excluir_produto(id_produto)
        atualizar_tabela()
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")


def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)
    
    produtoLista = listar_produtos() # produtos

    for produto in produtoLista:
        tabela.insert("", tk.END, values=produto)

atualizar_tabela()

botao_excluir = tk.Button(
    frame_botoes,
    text="Excluir Produto",
    command=excluir,
    width=20,
    bg="#e7490f",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_excluir.grid(row=0, column=2, padx=5)
tk.Label(janela, text="Nome do produto: ").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="Categoria: ").pack()
entrada_categoria = tk.Entry(janela, width=40)
entrada_categoria.pack()

tk.Label(janela, text="Quantidade: ").pack()
entrada_quantidade = tk.Entry(janela, width=40)
entrada_quantidade.pack()

tk.Label(janela, text="Preco: ").pack()
entrada_preco = tk.Entry(janela, width=40)
entrada_preco.pack()



botao_salvar = tk.Button(
    frame_botoes,
    text="Cadastrar Produto",
    command=salvar,
    width=20,
    bg="#164193",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_salvar.grid(row=0, column=0, padx=5)


botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar Campos",
    command=limpar_campos,
    width=20
)
botao_limpar.grid(row=0, column=1, padx=5)
janela.mainloop()
