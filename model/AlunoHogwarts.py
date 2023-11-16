from Pessoa import Pessoa

class AlunoHogwarts(Pessoa):
    id = 0
    def __init__(self, nome, sobrenome, casa, ano, varinha):
        super().__init__(nome, sobrenome)
        self.casa = casa
        self.ano = ano
        self.varinha = varinha
        self.id = AlunoHogwarts.id
        AlunoHogwarts.id += 1
    
    def __repr__(self):
        return "Aluno: " + super().__repr__() + " " + " " + str(self.id)
    
if __name__ == "__main__":
    aluno = AlunoHogwarts("Harry", "Potter", "Grifinória", 1, "Varinha")
    print(aluno)