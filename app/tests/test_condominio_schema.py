import pytest
from pydantic import ValidationError

from app.api.models.schemas import CondominioCreate


def test_should_create_condominio_weth_validade_data():
    # Arrange:
    dados = {
        "nome": "Condominio teste",
        "endereco": "Rua dos testes plenos, 345, Bairro Da Hora"
    }
    # Act:
    condo_1 = CondominioCreate(**dados)
    # Assert:
    assert condo_1.nome == 'Condominio teste'
    assert condo_1.endereco == 'Rua dos testes plenos, 345, Bairro Da Hora'


def test_should_reject_condominio_with_invalid_name_type():
    with pytest.raises(ValidationError):
        # Arrange:
        dados = {
            "nome": 1234,
            "endereco": "Rua dos testes plenos, 345, Bairro Da Hora"
        }
        CondominioCreate(**dados)
