from app.api.interfaces.iproduto import IProdutoRepository
from app.api.models.schemas import ProdutoCreate


class ProdutoRepositoryEmMemoria(IProdutoRepository):
    def __init__(self) -> None:
        self.dados = {}
        self._proximo_id = 1

    def salvar(self, dados: ProdutoCreate) -> dict:
        '''
        Salvar o dado do produto em memória incrementando o id fora do
        dicionário e retornando o dado recém criado
        '''
        novo_id = self._proximo_id
        novo_dado_produto = {"id": novo_id, **dados.model_dump()}
        self._proximo_id += 1
        self.dados[novo_id] = novo_dado_produto
        return novo_dado_produto

    def buscar_por_id(self, id: int) -> dict:
        '''
        Retorna o dado com base no id passado por parâmetro
        '''
        if id not in self.dados:
            return {}
        return self.dados[id]
