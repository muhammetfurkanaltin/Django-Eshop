# Python tabanlı bir imaj seçiyoruz
FROM python:3.10-slim

# MySQL istemci kütüphanelerini kur
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config

# Çalışma dizinini belirtiyoruz
WORKDIR /app

# Gereken dosyaları kopyalıyoruz
COPY requirements.txt /app/

# Bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyalıyoruz
COPY . /app/

# Django projesini çalıştırmak için komut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
