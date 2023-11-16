from models.Pessoa import Pessoa

class FuncionarioHogwarts(Pessoa):
    def __init__(self, nome, sobrenome, funcao="Em contratação"):
        super().__init__(nome, sobrenome)
        self.funcao = funcao

    def add_funcao(self, funcao):
        if self.funcao == "Em contratação":
            self.funcao = funcao
        else:
            return "Já tem sua função!"
        
    def __repr__(self):
        return "Funcionário: " + super().__repr__() + " " + self.funcao
        
if __name__ == "__main__":
    snape = FuncionarioHogwarts("Severo", "Snape", "Professor")
    argo = FuncionarioHogwarts("Argo", "Filch")
    print(snape)
    print(argo)

