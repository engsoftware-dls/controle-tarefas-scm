# Controle de tarefas

Projeto acadêmico de gerenciamento de configuração com Git e GitHub.

## Versão inicial

Cadastro de tarefas com título obrigatório e situação de conclusão.
Cada tarefa começa com o campo `concluida` igual a `False`.

## Funcionalidades atuais

- Cadastrar tarefa com título não vazio.
- Iniciar cada tarefa com `concluida` igual a `False`.
- Aceitar as prioridades `baixa`, `media` e `alta`.
- Usar `media` como prioridade padrão quando o argumento for omitido.
- Remover espaços nas extremidades do título e da prioridade.
- Converter a prioridade para letras minúsculas antes da validação.
- Rejeitar título vazio ou prioridade inválida com `ValueError`, sem adicionar a tarefa à lista.

## Tecnologia e armazenamento

Python 3. A execução e os testes apresentados neste projeto foram realizados com Python 3.14.
Os dados permanecem somente em memória, sem persistência entre execuções.

## Executar o exemplo

No terminal, dentro da pasta do projeto, usando o seletor Python já utilizado neste ambiente Windows:

```bash
py -V:3.14 tarefas.py
```

Saída esperada:

```text
{'titulo': 'Revisar requisitos', 'prioridade': 'alta', 'concluida': False}
```

## Executar os testes

```bash
py -V:3.14 -m unittest -v
```

A suíte usa `unittest` e contém cinco testes:

1. Cadastro com prioridade informada e situação inicial não concluída.
2. Uso da prioridade padrão.
3. Normalização de título e prioridade.
4. Rejeição de título vazio.
5. Rejeição de prioridade inválida.

Resultado esperado: cinco testes executados e conclusão `OK`.
O tempo de execução pode variar.

## Artefatos

- `tarefas.py`: implementação do cadastro e exemplo de execução.
- `test_tarefas.py`: testes automatizados.
- `requisitos.md`: requisitos do projeto.
- `.gitignore`: regras de exclusão do versionamento.
- `README.md`: apresentação e instruções de execução.
