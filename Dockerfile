FROM python:3.8-slim

# 為了跑腳本，要安裝這個
# RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# COPY wait.sh /wait.sh
# RUN chmod +x /wait.sh

EXPOSE 8000

CMD ["python", "main.py"]
# "/wait.sh",