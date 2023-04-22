FROM ubuntu:latest
LABEL authors="maidanets"

ENTRYPOINT ["top", "-b"]