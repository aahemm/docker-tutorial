FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

COPY . /code/
ENTRYPOINT ["/bin/bash", "start.sh"]
