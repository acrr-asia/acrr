---
title: "Cơ sở hệ thống điều khiển"
description: "Loạt bài về cách phản hồi (feedback) định hình hành vi của các hệ động lực (dynamical system), từ những nguyên lý cơ bản đến mô hình không gian trạng thái (state-space model), tính ổn định và thiết kế phản hồi trạng thái."
category: "Robotics and Control"
status: "published"
objectives:
  - "Giải thích phản hồi làm thay đổi tính ổn định (stability) và tốc độ đáp ứng của một hệ thống như thế nào, và đáp ứng đó nhạy đến mức nào đối với sai lệch mô hình và nhiễu loạn (disturbance)."
  - "Mô tả một hệ tuyến tính bất biến theo thời gian (linear time-invariant system) ở cả dạng vào – ra (input-output form) lẫn dạng không gian trạng thái."
  - "Liên hệ các trị riêng (eigenvalue) của ma trận hệ thống với tính ổn định và hành vi quá độ (transient behavior)."
  - "Nhận ra các giả thiết và giới hạn của một mô hình trước khi thiết kế bộ điều khiển dựa trên mô hình đó."
---

Loạt bài này dành cho người đọc đã quen với giải tích và đại số tuyến tính cơ bản. Mỗi bài giới thiệu một ý tưởng, nêu rõ các giả thiết mà ý tưởng đó dựa vào, và chỉ ra ý tưởng tiếp theo trong chuỗi. Năm bài đi từ vòng kín và các chỉ tiêu chất lượng của nó, qua phản hồi tỉ lệ trên một hệ bậc nhất và mô hình không gian trạng thái, đến tính ổn định xét qua trị riêng và việc thiết kế một bộ điều khiển phản hồi trạng thái.
