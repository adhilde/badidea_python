FROM python:3.7-stretch

# Run all commands as `root` user
USER root

# Install dependencies
RUN apt-get update \
    && apt-get -y install vim

ADD ./payload /app
WORKDIR /app

# Setup Timezone
ENV TZ=America/Denver

# Install python requirements and run the root app file
RUN pip install -r requirements.txt

# Cache dir needs to exist
RUN mkdir /app/cache

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 app

