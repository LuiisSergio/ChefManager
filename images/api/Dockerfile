FROM python:3.9
WORKDIR /usr/src/app
COPY requeriments.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requeriments.txt
COPY . .
EXPOSE 8000
CMD ["python", "./app.py"]