FROM python:3.8-alpine
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt
COPY app /code/app
EXPOSE 8000
COPY entrypoint.sh /code
RUN chmod +x ./entrypoint.sh
COPY settings.cfg /code
ENTRYPOINT ["sh", "entrypoint.sh"]
