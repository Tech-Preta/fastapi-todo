# Estágio de construção
FROM cgr.dev/chainguard/python:latest AS builder

# Definir o diretório de trabalho
COPY . /app

RUN /bin/bash -c "pip install -r requirements.txt --user"

# Copiar os arquivos do projeto
COPY ./main.py /src/main.py

# Estágio de produção
FROM cgr.dev/chainguard/python:latest

# Copiar apenas os pacotes necessários do estágio de construção
COPY --from=builder /root/.local /root/.local

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o código do projeto
COPY --from=builder /src/main.py /app/main.py

# Definir a variável de ambiente para garantir que os pacotes Python sejam vistos pelo Python
ENV PATH=/root/.local/bin:$PATH

# Comando para executar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]