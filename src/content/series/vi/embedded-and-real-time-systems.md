---
title: "Hệ thống nhúng và thời gian thực"
description: "Loạt bài về những chiếc máy tính nằm bên trong máy móc: kiến trúc vi điều khiển (microcontroller), ngắt (interrupt) và DMA, các bus trên bo mạch và trên xe, hệ điều hành thời gian thực (real-time operating system, RTOS) và lập lịch (scheduling), cùng việc đo đặc tính thời gian."
category: "Computing Systems"
status: "published"
objectives:
  - "Mô tả cách CPU, bộ nhớ, bộ định thời (timer), bộ chuyển đổi và ngoại vi (peripheral) của một vi điều khiển phối hợp với nhau."
  - "Lựa chọn giữa thăm dò (polling), ngắt và DMA để truyền dữ liệu cảm biến."
  - "So sánh các bus nối tiếp (serial bus) UART, SPI, I2C và CAN theo topo mạng (topology), tốc độ và cách xử lý lỗi."
  - "Giải thích lập lịch thời gian thực và kiểm chứng bằng phép đo rằng các thời hạn (deadline) đều được đáp ứng."
---

Loạt bài này dành cho người đọc đã biết lập trình C cơ bản (kiểu dữ liệu, con trỏ, cấu trúc và các toán tử thao tác bit) và logic số cơ bản (số nhị phân và thập lục phân, cổng logic, flip-flop và xung nhịp), và muốn hiểu những chiếc máy tính nhỏ điều khiển máy móc. Loạt bài bắt đầu từ các khái niệm cơ bản của hệ thống thời gian thực (thời hạn, độ trễ (latency) và độ dao động thời gian (jitter)) và các thành phần của một vi điều khiển, sau đó theo dòng dữ liệu đi từ ngoại vi vào bộ nhớ bằng thăm dò, ngắt và DMA, và giữa các chip và các bộ điều khiển qua UART, SPI, I2C và CAN. Tiếp theo, loạt bài trình bày cách một hệ điều hành thời gian thực tổ chức phần sụn (firmware) thành các tác vụ (task) có mức ưu tiên, cách phân tích lập lịch dự đoán liệu mọi thời hạn có được đáp ứng hay không, và kết thúc bằng việc đo thời gian thực thi, độ trễ, độ dao động thời gian, tải bộ xử lý và mức sử dụng bộ nhớ trên phần cứng thật để kiểm chứng các dự đoán đó. Các ví dụ được viết bằng C11 cho một vi điều khiển 32 bit tổng quát thuộc lớp Arm Cortex-M, còn các phép tính dùng Python.
