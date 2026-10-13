---
title: "Tự động hóa công nghiệp"
description: "Loạt bài về tự động hóa các quá trình vật lý: điều khiển logic và điều khiển tuần tự (sequential control), bộ điều khiển logic khả trình (programmable logic controller, PLC), bus trường (fieldbus) và Ethernet công nghiệp (industrial Ethernet), điều khiển PID các biến quá trình (process variable), và tự động hóa nối mạng với bản sao số (digital twin)."
category: "Engineering"
status: "published"
objectives:
  - "Biểu diễn các nhiệm vụ điều khiển dưới dạng logic Boole (Boolean logic) và dưới dạng chương trình tuần tự dựa trên trạng thái."
  - "Mô tả cách một bộ điều khiển logic khả trình thực thi chương trình, và các ngôn ngữ lập trình được định nghĩa cho nó."
  - "So sánh các hệ thống bus trường và Ethernet công nghiệp theo đặc tính thời gian, topo mạng (topology) và tính tất định (determinism)."
  - "Chỉnh định (tuning) các vòng PID cho những biến quá trình điển hình như nhiệt độ, mức, lưu lượng và áp suất."
---

Loạt bài này dành cho người đọc đã có kiến thức kỹ thuật điện cơ bản (điện áp, dòng điện, công tắc và rơ-le) và muốn hiểu cách các quá trình vật lý được tự động hóa. Loạt bài không giả định người đọc đã biết về logic số hay bộ điều khiển khả trình; riêng bài về điều khiển PID có sử dụng các ý tưởng về phản hồi trong loạt bài Cơ sở hệ thống điều khiển. Loạt bài đi từ tầng dưới cùng của nhà máy lên trên: logic Boole, mạch chốt (latch), bộ định thời (timer) và máy trạng thái (state machine); bộ điều khiển logic khả trình (PLC) với chu kỳ quét (scan cycle), các đầu vào và đầu ra của nó và các ngôn ngữ lập trình theo IEC 61131-3; các mạng bus trường và Ethernet công nghiệp kết nối bộ điều khiển với thiết bị trường với độ trễ bị chặn; điều khiển PID nhiệt độ, mức, lưu lượng và áp suất, bao gồm chỉnh định và những vấn đề thực tế của các vòng điều khiển thật; và cuối cùng là việc kết nối hệ thống tự động hóa với các hệ thống cấp cao hơn thông qua ISA-95 và OPC UA, cùng các bản sao số chạy song song với nhà máy. Các ví dụ tính toán được kiểm tra bằng những chương trình Python ngắn.
