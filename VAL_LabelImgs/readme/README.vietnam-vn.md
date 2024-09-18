[English](../../README.md) | [简体中文](README.zh-CN.md) | [Tiếng việt](README.vietnam-vn.md)
# VAL LabelImg

Đây là một công cụ dùng để đánh nhãn dựa trên [LabelImg](https://github.com/HumanSignal/labelImg), chủ yếu được thiết kế để đánh nhãn cho Object Detection. Công cụ này giới thiệu một số tính năng mới, chẳng hạn như việc tích hợp AutoLabelImg với các backbone dựa trên các thuật toán mới nhất như YOLOv8, YOLOv9, YOLOv10 và RT-DETR, cho phép đánh nhãn hàng nghìn hình ảnh chỉ trong một thời gian rất ngắn. Dự án được phát triển bởi Tien-Dat Nguyen, một thành viên của Vision and Learning Lab tại Trường Đại học sư phạm Kỹ thuật Hưng Yên.
## Contents
1. [Introduction](#introduction)
2. [Timeline](#timeline)
3. [Installation](#installation)
4. [Quick Start Overview](#quick-start-overview)
5. [Send Us Feedback!](#send-us-feedback)
6. [License](#license)


# Introduction
Bằng cách sử dụng YOLO và RT-DETR mới nhất, chúng ta có thể đánh nhãn hàng nghìn hình ảnh chỉ trong một thời gian rất ngắn. Công cụ này được thiết kế để thân thiện với người dùng và dễ sử dụng, với giao diện đơn giản cho phép người dùng đánh nhãn hình ảnh một cách nhanh chóng và hiệu quả. Công cụ cũng được trang bị nhiều tính năng giúp dễ sử dụng, chẳng hạn như khả năng đánh nhãn nhiều đối tượng trong một hình ảnh, khả năng đánh nhãn các đối tượng có hình dạng và kích thước khác nhau, và khả năng đánh nhãn các đối tượng với các màu sắc khác nhau. Bên cạnh đó, chúng ta có thể sử dụng các lớp tùy chỉnh từ weights của bạn.
<p align="center">
    <img src="images/imgs1.png" width="360">
</p>

Giao diện của VAL-AutoLabelImg tương tự như [LabelImg](https://github.com/HumanSignal/labelImg)
Bạn có thể xem video demo của chúng tôi như sau:
<p align="center">
    <img src="videos/demo.gif" width="1000">
    <br>
    <sup>Demo VAL-AutoLabelImg <a href="https://github.com/ultralytics/ultralytics" target="_blank"><i>on Yolov8</i></a></sup>
</p>

# Timeline
- [Ngày 18 tháng 9 năm 2024] VAL-AutoLabelImg cho phép dùng weights tùy chỉnh với file yaml tuỳ chỉnh.
- [Ngày 17 tháng 9 năm 2024] Chúng tôi công bố Docker Images trên [Docker Hub.](https://hub.docker.com/r/nguyendat1354/val-autolabel)
- [Ngày 15 tháng 9 năm 2024] Chúng tôi thêm RT-DETR vào VAL-AutoLabelImg.
- [Ngày 13 tháng 9 năm 2024] Chúng tôi thêm AutoLabelImg với [YoloV9](https://github.com/WongKinYiu/yolov9) và [YoloV10](https://github.com/THU-MIG/yolov10).
- [Ngày 12 tháng 9 năm 2024] Chúng tôi phát hành phiên bản đầu tiên của VAL-AutoLabelImg, bao gồm YOLOv8.
# Installation

### Với Python Base
Requirements python >= 3.8
1. Cài đặt thư viện phụ thuộc
 ```bash
%cd VAL_ImglabelImg
pip install -r requirements.txt
pyrcc5 -o libs/resources.py resources.qrc
```

### Với Anaconda 
1. Cài đặt thư viện phụ thuộc
   - Bạn có thể load và cài thư viện bằng file ``` env.yaml```.
   - Bạn có thể tìm thấy file ```env.yaml``` trong folder ```Conda```
2. Sau khi bạn cài đặt các thư viện phụ thuộc, bạn có thể chạy lệnh này để xây dựng tài nguyên cho PyQT.
```bash
pyrcc5 -o libs/resources.py resources.qrc
```

### Với Docker
Bạn có thể xây dựng Docker Images với tệp Docker của tôi.
1. Xây dựng docker images
In folder ``VAL_LabelImg``` of this project open command prompt and run
``` bash
%cd VAL_LabelImg
docker build -t [names_you_choose] .
Example: docker build -t valautolabels .
```

### With Docker Hub
Bạn có thể kéo Docker Images từ Docker Hub của tôi.

# Quick Start Overview
### Với môi trường Python Base và môi trường Anaconda
1. Chạy nhanh
- Bạn có thể chạy file ```autolabelImg.py``` để bắt đầu dự án.

2. Sử dụng command line
- Bạn có thể sử dụng command line này để chạy dự án
```bash
%cd VAL_LabelImg
python mainapp.py
```

### With Docker
1. Chạy nhanh
Bạn truy cập dự án này với lệnh này
```bash
docker run -it \
--env DISPLAY=$DISPLAY \
--volume /tmp/.X11-unix:/tmp/.X11-unix \
--device /dev/snd \
your_image_name
```

# Send Us FeedBack
Dự án của chúng tôi là mã nguồn mở dành cho mục đích nghiên cứu, và chúng tôi muốn cải thiện nó! Vì vậy, hãy cho chúng tôi biết (tạo một vấn đề mới trên GitHub hoặc yêu cầu kéo, gửi email cho chúng tôi, v.v.) nếu bạn...
1. Tìm hoặc sửa bất kỳ lỗi nào hoặc biết cách tăng tốc hoặc cải thiện bất kỳ phần nào của VAL-LabelImg.
2. Muốn thêm/hiển thị một số chức năng/demo/dự án hay được xây dựng dựa trên VAL-AutoLabelImg. Chúng tôi có thể thêm liên kết dự án của bạn vào. [Issue](https://github.com/datnguyen-tien204/VAL_ImglabelImg/issues)

# License
Dự án này có sẵn miễn phí cho mục đích sử dụng phi thương mại. Nếu thấy hữu ích, bạn có thể cho 1 sao. Cảm ơn bạn đã sử dụng.
