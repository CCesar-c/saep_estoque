import tkinter as tk
from tkinter import messagebox
from banco import cadastrar_produto


janela = tk.Tk()
janela.title("Saep estoque tactil")
janela.geometry("500x400")
titulo = tk.Label(
    janela,
    text="Saep estoqu tactil",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

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

def salvar():
    nome = entrada_nome.get()
    categoria = entrada_categoria.get()
    quantidade = entrada_quantidade.get()
    preco = entrada_preco.get()