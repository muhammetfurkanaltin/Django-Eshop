# Python tabanlı bir imaj seçiyoruz
FROM python:3.10-slim

# Gerekli bağımlılıkları kuruyoruz
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential pkg-config && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini belirtiyoruz
WORKDIR /djangoEshop

# Gereken dosyaları kopyalıyoruz
COPY requirements.txt /djangoEshop/

# Bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyalıyoruz
COPY . /djangoEshop/

# Django projesini çalıştırmak için komut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
