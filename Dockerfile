FROM python:3.11.4
WORKDIR /Users/homebase/Desktop/HNG12/Python/Stage-1
COPY . /Users/homebase/Desktop/HNG12/Python/Stage-1/
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./Number-API.py