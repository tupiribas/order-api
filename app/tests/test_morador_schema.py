import pytest
from pydantic import ValidationError

from app.api.models.schemas import MoradorCreate  # type: ignore


def test_should_create_morador_with_valid_data():
    # Arrange:
    dados = {
        "condominio_id": 1,
        "pessoa_id": 1,
        "unidade": "A/0001"
    }
    # Act:
    morador_1 = MoradorCreate(**dados)
    # Assert:
    assert morador_1.condominio_id == 1
    assert morador_1.pessoa_id == 1
    assert morador_1.unidade == "A/0001"


def test_rejects_condo_resident_and_person_is_int_from_float():
    with pytest.raises(ValidationError) as exc_info:
        # Arrange:
        dados = {
            "condominio_id": 1.1,
            "pessoa_id": 1.1,
            "unidade": "A/0001"
        }
        # Act
        MoradorCreate(**dados)  # type: ignore

    # Inspecionando os detalhes do erro
    # Assert
    erros = exc_info.value.errors()
    assert erros[0]["loc"] == ("condominio_id",)
    assert "int_from_float" in erros[0]["type"]
    assert erros[1]["loc"] == ("pessoa_id",)
    assert "int_from_float" in erros[1]["type"]


def test_rejects_condo_resident_and_person_is_int_parsing():
    with pytest.raises(ValidationError) as exc_info:
        # Arrange:
        dados = {
            "condominio_id": "um",
            "pessoa_id": "um",
            "unidade": "A/0001"
        }
        # Act
        MoradorCreate(**dados)  # type: ignore

    # Inspecionando os detalhes do erro
    # Assert
    erros = exc_info.value.errors()
    assert erros[0]["loc"] == ("condominio_id",)
    assert "int_parsing" in erros[0]["type"]
    assert erros[1]["loc"] == ("pessoa_id",)
    assert "int_parsing" in erros[1]["type"]


def test_rejects_condo_resident_and_person_is_int_type():
    with pytest.raises(ValidationError) as exc_info:
        # Arrange:
        dados = {
            "condominio_id": None,
            "pessoa_id": None,
            "unidade": "A/0001"
        }
        # Act
        MoradorCreate(**dados)  # type: ignore

    # Inspecionando os detalhes do erro
    # Assert
    erros = exc_info.value.errors()
    assert erros[0]["loc"] == ("condominio_id",)
    assert "int_type" in erros[0]["type"]
    assert erros[1]["loc"] == ("pessoa_id",)
    assert "int_type" in erros[1]["type"]
