class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.animal_estimacao = ""

    def adicionar_animal(self, animal):
        self.animal_estimacao = animal

    def __repr__(self):
        return "Nome: " + self.nome + " " + self.sobrenome + " " + self.animal_estimacao


    