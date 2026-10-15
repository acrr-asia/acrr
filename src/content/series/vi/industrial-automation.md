---
title: "Tự động hóa công nghiệp"
description: "Năm bài về tự động hóa các quá trình vật lý, từ logic Boole và PLC qua bus trường và vòng PID đến OPC UA và bản sao số."
category: "Engineering"
status: "published"
objectives:
  - "Biểu diễn các nhiệm vụ điều khiển dưới dạng logic Boole (Boolean logic) và dưới dạng chương trình tuần tự dựa trên trạng thái."
  - "Mô tả cách một bộ điều khiển logic khả trình (programmable logic controller) thực thi chương trình, và các ngôn ngữ được định nghĩa cho nó."
  - "So sánh các hệ thống bus trường (fieldbus) và Ethernet công nghiệp (industrial Ethernet) theo đặc tính thời gian, topo mạng (topology) và tính tất định (determinism)."
  - "Chỉnh định (tuning) các vòng PID cho những biến quá trình (process variable) điển hình như nhiệt độ, mức, lưu lượng và áp suất."
  - "Giải thích dữ liệu nhà máy đến các hệ thống cấp cao hơn như thế nào thông qua các cấp ISA-95 và OPC UA, và một bản sao số (digital twin) dùng phần dư (residual) để phát hiện sự cố ra sao."
---

Loạt bài này dành cho người đọc đã có kiến thức kỹ thuật điện cơ bản (điện áp, dòng điện, công tắc và rơ-le) và muốn hiểu cách các quá trình vật lý được tự động hóa. Loạt bài không giả định người đọc đã biết về logic số hay bộ điều khiển khả trình. Bài về điều khiển tỉ lệ – tích phân – vi phân (proportional–integral–derivative, PID) còn dùng các ý tưởng về phản hồi (feedback) của loạt bài [Cơ sở hệ thống điều khiển](/vi/series/foundations-of-control-systems).

Các bài xây dựng hệ thống tự động hóa của một nhà máy từ dưới lên, và mỗi bài dựa vào bài trước nó. Bài thứ nhất phát triển logic của tự động hóa: hàm Boole, mạch chốt (latch), bộ định thời (timer), bộ đếm (counter) và máy trạng thái (state machine). Bài thứ hai mô tả bộ điều khiển logic khả trình (PLC) thực thi logic đó: chu kỳ quét (scan cycle), các đầu vào và đầu ra số và 4–20 mA của nó, và các ngôn ngữ theo IEC 61131-3. Bài thứ ba mở rộng đặc tính thời gian vào – ra của PLC qua bus trường và Ethernet công nghiệp, những mạng kết nối bộ điều khiển với thiết bị với độ trễ bị chặn. Bài thứ tư khép các vòng phản hồi liên tục qua các đầu vào và đầu ra đó, với điều khiển PID nhiệt độ, mức, lưu lượng và áp suất, bao gồm chỉnh định và những vấn đề thực tế của các vòng điều khiển thật. Bài thứ năm nhìn lên phía trên: các cấp ISA-95 và OPC UA kết nối tầng điều khiển với các hệ thống cấp cao hơn như thế nào, kết nối đó được bảo mật ra sao, và một bản sao số chạy song song với nhà máy có thể ước lượng những gì không thiết bị đo nào đo được như thế nào.

Các bài dùng chung ba quy ước. Các ví dụ lập trình tuân theo ấn bản thứ ba của IEC 61131-3 (2013), và bài thứ hai lưu ý rằng phạm vi đã công bố của ấn bản 2025 không còn liệt kê Instruction List. Bài thứ tư biểu diễn tín hiệu quá trình và đầu ra bộ điều khiển theo phần trăm khoảng đo (span), như các hệ thống điều khiển quá trình hiển thị chúng. Các ví dụ tính toán được kiểm tra bằng những chương trình Python 3 ngắn chỉ dùng thư viện chuẩn, và kết quả thực của chúng được hiển thị.
