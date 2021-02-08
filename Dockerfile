FROM python:3.8.7-buster

WORKDIR /docker_unittest

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /docker_unittest


#CMD ["python", "test.py"]

CMD ["python", "prime_numbers.py"]