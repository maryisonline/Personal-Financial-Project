import sqlite3
import os

db_name = r'C:\Users\mary saotome\Documents\database\financial.db'

if not os.path.exists(db_name):
    connect = sqlite3.connect(db_name)
    cursor = connect.cursor()

    cursor.execute(
    '''
        CREATE TABLE flow (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origem TEXT NOT NULL,
        metodo TEXT NOT NULL,
        valor REAL NOT NULL,
        data TEXT NOT NULL,
        tipo TEXT NOT NULL        
        )
    '''
    )
    print(f'{db_name} was created successfully.')
    connect.close()

else:
     print('this database already exists, check the name or another parameters.')


# ###### insercao de dados teste

# db_name = r'C:\Users\mary saotome\Documents\database\financial.db'
# connect = sqlite3.connect(db_name)
# cursor = connect.cursor()

# data = [
#     ('SHEIN', 'PIX', '131.00', '2025-01-19', 'Despesa'),
#     ('Shoppee', 'PIX', '230.00', '2025-01-19', 'Despesa'),
#     ('Comida', 'VR/VA', '13.99', '2025-01-220', 'Despesa'),
#     ('Salário', 'Débito', '1250.00', '2025-01-20', 'Receita'),
#     ('Itaú', 'Crédito', '462.00', '2025-01-19', 'Despesa'),
#     ('Nubank', 'Crédito', '260.00', '2025-01-19', 'Despesa')
# ]

# cursor.executemany(''' 
#             INSERT INTO flow (origem, metodo, valor, data, tipo) VALUES (?, ?, ?, ?, ?)
#                    ''', data)

# connect.commit()
# connect.close()
