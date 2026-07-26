import pytest
from pydantic import ValidationError

from app.api.models.schemas import ProdutoCreate


def test_should_create_produto_weth_validade_data():
    # Arrange:
    dados = {
        "nome": "Produto do mini mercado",
        "preco_base": 25.9
    }
    # Act:
    prod_1 = ProdutoCreate(**dados)
    # Assert:
    assert prod_1.nome == 'Produto do mini mercado'
    assert prod_1.preco_base == 25.9


def test_should_reject_produto_with_invalid_name_type():
    with pytest.raises(ValidationError):
        # Arrange:
        dados = {
            "nome": 3213,
            "preco_base": 25.9
        }
        ProdutoCreate(**dados)


def test_should_reject_produto_with_price_base_value_type_not_valid():
    with pytest.raises(ValidationError) as exc_info:
        dados = {
            "nome": "Validador",
            "preco_base": None
        }
        ProdutoCreate(**dados)  # type: ignore

    # Você pode inspecionar os detalhes do erro
    erros = exc_info.value.errors()
    assert erros[0]["loc"] == ("preco_base",)
    assert "float_type" in erros[0]["type"]


def test_should_reject_produto_with_price_base_float_parsing():
    with pytest.raises(ValidationError) as exc_info:
        dados = {
            "nome": "Validador",
            "preco_base": "Validador"
        }
        ProdutoCreate(**dados)  # type: ignore

    # Você pode inspecionar os detalhes do erro
    erros = exc_info.value.errors()
    assert erros[0]["loc"] == ("preco_base",)
    assert "float_parsing" in erros[0]["type"]
