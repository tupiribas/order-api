# import pytest
from app.api.models.schemas import PessoaCreate
from app.api.repositories.pessoa_repositories import (
    PessoaRepositoryEmMemoria)


def test_should_save_pessoa_and_assign_id():
    # Arrange
    dados1 = {
        "nome": 'Francisco de almeida coutinho do teste Dois',
    }
    dados2 = {
        "nome": 'Francisco de almeida coutinho do teste Dois',
    }

    # Act
    repo = PessoaRepositoryEmMemoria()
    pessoa1 = PessoaCreate(**dados1)
    pessoa2 = PessoaCreate(**dados2)
    resultado1 = repo.salvar(pessoa1)
    resultado2 = repo.salvar(pessoa2)

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
        "nome": 'Francisco de almeida coutinho do teste Dois',
    }

    # Act
    repo = PessoaRepositoryEmMemoria()
    prod1 = PessoaCreate(**dados1)

    _ = repo.salvar(prod1)

    resultado_busca_por_id_errado = repo.buscar_por_id(99)
    resultado_busca_por_id = repo.buscar_por_id(1)
    # Assert
    # Valida retorna vazio (não encontrado)]
    assert resultado_busca_por_id_errado == {}

    # Valida se o dado encontrado com base no id, retorava o dado salvo no repo
    assert resultado_busca_por_id == repo.dados[1]
