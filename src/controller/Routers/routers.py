from flask_restx import Api, Resource
from flask import Flask
from controller.Server.instance import Server
from controller.Pedido import pedido


app, api = Server.app, Server.api

books_db = [
    {'id': 0, 'title': 'War and peace'},
    {'id': 1, 'title': 'Clean code'},
    {'id': 2, 'title': 'Clean Arquitecture'},
]

print('aqui')


@api.route('/pedido')
class Pedido(Resource):
    print('PEDIDO')
    """
    Aqui deverão ser criados metodos com o mesmo nome de HTTP:
    get,post,put,delete
    """

    def get(self,):
        print('GET')
        Pedido.getPedidos(self)
        # Aqui iria fazer request para bd para pegar os dados
        return books_db
