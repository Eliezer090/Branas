


books_db = [
    {'id': 0, 'title': 'War and peace'},
    {'id': 1, 'title': 'Clean code'},
    {'id': 2, 'title': 'Clean Arquitecture'},
]


class Pedido():
    """
    Aqui deverão ser criados metodos com o mesmo nome de HTTP:
    get,post,put,delete
    """

    def getPedidos(self,):
        print('GET')
        # Aqui iria fazer request para bd para pegar os dados
        return books_db