from django.db import models
from pessoa.models import Pessoa

class AlunoHogwarts(Pessoa, models.Model):
    casa = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    varinha = models.CharField(max_length=50)
    
    def __repr__(self):
        return f"Aluno: {super().__repr__()} Casa: {self.casa} Ano: {self.ano} Varinha: {self.varinha}"

# Se preferir, você pode usar o método __str__ ao invés de __repr__ para representação mais amigável em strings.
    def __str__(self):
        return f"{super().__str__()} - Casa: {self.casa}, Ano: {self.ano}, Varinha: {self.varinha}"
