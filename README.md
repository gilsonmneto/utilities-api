# Utilities - API

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte software instalado em seu computador:

- [Python](https://www.python.org/)
- [Git](https://git-scm.com/)

## Instalação

1. Clone o repositório para o seu computador local:

   ```bash
   git clone https://github.com/agu-pgu/utilities-api.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd utilities-api
   ```

3. Crie o ambiente virtual: [^1]

   ```bash
   python3 -m venv utilities-api/venv/
   ```

4. Ative o ambiente virtual

   - Linux

   ```bash
   source venv/bin/activate
   ```

   - Windows

   ```bash
   utilities-api\venv\Scripts\activate
   ```

5. Instalar as dependências do projeto:

   ```bash
   pip3 install -r requirements.txt
   ```

## Executando o Projeto

1. Para iniciar o servidor `Flask` de desenvolvimento execute:

   ```bash
   python app.py
   ```

2. Uma mensagem será exibida no terminal, contendo o endereço e porta do servidor:

   ```bash
   http://localhost:5000
   ```
