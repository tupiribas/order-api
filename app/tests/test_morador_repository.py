# import pytest

from app.api.models.schemas import MoradorCreate
from app.api.repositories.morador_repositories import (
    MoradorRepositoryEmMemoria)


def test_should_save_resident_and_assign_id():
    # Arrange
    dados1 = {
        "condominio_id": 1,
        "pessoa_id": 1,
        "unidade": '01-0001'
    }
    dados2 = {
        "condominio_id": 2,
        "pessoa_id": 2,
        "unidade": '01-0201'
    }

    # Act
    repo = MoradorRepositoryEmMemoria()
    mora1 = MoradorCreate(**dados1)
    mora2 = MoradorCreate(**dados2)
    resultado1 = repo.salvar(mora1)
    resultado2 = repo.salvar(mora2)

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
        "condominio_id": 1,
        "pessoa_id": 1,
        "unidade": '01-0001'
    }

    # Act
    repo = MoradorRepositoryEmMemoria()
    mora1 = MoradorCreate(**dados1)

    _ = repo.salvar(mora1)

    resultado_busca_por_id_errado = repo.buscar_por_id(99)
    resultado_busca_por_id = repo.buscar_por_id(1)
    # Assert
    # Valida retorna vazio (não encontrado)]
    assert resultado_busca_por_id_errado == {}

    # Valida se o dado encontrado com base no id, retorava o dado salvo no repo
    assert resultado_busca_por_id == repo.dados[1]
