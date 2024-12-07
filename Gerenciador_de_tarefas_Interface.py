import tkinter as tk
from tkinter import messagebox


class GerenciadorTarefas:
    def __init__(self):
        # Inicializa a lista de tarefas
        self.tarefas = []

        # Configuração da janela principal
        self.root = tk.Tk()
        self.root.title("Gerenciador de Tarefas")

        # Widgets da interface
        self.label_titulo = tk.Label(self.root, text="Tarefas", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.lista_tarefas = tk.Listbox(self.root, width=50, height=10)
        self.lista_tarefas.pack(pady=10)

        self.entry_tarefa = tk.Entry(self.root, width=40)
        self.entry_tarefa.pack(pady=5)

        self.botao_adicionar = tk.Button(self.root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_adicionar.pack(pady=5)

        self.botao_concluir = tk.Button(self.root, text="Concluir Tarefa", command=self.concluir_tarefa)
        self.botao_concluir.pack(pady=5)

    def adicionar_tarefa(self):
        """Adiciona uma nova tarefa."""
        descricao = self.entry_tarefa.get()
        if descricao:
            nova_tarefa = {"descricao": descricao, "concluida": False}
            self.tarefas.append(nova_tarefa)
            self.entry_tarefa.delete(0, tk.END)
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Tarefa adicionada!")
        else:
            messagebox.showwarning("Erro", "A descrição da tarefa não pode estar vazia.")

    def concluir_tarefa(self):
        """Marca uma tarefa selecionada como concluída."""
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            indice = selecionado[0]
            self.tarefas[indice]["concluida"] = True
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Tarefa concluída!")
        else:
            messagebox.showwarning("Erro", "Nenhuma tarefa selecionada.")

    def atualizar_lista(self):
        """Atualiza a lista de tarefas exibida."""
        self.lista_tarefas.delete(0, tk.END)
        for i, tarefa in enumerate(self.tarefas, 1):
            status = "✅" if tarefa["concluida"] else "❌"
            self.lista_tarefas.insert(tk.END, f"{i}. {tarefa['descricao']} - {status}")

    def executar(self):
        """Inicia a interface gráfica."""
        self.root.mainloop()


if __name__ == "__main__":
    app = GerenciadorTarefas()
    app.executar()
