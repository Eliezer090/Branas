import inject
import json
from flask import Blueprint, jsonify, Response, request
from src.domain.actions.pedido.get_pedidos import GetPedido
from src.domain.actions.pedido.post_pedido import PostPedido
from src.domain.interfaces.pedido.pedido import Pedido


@inject.autoparams()
def pedidos(get_pedido: GetPedido, post_pedidos: PostPedido) -> Blueprint:
    pedidos_blueprint = Blueprint('pedidos', __name__)

    @pedidos_blueprint.route('/get_pedidos', methods=['GET'])
    def get_pedidos() -> Response:
        pedidos = get_pedido.execute()
        return jsonify({
            'pedidos': pedidos
        })

    @pedidos_blueprint.route('/post_pedido', methods=['POST'])
    def post_pedido() -> Response:
        """
            Pega o conteudo do argumento book que veio junto na URL
        """
        #book = request.args.get('book')
        """ 
            Pega o conteudo do body do request, deve vir no type json
        """
        request_data = request.get_json()
        # print(request_data)
        if (request_data is not None) and (type(request_data) is not dict):
            request_data = json.loads(request_data)
        #j = json.loads(book)
        pedido_obj: Pedido = None
        try:
            pedido_obj = Pedido(**request_data)
        except TypeError as err:
            print(err)
        print('pedido_obj', pedido_obj)
        pedidos = post_pedidos.execute(pedido_obj)

        # print(pedido_obj)
        # books_db.append(pedido_obj)

        # if book is not None:
        #    json_object = json.loads(book)  # Converte o string em json object
        # books_db.append(json_object)

        # if request_data is not None:
        #    books_db.append(request_data)
       # books_db = ''
        return jsonify({
            'pedidos': pedidos
        })
    return pedidos_blueprint
