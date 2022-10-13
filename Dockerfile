FROM python:3.9-slim
RUN mkdir /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY orders/ /app
WORKDIR /app
CMD ["gunicorn", "orders.wsgi:application", "--bind", "0:8000"]