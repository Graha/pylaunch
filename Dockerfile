FROM python:3.6
ADD . /src
WORKDIR /src
RUN pip install -r requirments.txt
EXPOSE 8080
CMD ./start.sh

