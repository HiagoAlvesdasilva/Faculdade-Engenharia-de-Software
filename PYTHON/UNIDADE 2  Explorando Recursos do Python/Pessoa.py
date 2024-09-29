# Define uma classe chamada Pessoa
class Pessoa:
    # O Metodo __init__ é um construtor, chamado quando um objeto da classe é criado
    # Ele inicializa os atributos da classe
    def __init__(self, nome, idade, genero): 
        # self é uma uma convenção em Python que se refere à própria instância da classe
        # Os parâmetros nome, idade e genero são passados durante a criação do objeto
        # Eles são usados para inicializar os atributos da instância
        self.nome = nome  # Atribui o valor de nome ao atributo nome da instância
        self.idade = idade  # ----
        self.genero = genero  # -----

    # O Método cumprimentar retorna uma saudação com o nome da Pessoa
    def cumprimentar(self):
        return f"Olá, Meu Nome é: {self.nome}."

    # O Método aniversario aumenta a idade da pessoa em 1
    def aniversario(self):
        self.idade += 1


# Cria uma Instância da Classe Pessoa
pessoa1 = Pessoa("João", 30, "Masculino")

# Chama o método cumprimentar
print(pessoa1.cumprimentar())  

# Chama o método idade
print(f"Idade: {pessoa1.idade}")

# Chama o método aniversario
pessoa1.aniversario()

# Acessa o atributo idade atualizado da instância pessoa1 e imprime a nova idade
print(f"Nova Idade: {pessoa1.idade}")
