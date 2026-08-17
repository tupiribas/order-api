# import pytest

from app.api.models.schemas import ProdutoCreate
from app.api.repositories.produto_repositories import (
    ProdutoRepositoryEmMemoria)


def test_should_save_produto_and_assign_id():
    # Arrange
    dados1 = {
        "nome": 'Teste Produto 1',
        "preco_base": 65.69
    }
    dados2 = {
        "nome": 'Teste Produto 2',
        "preco_base": 24.22
    }

    # Act
    repo = ProdutoRepositoryEmMemoria()
    prod1 = ProdutoCreate(**dados1)
    prod2 = ProdutoCreate(**dados2)
    resultado1 = repo.salvar(prod1)
    resultado2 = repo.salvar(prod2)

    # Assert
    # Validando se os dados foram salvos
    assert resultado1 == repo.dados[1]
    assert resultado2 == repo.dados[2]
    # Validar se os dados foram devidamente slvos, validando pelo ids
    assert resultado1["id"] == 1
    assert resultado2["id"] == 2


def test_should_find_by_id():
    # Arrange
    dados1 = {
        "nome": 'Teste Produto 1',
        "preco_base": 65.69
    }

    # Act
    repo = ProdutoRepositoryEmMemoria()
    prod1 = ProdutoCreate(**dados1)

    _ = repo.salvar(prod1)

    resultado_busca_por_id_errado = repo.buscar_por_id(99)
    resultado_busca_por_id = repo.buscar_por_id(1)
    # Assert
    # Valida retorna vazio (não encontrado)]
    assert resultado_busca_por_id_errado == {}

    # Valida se o dado encontrado com base no id, retorava o dado salvo no repo
    assert resultado_busca_por_id == repo.dados[1]
