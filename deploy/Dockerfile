FROM python:3.8

ENV DOCKERIZE_VERSION v0.6.1

RUN apt-get update && apt-get install -y wget \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && apt-get install postgresql gcc python3-dev musl-dev -y

WORKDIR /app/

COPY deploy/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY --chown=www-data:www-data deploy/scripts/* /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
