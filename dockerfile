FROM python:3.13-alpine  # 3.13-slim has vulnerabilities according to Docker

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Build deps for python-olm (libolm is compiled from source)
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential cmake \
&& rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY pyproject.toml .
RUN uv sync

COPY . .

CMD ["uv", "run", "main.py"]
