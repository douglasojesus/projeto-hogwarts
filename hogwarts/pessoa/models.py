from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    animal_estimacao = models.CharField(max_length=100, blank=True, null=True)

    def adicionar_animal(self, animal):
        self.animal_estimacao = animal

    def __repr__(self):
        return f"Nome: {self.nome} {self.sobrenome} Animal de Estimação: {self.animal_estimacao}"

    # Se preferir, você pode usar o método __str__ ao invés de __repr__ para representação mais amigável em strings.
    def __str__(self):
        return f"{self.nome} {self.sobrenome} - Animal de Estimação: {self.animal_estimacao}"
