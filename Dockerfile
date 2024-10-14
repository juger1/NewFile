FROM python:latest
WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT ["python3"]
CMD ["main.py"]
