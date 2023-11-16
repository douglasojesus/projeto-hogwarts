from docs.AlunoHogwarts import AlunoHogwarts
from docs.EscolaHogwarts import EscolaHogwarts
from docs.FuncionarioHogwarts import FuncionarioHogwarts

def listar_pessoas(pessoas):
    for pessoa in pessoas:
        print(pessoa)

def main():
    ESCOLA = EscolaHogwarts()
    harry = AlunoHogwarts("Harry", "Potter", "Grifinória", 1, "Varinha 1")
    hermione = AlunoHogwarts("Hermione", "Granger", "Grifinória", 1, "Varinha 2")
    ron = AlunoHogwarts("Ron", "Weasley", "Grifinória", 1, "Varinha 3")
    draco = AlunoHogwarts("Draco", "Malfoy", "Sonserina", 1, "Varinha 4")
    ESCOLA.add_aluno(harry, hermione, ron, draco)
    #listar_pessoas(ESCOLA.todos_alunos())
    snape = FuncionarioHogwarts("Severo", "Snape", "Professor")
    argo = FuncionarioHogwarts("Argo", "Filch")
    ESCOLA.add_func(snape, argo)
    #listar_pessoas(ESCOLA.todos_funcs())
    argo.adicionar_animal("Gato")
    argo.add_funcao("Zelador")
    harry.adicionar_animal("Coruja")
    listar_pessoas(ESCOLA.todos_alunos())
    listar_pessoas(ESCOLA.todos_funcs())

main()
