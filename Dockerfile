FROM python:3.13-alpine

LABEL org.opencontainers.image.source="https://github.com/smashedr/py-test-action"
LABEL org.opencontainers.image.description="Python Test Action"
LABEL org.opencontainers.image.authors="smashedr"

COPY requirements.txt /
# hadolint ignore=DL3013,DL3042
RUN python -m pip install -Ur requirements.txt

COPY src /src
ENTRYPOINT ["python", "/src/main.py"]
