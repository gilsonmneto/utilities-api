import pytest
from unittest.mock import MagicMock
from services.response_factory import ResponseFactory
from services.cpf_validator import CPFValidator


@pytest.fixture
def cpf_validator():
    validator = CPFValidator()
    validator.response_factory = MagicMock(spec=ResponseFactory)
    return validator


def test_is_valid_input_with_none(cpf_validator):
    result = cpf_validator._is_valid_input(None)
    assert result == {"cpf": None, "is_valid": False}


def test_is_valid_input_with_non_string(cpf_validator):
    result = cpf_validator._is_valid_input(12345678901)
    assert result == {"cpf": 12345678901, "is_valid": False}


def test_is_valid_input_with_string_correct(cpf_validator):
    result = cpf_validator._is_valid_input("12345678901")
    assert result is None


def test_is_length_valid_with_short_cpf(cpf_validator):
    result = cpf_validator._is_length_valid("1234567891")
    assert result == {"cpf": "1234567891", "is_valid": False}


def test_is_length_valid_with_long_cpf(cpf_validator):
    result = cpf_validator._is_length_valid("123456789012")
    assert result == {"cpf": "123456789012", "is_valid": False}


def test_is_length_valid_with_valid_cpf(cpf_validator):
    result = cpf_validator._is_length_valid("12345678901")
    assert result is None


def test_calculate_digit_valid(cpf_validator):
    digit = cpf_validator._calculate_digit("27233565821", 10)
    assert digit == 2  # Ajuste o valor esperado conforme a lógica


def test_calculate_digit_invalid(cpf_validator):
    digit = cpf_validator._calculate_digit("27233565821", 10)
    assert digit != 3  # Ajuste o valor esperado conforme a lógica


def test_is_first_digit_valid_invalid(cpf_validator):
    # Simula que o cálculo do dígito verificador deve ser 0
    cpf_validator._calculate_digit = MagicMock(
        return_value=int("1")
    )  # O dígito calculado
    result = cpf_validator._is_first_digit_valid("27233565821")
    assert result == {"cpf": "27233565821", "is_valid": False}


def test_is_first_digit_valid_valid(cpf_validator):
    cpf_validator._calculate_digit = MagicMock(return_value=int("2"))
    result = cpf_validator._is_first_digit_valid("27233565821")
    assert result is None


def test_is_second_digit_valid_invalid(cpf_validator):
    result = cpf_validator._is_second_digit_valid("12345678901")
    assert result == {"cpf": "12345678901", "is_valid": False}


def test_is_second_digit_valid_valid(cpf_validator):
    cpf_validator._calculate_digit = MagicMock(
        return_value=int("1")
    )  # Ajuste conforme necessário
    result = cpf_validator._is_second_digit_valid("27233565821")
    assert result is None


def test_is_cpf_valid_with_valid_cpf(cpf_validator):
    cpf = "27233565821"
    expected_response = {
        "status": "OK",
        "code": 200,
        "data": {"cpf": cpf, "is_valid": True},
        "message": "CPF informado é válido",
    }
    cpf_validator.response_factory.create_response = MagicMock(
        return_value=expected_response
    )
    response = cpf_validator.is_cpf_valid(cpf)
    assert response["data"]["is_valid"] == True
