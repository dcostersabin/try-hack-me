FROM python:3.13-alpine  AS base

ENV	PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN apk update

FROM base AS requirements

RUN apk add poetry;

RUN pip install poetry-plugin-export 

RUN poetry self add poetry-plugin-export 

WORKDIR /opt/app

COPY poetry.lock pyproject.toml .

RUN poetry export -f requirements.txt --without-hashes --output requirements.txt ;

FROM base AS installer

WORKDIR /opt/app

COPY --from=requirements /opt/app/requirements.txt .

RUN mkdir -p /install ;

RUN pip3 --no-cache-dir install --target=/install -r requirements.txt ;

FROM python:3.13-alpine AS runner

RUN apk update 

RUN apk add docker 

WORKDIR /opt/app

COPY --from=installer /install/ /usr/local/lib/python3.13/site-packages/

COPY src/ .

COPY docker/entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

