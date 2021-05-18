class Pessoa:
    def __init__(self, nome, cpf, data_de_nascimento, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.email = email
        self.telefone = telefone

    def alteraInformacao(self, informacao):
        if informacao == "nome":
            self.nome = input("Digite o nome: ")
        elif informacao == "cpf":
            self.cpf = input("Digite o cpf: ")
        elif informacao == "data_de_nascimento":
            self.data_de_nascimento = input("Digite a data de nascimento(dd/mm/YY): ")
        elif informacao == "email":
            self.email = input("Digite o e-mail: ")
        elif informacao == "telefone":
            self.telefone = input("Digite o telefone: ")