import sqlite3

# 1. Conectar ao Banco de Dados (ou Criar um novo)
# Usando a Função connect do modulo sqlite3 para se conactar a um Banco de dados SQLite.
# Chamado 'exemplo.db', se o BD não existir ele será criado AUTOMATICAMENTE
conn = sqlite3.connect('exemplo.db')

# 2. Criar um Objeto Cursor
# O cursor é usado paraexecutar comandos SQL no BD
# Ele atua como uma especie de ponteiro que percorre os resultados de consulta
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
# Defini uma String create_table que contem um comando SQL para criar uma tabela chamada "Produtos"
# Esta tabela terá quatro colunas: id (chave primaria), nome (texto), preco (numero real), e estoque(numero inteiro).
# O IF NOT EXISTS garante que a tabela só será criada se ainda não existir
create_table = """
CREATE TABLE IF NOT EXISTS Produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER
);
 """
# Use o metodo exucute do objeto cursor para executar o comando SQL definido anteriormente e criar a tabela no BD
# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)


# 5. Confirmar as alterações no banco de dados
conn.commit()

# 6. Fechar a conexão
conn.close()


# Adicionar produto
# Conectar ao BD
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# Dados do novo Produto
novo_produto = ('Camiseta', 19.99, 50)
# Comando SQL para inserir noco produto na tabela
inserir_produto = "INSERT INTO Produtos (nome,preco,estoque) VALUES (?,?,?) "
# Executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)
# Confirmando as alterações
conn.commit()
# Fechandoa Conexão
conn.close()

# Visualizar Produto
# Conactando ao BD
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# Comando SQL para selecionar Todos os Produtos
selecionar_produtos = "SELECT * FROM Produtos"
# Executando o Comando SQL
cursor.execute(selecionar_produtos)
# Obtendo Todos os Registtros e Exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
# Fechando a Conecxão
conn.close()


# Atualizar Produto
# Conectando ao BD
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# Novo preço e ID do produto a ser atualizado 
novo_preco = 24.99
produto_id = 1 # Supondo que atualizaremos o produto de id 1
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
# Executando o comando SQL de atualização
cursor.execute(atualizar_preco,(novo_preco, produto_id))
# Confirmando as Alterações
conn.commit()
# Fechando a Conexão
conn.close()


# Excluir Produto 
# Conectando ao BD
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# ID do produto a ser excluido
produto_id = 1
# comando SQL para Excluir o produto 
excluir_produto = "DELETE FROM Produtos WHERE id = ?"
#Executando o Comando Delete
cursor.execute(excluir_produto, (produto_id,))
# Confirmando 
conn.commit()
# Fechando Conexão
conn.close()