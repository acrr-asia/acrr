---
title: "Nhập môn robot học"
description: "Tìm hiểu cách một robot được cấu thành và phân tích: các phân hệ, hình học của hệ tọa độ, động học cánh tay và ước lượng trạng thái từ cảm biến có nhiễu."
category: "Robotics and Control"
status: "published"
objectives:
  - "Mô tả một robot gồm kết cấu cơ khí, cơ cấu chấp hành (actuator), cảm biến (sensor) và khối tính toán, được kết nối bằng một vòng điều khiển (control loop)."
  - "Biểu diễn vị trí và hướng của vật rắn (rigid body) bằng hệ tọa độ (coordinate frame) và ma trận quay (rotation matrix)."
  - "Giải thích động học thuận (forward kinematics) và động học ngược (inverse kinematics) cho một cánh tay phẳng (planar arm) đơn giản."
  - "Phác thảo cấu trúc cảm nhận – lập kế hoạch – hành động (sense, plan, act) được dùng trong nhiều kiến trúc phần mềm robot."
  - "Giải thích vì sao robot phải ước lượng trạng thái (state estimation) của mình, và bộ lọc Kalman (Kalman filter) kết hợp mô hình chuyển động với các phép đo có nhiễu như thế nào."
---

Loạt bài này dành cho người đọc đã quen với đại số tuyến tính cơ bản, lượng giác và giải tích (đạo hàm), và đã gặp mô-men lực (torque) và quán tính (inertia) trong cơ học nhập môn. Kiến thức xác suất cần thiết được giới thiệu ở bài cuối, nơi nó được dùng. Loạt bài không giả định người đọc đã biết gì về robot học; khái niệm phản hồi (feedback) được lấy từ loạt bài [Cơ sở hệ thống điều khiển](/vi/series/foundations-of-control-systems), nhưng có thể đọc các bài mà không cần loạt bài đó.

Bốn bài đi từ toàn bộ cỗ máy đến phần toán học mà mọi robot đều dựa vào, theo thứ tự mà mỗi ý tưởng trở nên cần thiết:

1. **Robot là gì.** Robot như một tổ hợp gồm kết cấu cơ khí, truyền động (actuation), cảm nhận (sensing) và tính toán, được nối với nhau bằng các vòng phản hồi chạy ở những tốc độ khác nhau, cùng các cách chính để tổ chức phần mềm của nó. Bài này cố định từ vựng (bậc tự do (degree of freedom), dư bậc tự do (redundancy), cảm nhận nội thể (proprioceptive) và ngoại thể (exteroceptive)) được các bài khác sử dụng.
2. **Hệ tọa độ và phép biến đổi.** Trước khi có thể xác định vị trí của bất kỳ bộ phận nào của robot, vị trí và hướng cần một ngôn ngữ chính xác: ma trận quay, góc Euler, quaternion, phép biến đổi thuần nhất (homogeneous transformation) và cây hệ tọa độ (frame tree).
3. **Động học của cánh tay phẳng.** Các phép biến đổi của bài 2 được áp dụng cho một cánh tay hai khâu, theo cả hai chiều: động học thuận, động học ngược dạng giải tích và dạng số, ma trận Jacobi (Jacobian) và các cấu hình kỳ dị (singular configuration).
4. **Cảm nhận và ước lượng trạng thái.** Bài 2 và bài 3 giả định rằng góc khớp và tư thế (pose) đã biết; bài này giải thích robot ước lượng chúng như thế nào từ các phép đo có nhiễu và có trễ, với một ví dụ bộ lọc Kalman được tính chi tiết.

Các bài dùng chung các quy ước: đơn vị SI, hệ tọa độ thuận tay phải, vector cột, và góc tính bằng radian trong mọi phép tính (các ví dụ hiển thị độ cho dễ đọc). Các ví dụ tính toán đủ nhỏ để kiểm tra bằng tay.
