---
title: "Hệ thống nhúng và thời gian thực"
description: "Loạt bài dự kiến về những chiếc máy tính nằm bên trong máy móc: kiến trúc vi điều khiển (microcontroller), ngắt (interrupt) và DMA, các bus trên bo mạch và trên xe, hệ điều hành thời gian thực (real-time operating system, RTOS) và lập lịch (scheduling), cùng việc đo đặc tính thời gian."
category: "Computing Systems"
status: "planned"
objectives:
  - "Mô tả cách CPU, bộ nhớ, bộ định thời (timer), bộ chuyển đổi và ngoại vi (peripheral) của một vi điều khiển phối hợp với nhau."
  - "Lựa chọn giữa thăm dò (polling), ngắt và DMA để truyền dữ liệu cảm biến."
  - "So sánh các bus nối tiếp (serial bus) UART, SPI, I2C và CAN theo topo mạng (topology), tốc độ và cách xử lý lỗi."
  - "Giải thích lập lịch thời gian thực và kiểm chứng bằng phép đo rằng các thời hạn (deadline) đều được đáp ứng."
plannedEntries:
  - title: "Bên trong một vi điều khiển"
    description: "CPU, bản đồ bộ nhớ (memory map), xung nhịp (clock), bộ định thời, bộ chuyển đổi tương tự – số (analog-to-digital converter, ADC) và cổng vào/ra đa dụng (general-purpose I/O), cùng cách phần sụn (firmware) điều khiển chúng."
  - title: "Ngắt, thăm dò và DMA"
    description: "Ba cách truyền dữ liệu giữa ngoại vi và bộ nhớ, và ảnh hưởng của mỗi cách đến độ trễ (latency) và tải CPU."
  - title: "Bus nối tiếp: UART, SPI, I2C và CAN"
    description: "Cách mỗi bus đóng khung (framing), đánh địa chỉ và kiểm tra dữ liệu, và nơi mỗi bus được dùng, từ bo mạch cảm biến đến xe cộ."
  - title: "Hệ điều hành thời gian thực và lập lịch"
    description: "Tác vụ (task), mức ưu tiên, đồng bộ hóa (synchronisation) và lý thuyết lập lịch cho biết các thời hạn có thể được đáp ứng hay không."
  - title: "Đo đặc tính thời gian, độ trễ và mức sử dụng tài nguyên"
    description: "Gắn công cụ đo (instrumentation) vào phần mềm nhúng để kiểm chứng thời gian thực thi, độ dao động thời gian (jitter) và mức sử dụng bộ nhớ trên phần cứng thật."
---

Loạt bài này đang được lên kế hoạch và chưa bắt đầu xuất bản. Loạt bài giả định người đọc đã biết lập trình C cơ bản và logic số. Đề cương dưới đây mô tả phạm vi dự kiến và có thể thay đổi trước khi bất kỳ bài nào được viết.
