---
title: "Khoảng cách mô phỏng – thực tế: cần thu hẹp hay cần đo?"
description: "Vì sao khoảng cách giữa hành vi mô phỏng và hành vi thực của robot có thể hữu ích hơn khi được đo và báo cáo như một thuộc tính của bộ điều khiển học được."
publishedAt: 2026-10-09
kind: "Research question"
tags:
  - robotics
  - machine learning
  - simulation
---

Bộ điều khiển và chính sách (policy) cho robot thường được huấn luyện trong mô phỏng rồi chạy trên phần cứng, và sự khác biệt giữa hai hành vi thường được mô tả như một khoảng cách cần thu hẹp. Ghi chú này đặt câu hỏi liệu có nên coi nó là một thuộc tính cần được đo và báo cáo hay không. Câu trả lời quan trọng với bất kỳ ai đọc hoặc đưa ra một khẳng định về một robot được huấn luyện bằng mô phỏng, vì nó quyết định khẳng định đó cần đi kèm loại bằng chứng nào.

## Đã xác lập

Một trình mô phỏng (simulator) là một mô hình. Để giữ chi phí tính toán trong tầm kiểm soát, và vì vật lý thực cùng các tham số thực chỉ được biết một phần, nó đơn giản hóa vật lý. Tiếp xúc thường được xấp xỉ bằng một mô hình đơn giản, ma sát thường được mô tả bằng vài hệ số, cơ cấu chấp hành (actuator) thường được lý tưởng hóa, còn cảm biến thường không có nhiễu hoặc chỉ được gán những mô hình nhiễu đơn giản. Một robot thực còn có những hiệu ứng như độ trễ truyền thông, độ rơ bánh răng (gear backlash) và độ đàn hồi của kết cấu, mà trình mô phỏng có thể bỏ qua hoặc chỉ mô tả một cách thô.

Một chính sách được huấn luyện trên một mô hình như vậy sẽ tối ưu cho hành vi của chính mô hình đó. Nếu hệ thực khác mô hình ở những chi tiết mà chính sách phụ thuộc vào, chính sách có thể hoạt động kém hơn hoặc thất bại. Sự sai khác này thường được gọi là **khoảng cách mô phỏng – thực tế** (sim-to-real gap).

Hai ý tưởng được dùng rộng rãi giúp giảm khoảng cách này. **Ngẫu nhiên hóa miền** (domain randomization) thay đổi các tham số của trình mô phỏng như khối lượng, hệ số ma sát hay nhiễu cảm biến trong quá trình huấn luyện, để chính sách tiếp xúc với cả một dải động lực học khả dĩ thay vì chỉ một. **Nhận dạng hệ thống** (system identification) khớp các tham số của trình mô phỏng với số liệu đo trên robot thực, để mô hình bám sát robot hơn.

## Diễn giải

Một cách hiểu là coi khoảng cách này như một thuộc tính đo được của một tổ hợp cụ thể gồm trình mô phỏng, chính sách, nhiệm vụ và robot, cần được kiểm tra thay vì được giả định là không có. Mọi trình mô phỏng đều được đơn giản hóa, nên luôn còn lại một khoảng cách nào đó, và câu hỏi thực tế là khoảng cách ấy có ảnh hưởng đến nhiệm vụ hay không. Theo từ vựng của loạt bài Mô phỏng số, đây là một câu hỏi [thẩm định](/blog/verifying-and-validating-a-simulation#4-validation) (validation): các dự đoán của mô hình khớp với số liệu đo trên hệ thực đến mức nào, trong phạm vi một độ không đảm bảo đã nêu rõ.

Một cách đơn giản để định lượng một phần của khoảng cách là áp dụng cùng một chuỗi tác động (action sequence), từ cùng một trạng thái ban đầu danh định, trong mô phỏng và trên phần cứng, rồi báo cáo

$$
\Delta(T) = \max_{0 \le t \le T} \lVert x_{\text{real}}(t) - x_{\text{sim}}(t) \rVert .
$$

Đại lượng này đo độ sai lệch quỹ đạo trên một khoảng thời gian $T$ và một chuẩn đã nêu rõ, đối với một chuỗi tác động được chọn. Nó trộn lẫn sai số động lực học với sai số đo và sai số trạng thái ban đầu. Nó cũng không phản ánh việc chính sách vòng kín xử lý sự sai lệch đó ra sao, nên các kết quả ở cấp nhiệm vụ, chẳng hạn tỉ lệ lần thử thành công trong cùng điều kiện, cần được báo cáo kèm theo. Sự đánh đổi rộng hơn giữa chính sách học được và điều khiển dựa trên mô hình là chủ đề của ghi chú về [điều khiển dựa trên mô hình và chính sách học được](/vi/insights/control-vs-learning-approaches).

## Câu hỏi còn mở

- Làm thế nào để chặn trên khoảng cách này trước khi triển khai, khi dữ liệu từ phần cứng thực khan hiếm hoặc không có? Loại bằng chứng nào đủ để biện minh cho một cận như vậy?
- Những chi tiết mô hình nào (tiếp xúc, ma sát, động lực học cơ cấu chấp hành, độ trễ, cảm biến) quan trọng nhất với nhiệm vụ nào, và có thể học được điều đó từ một lượng nhỏ dữ liệu thực hay không?
- Trong những điều kiện nào thì một sự bảo đảm, thay vì một phép đo, sẽ trở thành cách tốt hơn để xử lý khoảng cách này?
