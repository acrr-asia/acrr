---
title: "Hệ thống nhúng và thời gian thực"
description: "Theo dòng dữ liệu qua những máy tính nhỏ bên trong máy móc, từ phần cứng vi điều khiển và bus nối tiếp đến lập lịch thời gian thực và đo đặc tính thời gian."
category: "Computing Systems"
status: "published"
objectives:
  - "Mô tả cách CPU, bộ nhớ, bộ định thời (timer), bộ chuyển đổi và ngoại vi (peripheral) của một vi điều khiển (microcontroller) phối hợp với nhau."
  - "Lựa chọn giữa thăm dò (polling), ngắt (interrupt) và DMA để truyền dữ liệu cảm biến."
  - "So sánh các bus nối tiếp (serial bus) UART, SPI, I2C và CAN theo topo mạng (topology), tốc độ và cách xử lý lỗi."
  - "Giải thích lập lịch thời gian thực (real-time scheduling), tính thời gian đáp ứng trong trường hợp xấu nhất (worst-case response time) và đối chiếu chúng với phép đo."
---

Loạt bài này dành cho người đọc đã biết lập trình C cơ bản (kiểu dữ liệu, con trỏ, cấu trúc và các toán tử thao tác bit) và logic số cơ bản (số nhị phân và thập lục phân, cổng logic, flip-flop và xung nhịp), và muốn hiểu những chiếc máy tính nhỏ điều khiển máy móc. Loạt bài không giả định người đọc đã có kinh nghiệm về hệ thống nhúng. Loạt bài xét các vi điều khiển một lõi; lập lịch đa lõi, Linux nhúng, API của bất kỳ nhân (kernel) cụ thể nào, thiết kế mạch và chứng nhận an toàn nằm ngoài phạm vi của nó.

Các bài theo dòng dữ liệu đi qua một hệ thống nhúng rồi chuyển sang vấn đề thời gian. Bài thứ nhất định nghĩa từ vựng về thời gian của toàn bộ loạt bài (sự kiện, thời hạn (deadline), độ trễ (latency) và độ dao động thời gian (jitter)) và các thành phần của một vi điều khiển, rồi kết thúc bằng cấu trúc phần sụn (firmware) đơn giản nhất, vòng lặp lớn (superloop), trong đó mọi sự kiện đều phải chờ phần còn lại của vòng lặp. Bài thứ hai phân tích việc thăm dò mà vòng lặp lớn thực hiện và chỉ ra cách ngắt và truy cập bộ nhớ trực tiếp (direct memory access, DMA) cho phép xử lý các sự kiện phần cứng ngay khi chúng xảy ra, cùng cái giá của mỗi phương pháp về độ trễ và thời gian bộ xử lý. Bài thứ ba theo dữ liệu ra khỏi chip qua bốn bus nối tiếp: bộ thu phát không đồng bộ vạn năng (universal asynchronous receiver-transmitter, UART), giao diện ngoại vi nối tiếp (Serial Peripheral Interface, SPI), Inter-Integrated Circuit (I2C) và mạng vùng điều khiển (Controller Area Network, CAN).

Bài thứ tư gỡ bỏ giới hạn mà bài thứ hai còn để lại, đó là việc xử lý vẫn chạy trong một vòng lặp, bằng cách tổ chức nó thành các tác vụ (task) có mức ưu tiên dưới một hệ điều hành thời gian thực (real-time operating system), và tính xem mọi thời hạn có được đáp ứng trong trường hợp xấu nhất hay không. Bài thứ năm đo thời gian thực thi, độ trễ, độ dao động thời gian, tải bộ xử lý và mức sử dụng bộ nhớ trên phần cứng thật, và đối chiếu kết quả tính toán với các phép đo đó.

Quy ước chung: mã được viết bằng C11 cho một vi điều khiển 32 bit tổng quát thuộc lớp Arm Cortex-M chạy ở 48 MHz, với cách bố trí thanh ghi ngoại vi được đặt ra để minh họa; các ví dụ trên máy tính để bàn dùng giao diện hệ điều hành khả chuyển (Portable Operating System Interface, POSIX); các phép tính dùng Python 3 với thư viện chuẩn. Thời gian dùng tiền tố SI và dung lượng bộ nhớ dùng tiền tố nhị phân (1 KiB = 1024 byte).
