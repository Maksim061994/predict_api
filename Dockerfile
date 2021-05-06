FROM python:3.6
MAINTAINER Maxim Kulagin 'maksimkulagin06@yandex.ru'

# Setting workaround
COPY api/ /app/api
WORKDIR /app

# Install libs
RUN pip install -r api/requirements.txt

# Start app
ENTRYPOINT ["python3.6"]
CMD ["./api/app.py"]
