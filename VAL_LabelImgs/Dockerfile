# Sử dụng phiên bản slim và cài đặt các gói cần thiết
FROM python:3.8.19-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libx11-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt các thư viện để hỗ trợ PyQt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install PyQt5==5.15.11
RUN pip install lxml

# Sao chép mã nguồn vào container
COPY . /app

# Cài đặt các yêu cầu khác
RUN pip install -r requirements.txt

# Thiết lập biến môi trường DISPLAY với IP của host
ENV DISPLAY=host.docker.internal:0.0

# Khởi chạy ứng dụng PyQt
CMD ["python", "autolabelImg.py"]
