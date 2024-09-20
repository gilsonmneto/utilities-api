from flask import Flask, request, jsonify
from services.cpf_validator import CPFValidator
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template_file="docs/swagger.yml")


@app.get("/")
def index():
    return (
        jsonify(
            {
                "status": 200,
                "MENSAGEM": "Operando normalmente.",
                "NOME": "UTILITIES API",
                "APLICACAO": "BACKEND",
                "AMBIENTE": "DESENVOLVIMENTO",
            }
        ),
        200,
    )


@app.route("/validate/cpf", methods=["POST"])
def validate_cpf():
    data = request.json
    cpf = data.get("cpf")

    validade_cpf = CPFValidator()
    result = validade_cpf.is_cpf_valid(cpf)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
