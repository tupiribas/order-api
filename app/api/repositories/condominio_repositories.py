from app.api.interfaces.icondominio import ICondominioRepository
from app.api.models.schemas import CondominioCreate


class CondominioRepositoryEmMemoria(ICondominioRepository):
    def __init__(self) -> None:
        self.dados = {}
        self._proximo_id = 1

    def salvar(self, dados: CondominioCreate) -> dict:
        '''
        Salvar o dado do condomínio em memória incrementando o id fora do
        dicionário e retornando o dado recém criado
        '''
        novo_id = self._proximo_id
        novo_dado_condominio = {"id": novo_id, **dados.model_dump()}
        self._proximo_id += 1
        self.dados[novo_id] = novo_dado_condominio
        return novo_dado_condominio
