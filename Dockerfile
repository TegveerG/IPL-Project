FROM python:3.9-slim
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn main:app