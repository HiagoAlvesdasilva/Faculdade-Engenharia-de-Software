# # Define uma classe chamada Pessoa
# class Pessoa:
#     # O Metodo __init__ é um construtor, chamado quando um objeto da classe é criado
#     # Ele inicializa os atributos da classe
#     def __init__(self, nome, idade, genero):
#         # self é uma uma convenção em Python que se refere à própria instância da classe
#         # Os parâmetros nome, idade e genero são passados durante a criação do objeto
#         # Eles são usados para inicializar os atributos da instância
#         self.nome = nome  # Atribui o valor de nome ao atributo nome da instância
#         self.idade = idade  # ----
#         self.genero = genero  # -----

#     # O Método cumprimentar retorna uma saudação com o nome da Pessoa
#     def cumprimentar(self):
#         return f"Olá, Meu Nome é: {self.nome}."

#     # O Método aniversario aumenta a idade da pessoa em 1
#     def aniversario(self):
#         self.idade += 1


# # Cria uma Instância da Classe Pessoa
# pessoa1 = Pessoa("João", 30, "Masculino")

# # Chama o método cumprimentar
# print(pessoa1.cumprimentar())

# # Chama o método idade
# print(f"Idade: {pessoa1.idade}")

# # Chama o método aniversario
# pessoa1.aniversario()

# # Acessa o atributo idade atualizado da instância pessoa1 e imprime a nova idade
# print(f"Nova Idade: {pessoa1.idade}")

# # Classe Animal
# class Animal:
#     def __init__(self, nome):
#         self.nome = nome

#         def fazer_barulho(self):
#             pass


# class Cachorro (Animal):
#     def fazer_barulho(self):
#         return "Latir"


# class Gato (Animal):
#     def fazer_barulho(self):
#         return "Miar"


# rex = Cachorro("Rex")
# garfield = Gato("Garfield")

# print(f"{rex.nome} faz: {rex.fazer_barulho()}")
# print(f"{garfield.nome} faz: {garfield.fazer_barulho()}")

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def freiar(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} Km/h"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        # Carros podem acelerar mais rapido
        self.velocidade += incremento + self.potencia


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} Km/h"


# Criando Objtos
carro1 = Carro("Toyota", "Corolla", 2022, 100)
bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

# Acelerando e verificando status
carro1.acelerar(50)
bicicleta1.acelerar(20)

# Exibndo Status
print("Status do Carro")
print(carro1.status())

print("Status da Bicicleta")
print(bicicleta1.status())
