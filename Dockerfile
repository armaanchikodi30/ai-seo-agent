FROM python:3.12-slim

# System deps (lxml/bs4 build needs these; curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Grab the uv binary directly from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Never let uv download its own Python — always use the base image's
# system interpreter (python3.11 from the FROM line above).
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_PYTHON_PREFERENCE=only-system

# Create the non-root user and app dir FIRST, then do everything as that user.
# This avoids any root-owned .venv that later needs chown'ing.
RUN useradd -m appuser
WORKDIR /app
RUN chown appuser:appuser /app
USER appuser

# Copy dependency manifests first (better layer caching), owned by appuser
COPY --chown=appuser:appuser pyproject.toml uv.lock ./

# Build the venv as appuser, against the system Python -> no permission mismatch possible
RUN uv sync --frozen --no-install-project --no-dev

# Copy application code, also owned by appuser
COPY --chown=appuser:appuser . .

# Put the project venv on PATH
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["uv", "run", "--frozen", "streamlit", "run", "app.py", \
    "--server.port=8501", \
    "--server.address=0.0.0.0", \
    "--server.headless=true", \
    "--browser.gatherUsageStats=false"]
