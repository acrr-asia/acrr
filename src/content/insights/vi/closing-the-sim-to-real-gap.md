---
title: "Khoảng cách mô phỏng – thực tế: cần thu hẹp hay cần đo?"
description: "Một câu hỏi nghiên cứu ngắn về khoảng cách giữa hành vi mô phỏng và hành vi thực của robot đối với các bộ điều khiển học được, và vì sao có thể hữu ích hơn khi coi nó là một đại lượng được đo thay vì một khiếm khuyết cần loại bỏ."
publishedAt: 2026-10-09
kind: "Research question"
tags:
  - robotics
  - machine-learning
  - simulation
---

## Đã xác lập

Một trình mô phỏng (simulator) là một mô hình. Để giữ chi phí tính toán trong tầm kiểm soát, và vì vật lý thực cùng các tham số thực chỉ được biết một phần, nó đơn giản hóa hoặc xấp xỉ vật lý: tiếp xúc thường được xấp xỉ bằng một mô hình đơn giản, ma sát thường được mô tả bằng vài hệ số, cơ cấu chấp hành (actuator) thường được lý tưởng hóa, còn cảm biến thường không có nhiễu hoặc chỉ được gán những mô hình nhiễu đơn giản. Một robot thực còn có những hiệu ứng như độ trễ truyền thông, độ rơ bánh răng (gear backlash) và độ đàn hồi của kết cấu, mà trình mô phỏng có thể bỏ qua hoặc chỉ mô tả một cách thô.

Một chính sách (policy) được huấn luyện trên một mô hình như vậy sẽ tối ưu cho hành vi của chính mô hình đó. Nếu hệ thực khác mô hình ở những chi tiết mà chính sách phụ thuộc vào, chính sách có thể hoạt động kém hơn hoặc thất bại. Sự sai khác này thường được gọi là khoảng cách mô phỏng – thực tế (sim-to-real gap).

Hai ý tưởng giảm thiểu được dùng rộng rãi là ngẫu nhiên hóa miền (domain randomisation), tức thay đổi các tham số của trình mô phỏng như khối lượng, hệ số ma sát hay nhiễu cảm biến trong quá trình huấn luyện để chính sách tiếp xúc với cả một dải động lực học khả dĩ thay vì chỉ một, và nhận dạng hệ thống (system identification), tức khớp các tham số của trình mô phỏng với số liệu đo trên robot thực để mô hình bám sát robot hơn.

## Diễn giải

Một cách hiểu hợp lý là coi khoảng cách này như một đại lượng đo được của một tổ hợp cụ thể gồm trình mô phỏng, chính sách, nhiệm vụ và robot, và cần được kiểm tra thay vì được giả định là không có. Vì mọi trình mô phỏng đều được đơn giản hóa, nên có thể dự kiến luôn còn lại một khoảng cách nào đó; câu hỏi thực tế là khoảng cách ấy có ảnh hưởng đến nhiệm vụ hay không.

Một cách đơn giản để định lượng một phần của nó là áp dụng cùng một chuỗi tác động (action sequence), từ cùng một trạng thái ban đầu danh định, trong mô phỏng và trên phần cứng, rồi báo cáo

$$
\Delta(T) = \max_{0 \le t \le T} \lVert x_{\text{real}}(t) - x_{\text{sim}}(t) \rVert .
$$

Đại lượng này đo độ sai lệch quỹ đạo trên một khoảng thời gian $T$ và một chuẩn đã nêu rõ, đối với một chuỗi tác động được chọn. Nó trộn lẫn sai số động lực học với sai số đo và sai số trạng thái ban đầu, và không phản ánh việc chính sách vòng kín xử lý sự sai lệch đó ra sao, nên các kết quả ở cấp nhiệm vụ, chẳng hạn tỉ lệ lần thử thành công trong cùng điều kiện, cần được báo cáo kèm theo.

## Câu hỏi còn mở

- Làm thế nào để chặn trên khoảng cách này trước khi triển khai, khi dữ liệu từ phần cứng thực khan hiếm hoặc không có? Loại bằng chứng nào đủ để biện minh cho một cận như vậy?
- Những chi tiết mô hình nào (tiếp xúc, ma sát, động lực học cơ cấu chấp hành, độ trễ, cảm biến) quan trọng nhất với nhiệm vụ nào, và có thể học được điều đó từ một lượng nhỏ dữ liệu thực hay không?
- Trong những điều kiện nào thì một sự bảo đảm, thay vì một phép đo, sẽ trở thành cách tốt hơn để xử lý khoảng cách này?
