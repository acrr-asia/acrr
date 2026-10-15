---
title: "Hệ thống cảm biến"
description: "Theo dõi một phép đo từ đại lượng vật lý đến con số đáng tin cậy: cảm biến, chuẩn hóa tín hiệu, chuyển đổi, nhiễu, cảm biến thông minh, hiệu chuẩn và hợp nhất."
category: "Engineering"
status: "published"
objectives:
  - "Mô tả một hệ thống đo như một chuỗi đi từ đại lượng cần đo (measurand) đến con số, và đặc trưng hóa một cảm biến bằng các đặc tính tĩnh và động của nó."
  - "Giải thích các nguyên lý vật lý chính mà nhờ đó cảm biến chuyển một đại lượng thành tín hiệu điện."
  - "Thiết kế mạch đầu vào tương tự (analog front end) của cảm biến: nguồn kích thích (excitation), mạch cầu (bridge), khuếch đại và lọc."
  - "Giải thích lấy mẫu (sampling), lượng tử hóa (quantization) và chuyển đổi dữ liệu, cùng với nhiễu (noise) giới hạn những gì có thể phát hiện được."
  - "Phát biểu và tổng hợp độ không đảm bảo đo (measurement uncertainty), đồng thời hiệu chuẩn (calibration) và hợp nhất (fusion) các cảm biến."
---

Loạt bài này được viết cho người đọc đã quen với phân tích mạch cơ bản (định luật Ohm, mạch phân áp), giải tích và thống kê sơ cấp. Loạt bài theo dõi một phép đo từ thế giới vật lý đến một con số có thể tin cậy, và thứ tự của nó là thứ tự của chuỗi đo (measurement chain) mà bài thứ nhất trình bày.

Bài thứ nhất cung cấp từ vựng mà mọi bài sau đều dùng: đại lượng cần đo, các đặc tính của cảm biến, sai số và độ không đảm bảo đo. Bốn bài tiếp theo theo dõi tín hiệu qua từng tầng. Các nguyên lý cảm biến được trình bày trước, sau đó là chuẩn hóa tín hiệu (signal conditioning) tương tự, khâu làm cho một tín hiệu cảm biến nhỏ trở nên đo được, tiếp đến là lấy mẫu và chuyển đổi tương tự – số, rồi đến nhiễu và can nhiễu (interference), những thứ giới hạn những gì toàn bộ chuỗi có thể phát hiện. Bài thứ sáu cho thấy cảm biến thông minh (smart sensor) và hệ vi cơ điện tử (microelectromechanical systems, MEMS) xây dựng chuỗi đó trong một vỏ đóng gói duy nhất như thế nào. Bài cuối cùng khép lại vòng lặp bằng hiệu chuẩn, khâu làm cho các con số của một kênh đo có tính liên kết chuẩn (traceability), và bằng việc hợp nhất nhiều cảm biến không hoàn hảo thành một ước lượng tốt hơn.

Hai ví dụ xuyên suốt loạt bài. Một nhiệt điện trở bạch kim PT100 minh họa độ phi tuyến ở bài thứ nhất, nguồn kích thích và sai số do dây dẫn ở bài thứ ba, và việc khớp đường cong hiệu chuẩn ở bài cuối. Một kênh cân dùng cảm biến lực (load cell) được thiết kế ở bài thứ ba, số hóa ở bài thứ tư, lập ngân sách nhiễu (noise budget) ở bài thứ năm và hiệu chuẩn ở bài thứ bảy.

Đơn vị là SI, với gia tốc còn được cho theo bội số của gia tốc trọng trường tiêu chuẩn *g* và đầu ra của cầu đo tính bằng milivôn trên vôn. Các thuật ngữ về phép đo và độ không đảm bảo đo tuân theo *International Vocabulary of Metrology* (Từ vựng quốc tế về đo lường học, VIM) và *Guide to the Expression of Uncertainty in Measurement* (Hướng dẫn biểu thị độ không đảm bảo đo, GUM), như bài thứ nhất giải thích. Điện áp và dòng điện nhiễu là giá trị hiệu dụng (root-mean-square), được tính ở 300 K trừ khi có ghi chú khác. Các ví dụ mã ở bài cuối dùng Python 3 với NumPy.
