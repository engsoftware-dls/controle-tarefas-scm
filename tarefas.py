PRIORIDADES = {"baixa", "media", "alta"}
tarefas = []

def adicionar_tarefa(titulo, prioridade="media"):
    titulo = titulo.strip()
    prioridade = prioridade.strip().lower()

    if not titulo:
        raise ValueError("O titulo e obrigatorio.")

    if prioridade not in PRIORIDADES:
        raise ValueError("Prioridade invalida.")

    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade,
        "concluida": False,
    }
    tarefas.append(tarefa)
    return tarefa

if __name__ == "__main__":
    adicionar_tarefa("Revisar requisitos", "alta")
    for tarefa in tarefas:
        print(tarefa)
