import tkinter as tk
from tkinter import messagebox
import json
import os

# Caminho para o arquivo de persistência
ARQUIVO_TAREFAS = "tarefas.json"


class GerenciadorTarefasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.tarefas = self.carregar_tarefas()

        # Widgets da interface
        self.label_titulo = tk.Label(root, text="Tarefas", font=("Arial", 16))
        self.label_titulo.pack()

        self.lista_tarefas = tk.Listbox(root, width=50, height=15)
        self.lista_tarefas.pack()

        self.entrada_tarefa = tk.Entry(root, width=40)
        self.entrada_tarefa.pack(pady=5)

        self.botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_adicionar.pack(pady=5)

        self.botao_concluir = tk.Button(root, text="Concluir Tarefa", command=self.concluir_tarefa)
        self.botao_concluir.pack(pady=5)

        self.carregar_lista_tarefas()

    def carregar_tarefas(self):
        """Carrega as tarefas do arquivo JSON."""
        if os.path.exists(ARQUIVO_TAREFAS):
            with open(ARQUIVO_TAREFAS, "r") as arquivo:
                return json.load(arquivo)
        return []

    def salvar_tarefas(self):
        """Salva as tarefas no arquivo JSON."""
        with open(ARQUIVO_TAREFAS, "w") as arquivo:
            json.dump(self.tarefas, arquivo, indent=4)

    def carregar_lista_tarefas(self):
        """Atualiza a lista exibida na interface."""
        self.lista_tarefas.delete(0, tk.END)
        for i, tarefa in enumerate(self.tarefas, 1):
            status = "✅" if tarefa["concluida"] else "❌"
            self.lista_tarefas.insert(tk.END, f"{i}. {tarefa['descricao']} - {status}")

    def adicionar_tarefa(self):
        """Adiciona uma nova tarefa."""
        descricao = self.entrada_tarefa.get()
        if descricao:
            nova_tarefa = {"descricao": descricao, "concluida": False}
            self.tarefas.append(nova_tarefa)
            self.salvar_tarefas()
            self.carregar_lista_tarefas()
            self.entrada_tarefa.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Tarefa adicionada!")
        else:
            messagebox.showwarning("Erro", "A descrição não pode estar vazia.")

    def concluir_tarefa(self):
        """Marca a tarefa selecionada como concluída."""
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            indice = selecionado[0]
            self.tarefas[indice]["concluida"] = True
            self.salvar_tarefas()
            self.carregar_lista_tarefas()
            messagebox.showinfo("Sucesso", "Tarefa marcada como concluída!")
        else:
            messagebox.showwarning("Erro", "Nenhuma tarefa selecionada.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefasGUI(root)
    root.mainloop()
