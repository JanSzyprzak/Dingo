FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"]
EXPOSE 8000 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
