---
title: "Hệ thống cảm biến"
description: "Loạt bài về chuỗi đo (measurement chain), từ một đại lượng vật lý đến một con số đáng tin cậy: phép đo là gì, cảm biến chuyển các hiệu ứng vật lý thành tín hiệu như thế nào, và các tín hiệu đó được chuẩn hóa (conditioning), chuyển đổi, làm sạch, hiệu chuẩn (calibration) và kết hợp ra sao."
category: "Engineering"
status: "in-progress"
objectives:
  - "Mô tả một hệ thống đo như một chuỗi đi từ đại lượng cần đo (measurand) đến con số, và đặc trưng hóa một cảm biến bằng các đặc tính tĩnh và động của nó."
  - "Giải thích các nguyên lý vật lý chính mà nhờ đó cảm biến chuyển một đại lượng thành tín hiệu điện."
  - "Thiết kế mạch đầu vào tương tự (analog front end) của cảm biến: nguồn kích thích (excitation), mạch cầu (bridge), khuếch đại và lọc."
  - "Giải thích lấy mẫu (sampling), lượng tử hóa (quantization) và chuyển đổi dữ liệu, cùng với nhiễu (noise) giới hạn những gì có thể phát hiện được."
  - "Phát biểu và tổng hợp độ không đảm bảo đo (measurement uncertainty), đồng thời hiệu chuẩn và hợp nhất (fusion) các cảm biến."
plannedEntries:
  - title: "Hiệu chuẩn và hợp nhất đa cảm biến"
    description: "Hiệu chuẩn và tính liên kết chuẩn (traceability) trong thực tế, và việc kết hợp nhiều cảm biến không hoàn hảo thành một ước lượng tốt hơn."
---

Loạt bài này dành cho người đọc đã quen với phân tích mạch cơ bản (định luật Ohm, mạch chia áp), giải tích và thống kê sơ cấp. Loạt bài bắt đầu từ câu hỏi phép đo là gì và theo dõi tín hiệu từ thế giới vật lý đến một con số đáng tin cậy. Những bài chưa viết được liệt kê là dự kiến, và đề cương có thể thay đổi khi các bài đó được viết.
