
from controller.Server.instance import Server
from controller.Routers.routers import Routers

if __name__ == '__main__':
    print('Iniciando aplicação')
    server = Server()
    server.run()
