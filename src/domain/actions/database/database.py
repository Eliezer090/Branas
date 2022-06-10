from typing import List
import inject
from src.domain.interfaces.database import DatabaseInterface
from src.domain.interfaces.pedido.pedido import Pedido


class DatabaseActions:
    @inject.autoparams()
    def get_pedidos(self, database: DatabaseInterface) -> List[Pedido]:
        print("GetPedidoDATABASE_action")
        return database.get_pedidos(self)

    @inject.autoparams()
    def get_next_id(self, database: DatabaseInterface) -> int:
        return database.get_next_id(self)
