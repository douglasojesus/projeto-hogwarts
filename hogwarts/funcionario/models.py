from django.db import models
from pessoa.models import Pessoa

class FuncionarioHogwarts(Pessoa, models.Model):
    funcao = models.CharField(max_length=100, default="Em contratação")

    def add_funcao(self, funcao):
        if self.funcao == "Em contratação":
            self.funcao = funcao
        else:
            return "Já tem sua função!"
        
    def __repr__(self):
        return f"Funcionário: {super().__repr__()} Função: {self.funcao}"

    # Se preferir, você pode usar o método __str__ ao invés de __repr__ para representação mais amigável em strings.
    def __str__(self):
        return f"{super().__str__()} - Função: {self.funcao}"

if __name__ == "__main__":
    snape = FuncionarioHogwarts.objects.create(nome="Severo", sobrenome="Snape", funcao="Professor")
    argo = FuncionarioHogwarts.objects.create(nome="Argo", sobrenome="Filch")
    print(snape)
    print(argo)
