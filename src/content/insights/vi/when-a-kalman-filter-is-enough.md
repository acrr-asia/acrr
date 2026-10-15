---
title: "Khi nào một bộ lọc Kalman là đủ?"
description: "Khi nào bộ lọc Kalman là bộ ước lượng phù hợp, khi nào cần các biến thể phi tuyến của nó hoặc bộ lọc hạt, và những câu hỏi nào về lựa chọn này vẫn còn mở."
publishedAt: 2026-10-11
kind: "Comparison"
tags:
  - control theory
  - robotics
  - state estimation
---

Một robot hay một quá trình hiếm khi đo trực tiếp trạng thái của mình, nên nó ước lượng trạng thái đó, và điểm xuất phát thông thường là bộ lọc Kalman (Kalman filter). Ghi chú này hỏi khi nào bộ lọc đó là đủ và khi nào một bộ ước lượng tốn kém hơn là xứng đáng, một lựa chọn quyết định cả chi phí tính toán lẫn kiểu thất bại có thể gặp. Bản thân các bộ ước lượng được mô tả và so sánh trong bài [Cảm nhận và ước lượng trạng thái: tổng quan](/vi/blog/sensing-and-state-estimation), bài cuối của loạt bài Nhập môn robot học.

## Đã xác lập

Xét mô hình $x_{k+1} = F x_k + w_k$, $z_k = H x_k + v_k$, với các ma trận $F$ và $H$ đã biết. Giả sử các nhiễu $w_k$ và $v_k$ có kỳ vọng bằng không, là nhiễu trắng và có phân phối Gauss, độc lập với nhau và với một trạng thái ban đầu có phân phối Gauss, với các ma trận hiệp phương sai $Q$ và $R$ đã biết. Khi đó bộ lọc Kalman tính chính xác $\mathbb{E}[x_k \mid z_{1:k}]$ và ma trận hiệp phương sai của nó. Kỳ vọng có điều kiện đó là ước lượng có sai số bình phương trung bình nhỏ nhất trong số mọi bộ ước lượng, dù tuyến tính hay không. Nếu nhiễu không có phân phối Gauss nhưng có cùng các ma trận hiệp phương sai, bộ lọc vẫn là tốt nhất trong số các bộ ước lượng tuyến tính, dù một bộ ước lượng phi tuyến có thể làm tốt hơn.

Với các mô hình phi tuyến, bộ lọc Kalman mở rộng (extended Kalman filter, EKF) tuyến tính hóa hàm động lực học và hàm đo quanh ước lượng hiện tại. Bộ lọc Kalman không mùi (unscented Kalman filter, UKF) thì thay vào đó đưa một tập nhỏ, tất định các điểm mẫu qua các hàm phi tuyến, và thường nắm bắt các hiệu ứng phi tuyến tốt hơn EKF với chi phí tương đương. Cả hai vẫn tóm tắt niềm tin (belief) bằng một phân phối Gauss duy nhất, và nói chung không bộ lọc nào là tối ưu. Bộ lọc hạt (particle filter) dùng các mẫu có trọng số, nên có thể biểu diễn những niềm tin đa đỉnh, không Gauss. Cái giá là khối lượng tính toán, tăng theo số hạt, và số hạt này thường phải tăng nhanh theo số chiều của trạng thái.

## Diễn giải

Một cách hiểu là câu hỏi quyết định không phải mô hình có phi tuyến hay không, mà là độ bất định có nhỏ so với thang đo mà trên đó tính phi tuyến phát huy tác dụng hay không. Điều đó gợi ra một hướng dẫn sơ lược:

- Mô hình tuyến tính, nhiễu gần với phân phối Gauss: một bộ lọc Kalman.
- Mô hình phi tuyến, trong đó một phân phối Gauss vẫn là bản tóm tắt chấp nhận được của niềm tin: một EKF khi tính phi tuyến yếu trên phạm vi trải rộng của độ bất định, một UKF khi nó mạnh hơn.
- Niềm tin thực sự đa đỉnh, chẳng hạn nhiều giả thuyết vị trí tách biệt: một bộ lọc hạt.

Theo cách hiểu này, thói quen hợp lý là bắt đầu với bộ lọc đơn giản nhất và chỉ chuyển lên mức cao hơn khi có bằng chứng cho thấy nó thất bại.

## Câu hỏi còn mở

- Làm thế nào để phát hiện một giả thiết Gauss bị vi phạm một cách âm thầm? Kiểm tra bình phương chuẩn hóa của phần dư đổi mới (normalized innovation squared), đại lượng phải tuân theo phân phối chi bình phương khi mô hình đúng, là một công cụ, nhưng chưa rõ khả năng phát hiện của nó trước các phân phối đuôi dày hay đa đỉnh.
- Nên chọn $Q$ và $R$ như thế nào? $Q$ phải hấp thụ phần động lực học không được mô hình hóa, và một bộ lọc có ma trận hiệp phương sai kém vẫn chạy và vẫn báo cáo một ma trận hiệp phương sai, có thể tự tin một cách sai lệch.
- Có thể ước lượng trực tuyến tỉ số giữa độ bất định và thang phi tuyến làm nền cho hướng dẫn ở trên hay không, để việc chọn bộ lọc không phải chờ đến khi quan sát thấy một thất bại?
