class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade

    # Getter
    @property
    def idade(self):
        return self.idade

    # Setter
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._idade = valor


pessoa1 = Pessoa('kauan', -10)
print(pessoa1.idade)