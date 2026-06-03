# 3.13-slim has vulnerabilities according to Docker
FROM python:3.13-alpine

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Build deps for python-olm (libolm is compiled from source)
RUN apk add --no-cache \
    build-base \
    cmake \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# Install project dependencies
COPY pyproject.toml .
RUN uv sync

COPY . .

CMD ["uv", "run", "main.py"]
