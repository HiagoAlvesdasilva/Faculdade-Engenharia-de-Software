import sqlite3

# Criação da conexão e do cursor
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

# Criação da tabela "Contatos"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contatos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT
    )
''')

# Dados de exemplo
dados_exemplo = [
    ('João', 'joao@email.com', '(77) 3422-1077'),
    ('Maria', 'maria@email.com', '(11) 4002-8922'),
    ('Carlos', 'carlos@email.com', '(11) 4035-9875')
]

# Inserção dos dados de exemplo
cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?,?,?)', dados_exemplo)
conn.commit()

# Leitura e exibição dos dados
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()

print("Contatos:")
for contato in contatos:
    print(contato)

# Atualização do número de telefone do contato com ID 2
novo_telefone = '9999-9999'
contato_id = 2
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()

# Exclusão do contato com ID 1
contato_id_para_excluir = 1
cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_para_excluir,))
conn.commit()

# Fechamento da conexão
conn.close()
