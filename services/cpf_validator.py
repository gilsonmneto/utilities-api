import re
from services.response_factory import ResponseFactory


class CPFValidator:

    def __init__(self):
        self.response_factory = ResponseFactory()

    def is_cpf_valid(self, cpf):
        """Valida o CPF"""

        data = self._is_valid_input(cpf)
        if data:
            return self.response_factory.create_response(
                "OK", 200, data, "CPF string inválida"
            )

        cpf = self._sanitize_cpf(cpf)

        data = self._is_length_valid(cpf)
        if data:
            return self.response_factory.create_response(
                "OK", 200, data, "CPF não tem 11 dígitos"
            )

        data = self._is_first_digit_valid(cpf)
        if data:
            return self.response_factory.create_response(
                "OK", 200, data, "Dígito verificador inválido"
            )

        data = self._is_second_digit_valid(cpf)
        if data:
            return self.response_factory.create_response(
                "OK", 200, data, "Dígito verificador inválido"
            )

        data = {"cpf": cpf, "is_valid": True}
        return self.response_factory.create_response(
            "OK", 200, data, "CPF informado é válido"
        )

    def _is_valid_input(self, cpf):
        if not cpf or not isinstance(cpf, str):
            return {"cpf": cpf, "is_valid": False}
        return None

    def _sanitize_cpf(self, cpf):
        return re.sub(r"[\D]", "", cpf)

    def _is_length_valid(self, cpf):
        if len(cpf) != 11:
            return {"cpf": cpf, "is_valid": False}
        return None

    def _calculate_digit(self, cpf, factor):
        total = sum(int(cpf[i]) * (factor - i) for i in range(factor - 1))
        remainder = (total * 10) % 11
        return 0 if remainder == 10 else remainder

    def _is_first_digit_valid(self, cpf):
        if int(cpf[9]) != self._calculate_digit(cpf, 10):
            return {"cpf": cpf, "is_valid": False}
        return None

    def _is_second_digit_valid(self, cpf):
        if int(cpf[10]) != self._calculate_digit(cpf, 11):
            return {"cpf": cpf, "is_valid": False}
        return None
