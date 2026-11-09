FROM python:3.12-slim

# Installation uv depuis l'image officielle ou via pip
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Création d'un utilisateur non-root pour la sécurité
RUN useradd -m -u 1000 safebank && \ 
    mkdir -p   /app && \
    chown -R safebank:safebank /app

WORKDIR /app

# Changer d'utilisateur
USER safebank

# Copier les fichiers de configuration des dépendances
COPY --chown=safebank:safebank pyproject.toml uv.lock ./

# Installer les dépendances de production sans environnement virtuel système (ou avec uv dans /app/.venv)
RUN uv sync --frozen --no-dev --no-install-project

# Copier le reste du code source
COPY --chown=safebank:safebank . .

# Installer le projet lui-même dans l'environnement
RUN uv sync --frozen --no-dev


# Exposer le port de l'API
EXPOSE 8000

# Lancer l'application avec uvicorn
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]