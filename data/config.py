import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("amarelinho.db")
cursor = conn.cursor()

categorias = [
    ('Lanches',),
    ('Açaís',),
    ('Bebidas',),
    ('Batatas',)
]

cursor.executemany("""
INSERT INTO categorias (nome) VALUES (?)
""", categorias)

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão
conn.close()

