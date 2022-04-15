FROM python:3.10.4

RUN mkdir /home/test
WORKDIR /home/test

COPY . .

RUN pip install -r ./requirement.txt

ENV APP_ENV production

CMD python3 ./test.py
