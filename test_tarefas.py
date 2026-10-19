import unittest

from tarefas import adicionar_tarefa, tarefas


class TestTarefas(unittest.TestCase):
    def setUp(self):
        tarefas.clear()

    def test_prioridade_informada(self):
        tarefa = adicionar_tarefa("Revisar requisitos", "alta")
        self.assertEqual(tarefa["prioridade"], "alta")
        self.assertFalse(tarefa["concluida"])
        self.assertEqual(tarefas, [tarefa])

    def test_prioridade_padrao(self):
        tarefa = adicionar_tarefa("Documentar")
        self.assertEqual(tarefa["prioridade"], "media")

    def test_normalizacao(self):
        tarefa = adicionar_tarefa("  Revisar  ", " ALTA ")
        self.assertEqual(tarefa["titulo"], "Revisar")
        self.assertEqual(tarefa["prioridade"], "alta")

    def test_titulo_vazio(self):
        with self.assertRaises(ValueError):
            adicionar_tarefa("   ")
        self.assertEqual(len(tarefas), 0)

    def test_prioridade_invalida(self):
        with self.assertRaises(ValueError):
            adicionar_tarefa("Revisar", "urgente")
        self.assertEqual(len(tarefas), 0)


if __name__ == "__main__":
    unittest.main()
