import tkinter as tk
from tkinter import messagebox
from knapsack import knapsack
from utils import validar_peso, validar_valor

class PlanejadorMochila:
    def __init__(self, root):
        self.root = root
        self.root.title("Planejador de Mochila para Viagens")
        self.itens = []

        # Entrada de peso máximo
        tk.Label(root, text="Peso máximo da mochila:").grid(row=0, column=0, padx=10, pady=5)
        self.peso_maximo_entry = tk.Entry(root)
        self.peso_maximo_entry.grid(row=0, column=1, padx=10, pady=5)

        # Entradas para item
        tk.Label(root, text="Nome do item:").grid(row=1, column=0, padx=10, pady=5)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Peso:").grid(row=2, column=0, padx=10, pady=5)
        self.peso_entry = tk.Entry(root)
        self.peso_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Valor:").grid(row=3, column=0, padx=10, pady=5)
        self.valor_entry = tk.Entry(root)
        self.valor_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botões
        tk.Button(root, text="Adicionar Item", command=self.adicionar_item).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Calcular Mochila", command=self.calcular_mochila).grid(row=5, column=0, columnspan=2, pady=5)

        # Lista de itens
        self.lista_itens = tk.Text(root, width=40, height=10)
        self.lista_itens.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def adicionar_item(self):
        try:
            nome = self.nome_entry.get()
            peso = validar_peso(self.peso_entry.get())
            valor = validar_valor(self.valor_entry.get())

            self.itens.append((nome, peso, valor))
            self.lista_itens.insert(tk.END, f"{nome} - Peso: {peso}, Valor: {valor}\n")
            self.nome_entry.delete(0, tk.END)
            self.peso_entry.delete(0, tk.END)
            self.valor_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def calcular_mochila(self):
        try:
            peso_maximo = validar_peso(self.peso_maximo_entry.get())
            valor_total, escolhidos = knapsack(peso_maximo, self.itens)
            resultado = f"Valor Total: {valor_total}\nItens Escolhidos:\n"
            for nome, peso, valor in escolhidos:
                resultado += f"{nome} - Peso: {peso}, Valor: {valor}\n"
            messagebox.showinfo("Resultado", resultado)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanejadorMochila(root)
    root.mainloop()
