# Dockerfile

# 1. Estágio de Build: Instala dependências

FROM python:3.9-slim AS builder

WORKDIR /install

# Copia apenas o requirements.txt primeiro para aproveitar o cache do Docker

COPY app/requirements.txt .

# Instala as dependências em um diretório separado

RUN pip install --user --no-cache-dir -r requirements.txt

# 2. Estágio Final: Copia dependências e código da aplicação

FROM python:3.9-slim

WORKDIR /app

# Copia as dependências instaladas do estágio 'builder'

COPY --from=builder /root/.local /root/.local

# Copia o código da aplicação

COPY app/ .

# Adiciona o diretório de binários das dependências ao PATH

ENV PATH=/root/.local/bin:$PATH

# Garante que o output do Python não seja bufferizado (útil para logs)

ENV PYTHONUNBUFFERED=1

# Expõe a porta que a aplicação usa

EXPOSE 8080

# Comando para rodar a aplicação quando o container iniciar

CMD ["python", "app.py"]
