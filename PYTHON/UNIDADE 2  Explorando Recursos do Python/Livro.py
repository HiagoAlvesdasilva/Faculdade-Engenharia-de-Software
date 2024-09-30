import matplotlib.pyplot as plt

class Livro:
    biblioteca = []  # Lista de livros como atributo de classe
    anos = []  # Lista de anos de publicação como atributo de classe

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"

    @classmethod
    def adicionar_livro(cls, titulo, autor, ano_publicacao):
        novo_livro = Livro(titulo, autor, ano_publicacao)
        cls.biblioteca.append(novo_livro)
        cls.anos.append(ano_publicacao)  # Adiciona o ano à lista de anos
        print(f"O Livro '{titulo}' Foi Adicionado à Biblioteca")

    @classmethod
    def listar_livros(cls):
        print("Livros na Biblioteca:")
        for livro in cls.biblioteca:
            print(livro)


# Adicionando Livros à Biblioteca
Livro.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
Livro.adicionar_livro("Orgulho e Preconceito", "Jane Austen", 1813)
Livro.adicionar_livro("1984", "George Orwell", 1949)
Livro.adicionar_livro("Cem Anos de Solidão", "Gabriel Garcia Marquez", 1967)
Livro.adicionar_livro("Apanhador no Campo de Centeio", "J.D Salinger", 1951)

# Listando Livros
Livro.listar_livros()

# Criar Um Gráfico de Livros por ano
anos_unicos = sorted(set(Livro.anos))  # Remove duplicatas e ordena os anos

# Contagem de Livros por ano
contagem_por_ano = [Livro.anos.count(ano) for ano in anos_unicos]

# Cria um Gráfico de Linhas
plt.plot(anos_unicos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

# Adicionar Rótulos aos Pontos de Dados
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos_unicos[i], valor, str(valor), ha='center', va='bottom')

plt.grid(True)

# Mostrar o Gráfico
plt.show()
