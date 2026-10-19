# Requisitos

## Requisitos funcionais

- **RF01:** cadastrar tarefa com título não vazio após a remoção de espaços nas extremidades. Caso o título seja vazio, gerar `ValueError` sem adicionar a tarefa à lista.
- **RF02:** iniciar cada tarefa com o campo `concluida` igual a `False`.
- **RF03:** permitir as prioridades `baixa`, `media` e `alta`.
- **RF04:** utilizar `media` como prioridade padrão quando o argumento de prioridade for omitido.
- **RF05:** remover espaços nas extremidades do título e da prioridade e converter a prioridade para letras minúsculas antes da validação e do armazenamento.
- **RF06:** rejeitar prioridade fora dos valores permitidos com `ValueError`, sem adicionar a tarefa à lista.

## Armazenamento

As tarefas permanecem somente em memória, sem persistência entre execuções.

## Observação sobre a nomenclatura

O RF02 usa `concluida`, nome do campo presente na implementação, em lugar de `concluido` na redação inicial. O comportamento permanece o mesmo: toda tarefa começa não concluída.
