import pytest
from pydantic import ValidationError

from app.api.models.schemas import PessoaCreate


def test_should_create_pessoa_weth_validade_data():
    # Arrange:
    dados = {
        "nome": "Francisco de almeida coutinho do teste",
    }
    # Act:
    pessoa_1 = PessoaCreate(**dados)
    # Assert:
    assert pessoa_1.nome == 'Francisco de almeida coutinho do teste'


def test_should_reject_pessoa_with_invalid_name_type():
    with pytest.raises(ValidationError):
        # Arrange:
        dados = {
            "nome": 1234,
        }
        PessoaCreate(**dados)  # type: ignore
