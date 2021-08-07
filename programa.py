import mysql.connector


def conexao():
    db = mysql.connector.connect(
        host='localhost',
        database='cadastro',
        user='root',
        password='Blumenau1'
        )
    return db

def salvar(db, novo_produto):
    comando_sql = 'INSERT INTO PRODUTOS (NOME, DESCRICAO, MARCA, PRECO, COR) VALUES (%s, %s, %s, %s, %s)'
    parametros = (novo_produto.nome,novo_produto.descricao, novo_produto.marca, novo_produto.preco, novo_produto.cor)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)

def select(db):
    comando_sql = 'SELECT * FROM produtos'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        resultado = cursor.fetchall()
        # for registro in resultado:
        #     print(f'id: {registro[0]}, nome: {registro[1]}, sobrenome: {registro[2]}',
        #     f'cpf: {registro[3]}, email: {registro[4]}, telefone: {registro[5]}')
        cursor.close()
        return resultado
    except Exception as error:
        print(error)

def delete(db, id_registro):
    comando_sql = f'DELETE FROM PRODUTOS WHERE ID = {id_registro}'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)

def select_id(db, id_registro):
    comando_sql = f'SELECT * FROM produtos WHERE id = {id_registro}'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    except Exception as error:
        print(error)

def update(db, novo_produto):
    comando_sql = "UPDATE PRODUTOS SET NOME = %s, DESCRICAO = %s, MARCA = %s, PRECO = %s, COR = %s"
    parametros = (novo_produto.nome,novo_produto.descricao, novo_produto.marca, novo_produto.preco, novo_produto.cor)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)





