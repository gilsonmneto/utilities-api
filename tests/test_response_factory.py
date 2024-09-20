import pytest
from services.response_factory import (
    ResponseFactory,
)  # Altere para o nome correto do módulo


# Fixture para criar uma instância da classe ResponseFactory
@pytest.fixture
def response_factory():
    return ResponseFactory()


# Teste para verificar se a resposta é criada corretamente com valores normais
def test_create_response_normal(response_factory):
    status = "success"
    code = 200
    data = {"user": "Alice"}
    message = "Request completed successfully"

    expected_response = {
        "status": status,
        "code": code,
        "data": data,
        "message": message,
    }

    response = response_factory.create_response(status, code, data, message)
    assert response == expected_response


# Teste para verificar se a resposta é criada corretamente com status de erro
def test_create_response_error(response_factory):
    status = "error"
    code = 404
    data = None
    message = "Resource not found"

    expected_response = {
        "status": status,
        "code": code,
        "data": data,
        "message": message,
    }

    response = response_factory.create_response(status, code, data, message)
    assert response == expected_response


# Teste para verificar se a resposta é criada corretamente com valores vazios
def test_create_response_empty(response_factory):
    status = ""
    code = 0
    data = {}
    message = ""

    expected_response = {
        "status": status,
        "code": code,
        "data": data,
        "message": message,
    }

    response = response_factory.create_response(status, code, data, message)
    assert response == expected_response


# Teste para verificar se a resposta é criada corretamente com tipos mistos de dados
def test_create_response_mixed_data(response_factory):
    status = "partial"
    code = 206
    data = [1, 2, 3]
    message = "Partial content"

    expected_response = {
        "status": status,
        "code": code,
        "data": data,
        "message": message,
    }

    response = response_factory.create_response(status, code, data, message)
    assert response == expected_response
