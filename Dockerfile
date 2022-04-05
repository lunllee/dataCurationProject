FROM python:3.10.4

RUN mkdir /home/test
RUN mkdir /home/test/data
RUN mkdir /home/test/data/8fd2d3e0-352a-11ec-8bab-6194bb3a1754
RUN mkdir /home/test/data/8fd2d3e0-352a-11ec-8bab-6194bb3a1754/cf1fbe80-352c-11ec-8bab-6194bb3a1754

COPY ./requirement.txt /home/test
COPY ./test.py /home/test
COPY ./data/8fd2d3e0-352a-11ec-8bab-6194bb3a1754/cf1fbe80-352c-11ec-8bab-6194bb3a1754/covid.csv /home/test/data/8fd2d3e0-352a-11ec-8bab-6194bb3a1754/cf1fbe80-352c-11ec-8bab-6194bb3a1754

WORKDIR /home/test
RUN pip install -r ./requirement.txt

CMD python3 ./test.py
