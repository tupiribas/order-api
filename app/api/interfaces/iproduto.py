from abc import ABC, abstractmethod

from app.api.models.schemas import ProdutoCreate


class IProdutoRepository(ABC):
    @abstractmethod
    def salvar(self, dados: ProdutoCreate) -> dict:
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> dict:
        pass
