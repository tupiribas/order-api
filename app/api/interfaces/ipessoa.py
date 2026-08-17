from abc import ABC, abstractmethod

from app.api.models.schemas import PessoaCreate


class IPessoaRepository(ABC):
    @abstractmethod
    def salvar(self, dados: PessoaCreate) -> dict:
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> dict:
        pass
