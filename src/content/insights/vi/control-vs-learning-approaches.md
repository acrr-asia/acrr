---
title: "Điều khiển dựa trên mô hình và chính sách học được"
description: "Một so sánh ngắn giữa điều khiển dựa trên mô hình và các chính sách dựa trên học máy, tách bạch điều đã được xác lập vững chắc với phần diễn giải và các câu hỏi còn mở."
publishedAt: 2026-10-11
kind: "Comparison"
tags:
  - control theory
  - machine learning
  - robotics
---

## Đã xác lập

Điều khiển dựa trên mô hình (model-based control) thiết kế một luật phản hồi từ một mô hình toán học của hệ thống. Với một mô hình tuyến tính và một hàm chi phí bậc hai, bộ điều chỉnh tuyến tính – bậc hai (linear-quadratic regulator, LQR) cho ra một ma trận độ lợi phản hồi trạng thái tối ưu. Các công cụ kinh điển như dự trữ độ lợi và dự trữ pha (gain and phase margins) mô tả mức sai số mô hình mà một số vòng kín nhất định có thể chịu được. Điều khiển dự báo theo mô hình (model predictive control, MPC) giải một bài toán tối ưu trên một khoảng thời gian hữu hạn ở mỗi bước, dùng một mô hình, và có thể biểu diễn tường minh các ràng buộc lên đầu vào và trạng thái.

Các phương pháp dựa trên học máy, chẳng hạn học tăng cường (reinforcement learning), cải thiện một chính sách (policy) bằng dữ liệu thu được qua tương tác, trong mô phỏng hoặc trên phần cứng. Chúng không cần một mô hình động lực học ở dạng tường minh, và có thể biểu diễn những hành vi phi tuyến khó viết ra bằng tay. Cái giá thường gặp là cần lượng dữ liệu lớn và các bảo đảm hình thức yếu hơn: một chính sách đã huấn luyện thường không đi kèm chứng minh ổn định, trừ khi bổ sung thêm cấu trúc. Một chính sách được huấn luyện trong mô phỏng cũng có thể hoạt động kém hơn trên phần cứng, vì động lực học mô phỏng và động lực học thực khác nhau. Sự khác biệt này thường được gọi là khoảng cách mô phỏng – thực tế (sim-to-real gap).

## Diễn giải

Hai cách tiếp cận này nên được hiểu như hai đầu của một phổ hơn là hai đối thủ. Các yếu tố quyết định có vẻ là lượng hiểu biết đáng tin cậy về mô hình hiện có và cái giá của một lần thất bại. Khi có sẵn một mô hình đủ chính xác và an toàn là điều quan trọng, thiết kế dựa trên mô hình cung cấp khả năng phân tích mà một chính sách học được thường không có. Khi động lực học hoặc các tiếp xúc quá phức tạp để mô hình hóa tốt, học máy có thể là con đường thực tế hơn.

Các phương pháp lai cố gắng kết hợp cả hai: học một thành phần hiệu chỉnh đặt chồng lên một bộ điều khiển danh định, hoặc học chính mô hình mà một bộ MPC sau đó sử dụng. Mức độ thành công của chúng nhiều khả năng phụ thuộc vào hệ thống cụ thể và vào cách ràng buộc phần được học.

## Câu hỏi còn mở

- Làm thế nào để chứng nhận tính ổn định hoặc tính an toàn của một thành phần học được mà chi phí chứng nhận không vượt quá chính chi phí huấn luyện?
- Những bộ chuẩn đánh giá (benchmark) nào so sánh hai họ phương pháp một cách công bằng, có tính đến dữ liệu, công sức thiết kế và độ bền vững chứ không chỉ phần thưởng cuối cùng?
- Khi thêm một thành phần hiệu chỉnh học được vào một bộ điều khiển danh định, trong những điều kiện nào thì các bảo đảm của thiết kế danh định vẫn còn giữ được?
