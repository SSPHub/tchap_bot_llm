FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Install project dependencies
COPY pyproject.toml .
RUN uv sync

COPY . .

CMD ["uv", "run", "main.py"]