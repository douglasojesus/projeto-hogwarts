class EscolaHogwarts:
    def __init__(self):
        self.alunos = list()
        self.funcionarios = list()

    def add_aluno(self, *alunos_a_serem_add):
        for aluno in alunos_a_serem_add:
            self.alunos.append(aluno)

    def add_func(self, *funcs_a_serem_add):
        for func in funcs_a_serem_add:
            self.funcionarios.append(func)

    def busca_aluno(self, id):
        for aluno in self.alunos:
            if aluno.id == id:
                return aluno
    
    def todos_alunos(self):
        return self.alunos
    
    def todos_funcs(self):
        return self.funcionarios
    
