---
title: "Nhập môn robot học"
description: "Loạt bài giới thiệu robot như những hệ thống gồm kết cấu, truyền động (actuation), cảm nhận (sensing) và tính toán, được kết nối với nhau bằng phản hồi (feedback)."
category: "Robotics and Control"
status: "published"
objectives:
  - "Mô tả một robot gồm kết cấu cơ khí, cơ cấu chấp hành (actuator), cảm biến (sensor) và khối tính toán, được kết nối bằng một vòng điều khiển (control loop)."
  - "Biểu diễn vị trí và hướng của vật rắn (rigid body) bằng hệ tọa độ (coordinate frame) và ma trận quay (rotation matrix)."
  - "Giải thích động học thuận (forward kinematics) và động học ngược (inverse kinematics) cho một cánh tay phẳng (planar arm) đơn giản."
  - "Phác thảo cấu trúc cảm nhận – lập kế hoạch – hành động (sense, plan, act) được dùng trong nhiều kiến trúc phần mềm robot."
  - "Giải thích vì sao robot phải ước lượng trạng thái (state estimation) của mình, và bộ lọc Kalman (Kalman filter) kết hợp mô hình chuyển động với các phép đo có nhiễu như thế nào."
---

Loạt bài này dành cho người đọc đã quen với đại số tuyến tính cơ bản, lượng giác và giải tích (đạo hàm), và đã gặp mô-men lực (torque) và quán tính (inertia) trong cơ học nhập môn. Kiến thức xác suất cần thiết được giới thiệu ngay tại chỗ nó được dùng. Loạt bài bắt đầu từ câu hỏi robot là gì rồi đi dần xuống hình học, động học và ước lượng mà mọi robot đều dựa vào.
