# syntax=docker/dockerfile:experimental
# BASE
FROM python:3.7.9-slim AS base

WORKDIR /home/root

# # In case DB access is required
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y gnupg2 curl \
#    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
#    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
#    && ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17 \
    && apt-get clean 


# Set timezone in container
ENV TZ=Europe/Berlin
# Disable command prompt interaction
ENV DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && apt-get install -y tzdata \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && apt-get clean

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# source poetry
# https://stackoverflow.com/questions/59895745/poetry-fails-to-install-in-docker
ENV PATH = "${PATH}:/root/.poetry/bin"

# create app path & add python path for shell execution
WORKDIR /home/root/app
ENV PYTHONPATH=/home/root/app


# IDE stage with pyproject.toml and optional .lock file
FROM base AS ide

# add git and auto-complete
RUN apt-get install -y git \
    && apt-get clean \
    && bash -c "curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash"; \
    /bin/bash -c "echo 'source ~/.git-completion.bash' >> ~/.bashrc"

# install code-server
RUN curl -fOL https://github.com/cdr/code-server/releases/download/v3.10.2/code-server_3.10.2_amd64.deb; \
    dpkg -i code-server_3.10.2_amd64.deb \
    && rm code-server_3.10.2_amd64.deb

# install code-server extensions
RUN code-server --install-extension ms-python.python \
    code-server --install-extension mhutchie.git-graph \
    code-server --install-extension njpwerner.autodocstring \
    code-server --install-extension mutantdino.resourcemonitor \
    code-server --install-extension streetsidesoftware.code-spell-checker \
    code-server --install-extension oderwat.indent-rainbow \
    code-server --install-extension redhat.vscode-yaml


# COPY poetry.toml and optional .lock file
COPY pyproject.toml poetry.lock* ./
# install poetry
RUN poetry install \
    && rm -rf ~/.cache/pypoetry/{cache,artifacts} \
    && rm pyproject.toml poetry.lock

