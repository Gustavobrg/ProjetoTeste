from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_de_nascimento, email, telefone, senha):
        super().__init__(nome, cpf, data_de_nascimento, email, telefone)
        self.senha = senha

