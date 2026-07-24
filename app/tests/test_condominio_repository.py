# import pytest

from app.api.models.schemas import CondominioCreate
from app.api.repositories.condominio_repositories import (
    CondominioRepositoryEmMemoria)


def test_should_save_condominio_and_assign_id():
    # Arrange
    dados1 = {
        "nome": 'Teste Condomínio',
        "endereco": "Rua dos testes plenos, 345, Bairro Da Hora"
    }
    dados2 = {
        "nome": 'Teste Condomínio',
        "endereco": "Rua dos testes plenos, 345, Bairro Da Hora"
    }

    # Act
    repo = CondominioRepositoryEmMemoria()
    cond1 = CondominioCreate(**dados1)
    cond2 = CondominioCreate(**dados2)
    resultado1 = repo.salvar(cond1)
    resultado2 = repo.salvar(cond2)

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
        "nome": 'Teste Condomínio',
        "endereco": "Rua dos testes plenos, 345, Bairro Da Hora"
    }

    # Act
    repo = CondominioRepositoryEmMemoria()
    cond1 = CondominioCreate(**dados1)

    _ = repo.salvar(cond1)

    resultado_busca_por_id_errado = repo.buscar_por_id(99)
    resultado_busca_por_id = repo.buscar_por_id(1)
    # Assert
    # Valida retorna vazio (não encontrado)]
    assert resultado_busca_por_id_errado == {}

    # Valida se o dado encontrado com base no id, retorava o dado salvo no repo
    assert resultado_busca_por_id == repo.dados[1]
