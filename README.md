# Projeto_talentotech
Projeto do Talentotech 


# Gerenciador de Tarefas

## Descrição
Este é um gerenciador de tarefas simples que permite ao usuário:
- Listar tarefas.
- Adicionar novas tarefas.
- Marcar tarefas como concluídas.

## Funcionalidades Planejadas
1. Adicionar opção de editar tarefas.
2. Permitir exclusão de tarefas.
3. Implementar interface gráfica ou API.

## Cronograma de Desenvolvimento
1. **Dia 1:** Configurar ambiente e repositório.
2. **Dia 2:** Implementar funcionalidade de listar e adicionar tarefas.
3. **Dia 3:** Implementar funcionalidade de marcar tarefas como concluídas.
4. **Dia 4:** Documentar e testar.


class GerenciadorTarefas:
    def __init__(self):
        # Inicializa as tarefas a partir do arquivo ou cria uma lista vazia
        self.tarefas = self.carregar_tarefas()

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

    def adicionar_tarefa(self, descricao):
        """Adiciona uma nova tarefa."""
        nova_tarefa = {
            "descricao": descricao,
            "concluida": False
        }
        self.tarefas.append(nova_tarefa)
        self.salvar_tarefas()
        print(f"Tarefa adicionada: {descricao}")

    def listar_tarefas(self):
        """Lista todas as tarefas com status."""
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return

        print("\nTarefas:")
        for i, tarefa in enumerate(self.tarefas, 1):
            status = "✅" if tarefa["concluida"] else "❌"
            print(f"{i}. {tarefa['descricao']} - {status}")

    def concluir_tarefa(self, numero):
        """Marca uma tarefa como concluída."""
        if 1 <= numero <= len(self.tarefas):
            self.tarefas[numero - 1]["concluida"] = True
            self.salvar_tarefas()
            print(f"Tarefa {numero} marcada como concluída.")
        else:
            print("Número de tarefa inválido.")

    def executar(self):
        """Executa o menu principal do gerenciador."""
        while True:
            print("\nGerenciador de Tarefas")
            print("1. Listar Tarefas")
            print("2. Adicionar Tarefa")
            print("3. Concluir Tarefa")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_tarefas()
            elif escolha == "2":
                descricao = input("Digite a descrição da tarefa: ")
                self.adicionar_tarefa(descricao)
            elif escolha == "3":
                self.listar_tarefas()
                try:
                    numero = int(input("Digite o número da tarefa para concluir: "))
                    self.concluir_tarefa(numero)
                except ValueError:
                    print("Por favor, insira um número válido.")
            elif escolha == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.executar()
