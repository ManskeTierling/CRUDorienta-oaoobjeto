from flask import request

class Produto():
    def __init__(self, nome, descricao, marca, preco, cor, id= None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.marca = marca
        self.preco = preco
        self.cor = cor






