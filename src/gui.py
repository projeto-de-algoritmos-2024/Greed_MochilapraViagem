from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMessageBox
)
from knapsack import knapsack
from utils import validar_peso, validar_valor

class PlanejadorMochila(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planejador de Mochila para Viagens")
        self.resize(600, 500)
        self.itens = []

        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()

        # Entrada de peso máximo
        self.peso_maximo_label = QLabel("Peso máximo da mochila:")
        layout.addWidget(self.peso_maximo_label)
        self.peso_maximo_entry = QLineEdit()
        layout.addWidget(self.peso_maximo_entry)
        self.peso_maximo_entry.editingFinished.connect(self.desativar_peso_maximo)

        # Entradas para item
        self.nome_label = QLabel("Nome do item:")
        layout.addWidget(self.nome_label)
        self.nome_entry = QLineEdit()
        layout.addWidget(self.nome_entry)

        self.peso_label = QLabel("Peso:")
        layout.addWidget(self.peso_label)
        self.peso_entry = QLineEdit()
        layout.addWidget(self.peso_entry)

        self.valor_label = QLabel("Valor:")
        layout.addWidget(self.valor_label)
        self.valor_entry = QLineEdit()
        layout.addWidget(self.valor_entry)

        # Botões
        self.adicionar_item_button = QPushButton("Adicionar Item")
        self.adicionar_item_button.clicked.connect(self.adicionar_item)
        layout.addWidget(self.adicionar_item_button)

        self.calcular_mochila_button = QPushButton("Calcular Mochila")
        self.calcular_mochila_button.clicked.connect(self.calcular_mochila)
        layout.addWidget(self.calcular_mochila_button)

        # Lista de itens
        self.lista_itens = QTextEdit()
        self.lista_itens.setReadOnly(True)
        layout.addWidget(self.lista_itens)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
 

    def desativar_peso_maximo(self):
        if self.peso_maximo_entry.text():
            self.peso_maximo_entry.setReadOnly(True)

    def adicionar_item(self):
        try:
            nome = self.nome_entry.text()
            peso = validar_peso(self.peso_entry.text())
            valor = validar_valor(self.valor_entry.text())

            self.itens.append((nome, peso, valor))
            self.lista_itens.append(f"{nome} - Peso: {peso}, Valor: {valor}")
            self.nome_entry.clear()
            self.peso_entry.clear()
            self.valor_entry.clear()
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))

    def calcular_mochila(self):
        try:
            peso_maximo = validar_peso(self.peso_maximo_entry.text())
            valor_total, escolhidos = knapsack(peso_maximo, self.itens)
            resultado = f"Valor Total: {valor_total}\nItens Escolhidos:\n"
            for nome, peso, valor in escolhidos:
                resultado += f"{nome} - Peso: {peso}, Valor: {valor}\n"
            QMessageBox.information(self, "Resultado", resultado)


            # Desativar campos de entrada e botão de adicionar item
            self.peso_maximo_entry.setReadOnly(True)
            self.nome_entry.setReadOnly(True)
            self.peso_entry.setReadOnly(True)
            self.valor_entry.setReadOnly(True)
            self.adicionar_item_button.setEnabled(False)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))