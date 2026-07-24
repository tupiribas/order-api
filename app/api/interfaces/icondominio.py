from abc import ABC, abstractmethod

from app.api.models.schemas import CondominioCreate


class ICondominioRepository(ABC):
    @abstractmethod
    def salvar(self, dados: CondominioCreate) -> dict:
        pass
