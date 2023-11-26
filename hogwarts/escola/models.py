from django.db import models
from aluno.models import Aluno
from funcionario.models import Funcionario

class EscolaHogwarts(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno)
    funcionarios = models.ManyToManyField(Funcionario)

    def add_aluno(self, *alunos_a_serem_add):
        for aluno in alunos_a_serem_add:
            self.alunos.add(aluno)

    def add_func(self, *funcs_a_serem_add):
        for func in funcs_a_serem_add:
            self.funcionarios.add(func)

    def busca_aluno(self, id):
        return self.alunos.get(id=id) if self.alunos.filter(id=id).exists() else None

    def todos_alunos(self):
        return self.alunos.all()

    def todos_funcs(self):
        return self.funcionarios.all()
