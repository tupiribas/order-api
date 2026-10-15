from abc import ABC, abstractmethod

from app.api.models.schemas import MoradorCreate


class IMoradorRepository(ABC):
    @abstractmethod
    def salvar(self, dados: MoradorCreate) -> dict:
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> dict:
        pass
