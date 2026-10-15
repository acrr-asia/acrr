---
title: "Điều gì làm cho một mô phỏng đáng tin cậy?"
description: "Kiểm chứng và thẩm định khác nhau thế nào, một nghiên cứu hội tụ cho thấy điều gì, và vì sao độ tin cậy của một mô phỏng phụ thuộc vào mục đích sử dụng nó."
publishedAt: 2026-10-09
kind: "Methodological note"
tags:
  - simulation
  - numerical methods
  - verification
---

Kết quả mô phỏng được dùng để chọn kích thước linh kiện, chỉnh định bộ điều khiển và lập luận rằng một thiết kế là an toàn, thường bởi những người đọc không viết ra mã đó. Ghi chú này tách những gì có thể xác lập về tính đúng đắn của một mô phỏng khỏi nhận định liệu nó có đáng tin cậy cho một mục đích cụ thể hay không, và liệt kê những gì vẫn còn khó. [Bài thứ năm của loạt bài Mô phỏng số](/blog/verifying-and-validating-a-simulation) trình bày sâu cùng chủ đề này.

## Đã xác lập

Theo thông lệ, hai câu hỏi được tách riêng. **Kiểm chứng** (verification) hỏi liệu các phương trình có đang được giải đúng hay không: mã có không có lỗi không, và sai số số có giảm khi bước thời gian hoặc lưới được làm mịn không? **Thẩm định** (validation) hỏi liệu có đang giải đúng các phương trình cần giải hay không: các dự đoán của mô hình có khớp với số liệu đo trên hệ thực, trong phạm vi một độ không đảm bảo đã nêu rõ, hay không?

Với một phương pháp số bậc $p$, sai số toàn cục sẽ tỉ lệ xấp xỉ với $h^p$ khi bước thời gian $h$ đủ nhỏ. Do đó, giảm $h$ đi một nửa sẽ làm sai số của một phương pháp bậc nhất như phương pháp Euler hiển (explicit Euler) giảm khoảng hai lần, và sai số của phương pháp Runge–Kutta bậc bốn cổ điển giảm khoảng mười sáu lần; bài [Ghi chú về tích phân số phương trình vi phân thường](/vi/blog/numerical-integration-notes) đo cả hai. Quan sát được tốc độ hội tụ như kỳ vọng trong một nghiên cứu làm mịn là bằng chứng cho thấy phần cài đặt là đúng, còn không quan sát được thì là một dấu hiệu cảnh báo.

Một số phương pháp còn có những kiểu thất bại về mặt định tính. Phương pháp Euler hiển áp dụng cho một bộ dao động không tắt dần làm năng lượng tăng lên sau mỗi bước. Sự tăng đó là một sản phẩm phụ của phương pháp số, không phải vật lý.

## Diễn giải

Một cách hiểu là độ tin cậy là thuộc tính của một mô phỏng cùng với mục đích sử dụng của nó, chứ không phải của riêng mô phỏng. Một mô hình có thể đủ tốt để dự đoán một xu hướng nhưng không đủ để dự đoán một biên an toàn. Vượt qua các bước kiểm chứng không xác lập được tính hợp lệ, vì một mô hình sai được giải hoàn hảo thì vẫn sai.

Vì vậy, một báo cáo đáng tin cậy nêu rõ các giả thiết, các giá trị tham số, các bước thời gian đã thử, và vùng chế độ mà trong đó việc so sánh với thực tế đã được tiến hành, vì ngoài vùng đó một dự đoán là một phép ngoại suy.

## Câu hỏi còn mở

- Nên định lượng độ không đảm bảo về dạng mô hình (model-form uncertainty), tức sai số đến từ chính các phương trình, như thế nào khi không có dữ liệu thực nghiệm?
- Khoảng cách giữa mô phỏng và hệ thực lớn đến đâu thì chấp nhận được đối với một quyết định cụ thể, và ai là người quyết định?
- Cách gọn nhất để trình bày cho người đọc một nghiên cứu hội tụ cùng các giả thiết của nó, mà không vùi chúng trong chi tiết, là gì?
