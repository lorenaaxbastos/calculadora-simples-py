class Calculadora:

    def __init__(self, n1, n2):
        self._n1 = n1
        self._n2 = n2

    @property
    def soma(self):
        return self._n1 + self._n2

    @property
    def multiplicacao(self):
        return self._n1 * self._n2

    @property
    def divisao(self):
        try:
            return self._n1 / self._n2
        except ZeroDivisionError:
            return "Não é possível dividir por zero."

    @property
    def subtracao(self):
        return self._n1 - self._n2

    @property
    def potenciacao(self):
        return self._n1 ** self._n2
    