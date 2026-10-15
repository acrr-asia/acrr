---
title: "Điều khiển dựa trên mô hình và chính sách học được"
description: "Điều khiển dựa trên mô hình và chính sách học được mỗi bên mang lại gì, điều gì đã được xác lập về chúng, và khi nào bên nào là lựa chọn thực tế hơn."
publishedAt: 2026-10-11
kind: "Comparison"
tags:
  - control theory
  - machine learning
  - robotics
---

Một bộ điều khiển có thể được thiết kế từ mô hình toán học của hệ thống, hoặc một chính sách (policy) có thể được học từ dữ liệu thu được khi tương tác với hệ thống. Hai họ phương pháp này thường được trình bày như những đối thủ. Ghi chú này tách điều đã được xác lập về mỗi họ khỏi phần diễn giải về khi nào họ nào là lựa chọn tốt hơn, dành cho các kỹ sư đang quyết định cách điều khiển một hệ thống mà mô hình của nó chỉ được biết một phần.

## Đã xác lập

**Điều khiển dựa trên mô hình** (model-based control) thiết kế một luật phản hồi từ một mô hình toán học của hệ thống. Loạt bài [Cơ sở hệ thống điều khiển](/vi/series/foundations-of-control-systems) xây dựng cách tiếp cận này từ những nguyên lý cơ bản, kết thúc bằng [thiết kế phản hồi trạng thái](/blog/state-feedback-controller-design). Với một mô hình tuyến tính và một hàm chi phí bậc hai, bộ điều chỉnh tuyến tính – bậc hai (linear-quadratic regulator, LQR) cho ra một độ lợi phản hồi trạng thái tối ưu. Dự trữ độ lợi và dự trữ pha (gain and phase margins) kinh điển đo lượng độ lợi vòng tăng thêm, hoặc độ trễ pha tăng thêm như một thời gian trễ không được mô hình hóa, mà một vòng một đầu vào – một đầu ra (single-input single-output) chịu được trước khi trở nên không ổn định; mỗi đại lượng chỉ bao quát một loại sai số mô hình tại một thời điểm. Điều khiển dự báo theo mô hình (model predictive control, MPC) giải một bài toán tối ưu trên một khoảng thời gian hữu hạn ở mỗi bước, dùng một mô hình, và có thể biểu diễn tường minh các ràng buộc lên đầu vào và trạng thái.

**Các phương pháp dựa trên học máy**, chẳng hạn học tăng cường (reinforcement learning), cải thiện một chính sách bằng dữ liệu thu được qua tương tác, trong mô phỏng hoặc trên phần cứng. Chúng không cần một mô hình động lực học ở dạng đóng, và có thể biểu diễn những hành vi phi tuyến khó viết ra bằng tay. Cái giá thường gặp là cần lượng dữ liệu lớn và các bảo đảm hình thức yếu hơn: một chính sách đã huấn luyện thường không đi kèm chứng minh ổn định, trừ khi bổ sung thêm cấu trúc. Một chính sách được huấn luyện trong mô phỏng cũng có thể hoạt động kém hơn trên phần cứng, vì động lực học mô phỏng và động lực học thực khác nhau; sự khác biệt đó là [khoảng cách mô phỏng – thực tế](/vi/insights/closing-the-sim-to-real-gap) (sim-to-real gap). Loạt bài [Cơ sở học máy](/vi/series/machine-learning-fundamentals) trình bày các ý tưởng nền tảng của việc học từ dữ liệu và của việc đánh giá những gì một mô hình đã học được.

## Diễn giải

Một cách hiểu là hai cách tiếp cận này là hai đầu của một phổ chứ không phải hai đối thủ, và có hai yếu tố quyết định giữa chúng: lượng hiểu biết đáng tin cậy về mô hình hiện có, và cái giá của một lần thất bại. Khi có sẵn một mô hình đủ chính xác và an toàn là điều quan trọng, thiết kế dựa trên mô hình cung cấp khả năng phân tích mà một chính sách học được thường không có. Khi động lực học hoặc các tiếp xúc quá phức tạp để mô hình hóa tốt, học máy có thể là con đường thực tế hơn.

Các phương pháp lai cố gắng kết hợp cả hai: học một thành phần hiệu chỉnh đặt chồng lên một bộ điều khiển danh định, hoặc học chính mô hình mà một bộ MPC sau đó sử dụng. Mức độ thành công của chúng phụ thuộc vào hệ thống cụ thể và vào cách ràng buộc phần được học, và chưa thấy một câu trả lời chung nào.

## Câu hỏi còn mở

- Làm thế nào để chứng nhận tính ổn định hoặc tính an toàn của một thành phần học được mà chi phí chứng nhận không vượt quá chính chi phí huấn luyện?
- Những bộ chuẩn đánh giá (benchmark) nào so sánh hai họ phương pháp một cách công bằng, có tính đến dữ liệu, công sức thiết kế và độ bền vững chứ không chỉ phần thưởng cuối cùng?
- Khi thêm một thành phần hiệu chỉnh học được vào một bộ điều khiển danh định, trong những điều kiện nào thì các bảo đảm của thiết kế danh định vẫn còn giữ được?
