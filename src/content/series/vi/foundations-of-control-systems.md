---
title: "Cơ sở hệ thống điều khiển"
description: "Loạt bài về cách phản hồi định hình hành vi của hệ động lực, từ nguyên lý cơ bản đến mô hình không gian trạng thái, tính ổn định và thiết kế phản hồi trạng thái."
category: "Robotics and Control"
status: "published"
objectives:
  - "Giải thích phản hồi (feedback) làm thay đổi tính ổn định (stability) và tốc độ đáp ứng của một hệ thống như thế nào, và đáp ứng đó nhạy đến mức nào đối với sai lệch mô hình và nhiễu loạn (disturbance)."
  - "Mô tả một hệ tuyến tính bất biến theo thời gian (linear time-invariant system) ở cả dạng vào – ra (input-output form) lẫn dạng không gian trạng thái (state-space form)."
  - "Liên hệ các trị riêng (eigenvalue) của ma trận hệ thống với tính ổn định và hành vi quá độ (transient behavior)."
  - "Nhận ra các giả thiết và giới hạn của một mô hình trước khi thiết kế bộ điều khiển dựa trên mô hình đó."
---

Loạt bài này dành cho người đọc đã biết giải tích và đại số tuyến tính cơ bản (tích ma trận, ma trận nghịch đảo, trị riêng và vector riêng) và đọc được Python. Loạt bài cũng dùng số phức và phương trình vi phân tuyến tính hệ số hằng; mọi kiến thức vượt ra ngoài phạm vi đó, kể cả biến đổi Laplace (Laplace transform) và hàm mũ ma trận (matrix exponential), đều được giới thiệu tại chỗ chúng được dùng lần đầu.

Các bài xây dựng một mạch lập luận duy nhất. Bài thứ nhất trình bày từ vựng của một vòng phản hồi, các yêu cầu mà một bộ điều khiển phải đáp ứng, hàm truyền (transfer function) và các chỉ tiêu đáp ứng bước (step response) được dùng xuyên suốt loạt bài. Bài thứ hai áp dụng phản hồi tỉ lệ (proportional feedback) cho đối tượng điều khiển (plant) đơn giản nhất có thể, một hệ bậc nhất, và chỉ ra những gì phản hồi thay đổi: tốc độ, tính ổn định và độ nhạy, với cái giá là một sai lệch tĩnh (offset). Một phương trình bậc nhất duy nhất không thể mô tả một vật nặng gắn trên lò xo hay một khớp robot, vì vậy bài thứ ba giới thiệu mô hình không gian trạng thái (state-space model), vốn gộp nhiều phương trình bậc nhất thành một phương trình ma trận, và liên hệ nó với hàm truyền. Bài thứ tư giải thích vì sao các trị riêng của ma trận hệ thống quyết định tính ổn định và hành vi quá độ, và chúng không còn đủ ở đâu. Bài thứ năm dùng phản hồi từ trạng thái đo được để đặt các trị riêng đó, và xem xét một thiết kế như vậy giả định những gì về mô hình, cơ cấu chấp hành (actuator) và các phép đo.

Góc nhìn vào – ra được trình bày trước vì nó cho các chỉ tiêu chất lượng ở dạng đơn giản nhất; góc nhìn không gian trạng thái theo sau vì nó xử lý được nhiều biến và dẫn thẳng đến thiết kế.

Mọi bài dùng đơn vị SI, với thời gian tính bằng giây, tần số góc và trị riêng tính bằng radian trên giây, tiêu chuẩn 2% cho thời gian xác lập, và $j$ cho đơn vị ảo. Mã dùng Python 3, và dùng thêm NumPy từ bài thứ ba trở đi.
