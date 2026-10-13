---
title: "Mô phỏng số cho kỹ sư"
description: "Loạt bài về việc tính ra những gì các phương trình dự đoán: rời rạc hóa (discretization) phương trình vi phân, sai phân hữu hạn (finite differences) cho bài toán truyền nhiệt và sóng, giải hệ phương trình tuyến tính cỡ lớn, phương pháp phần tử hữu hạn (finite element method), và kiểm tra để có thể tin cậy một mô phỏng."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Chuyển các phương trình đạo hàm riêng (partial differential equation) kèm điều kiện biên (boundary condition) thành các bài toán hữu hạn chiều."
  - "Phân tích độ chính xác và tính ổn định của các lược đồ sai phân hữu hạn hiển (explicit) và ẩn (implicit)."
  - "Lựa chọn phương pháp trực tiếp (direct) hoặc phương pháp lặp (iterative) cho các hệ tuyến tính cỡ lớn mà quá trình rời rạc hóa tạo ra."
  - "Giải thích phương pháp phần tử hữu hạn từ dạng biến phân (variational form) của nó, và kiểm chứng (verification) và thẩm định (validation) một mô phỏng."
---

Loạt bài này dành cho kỹ sư và sinh viên sử dụng kết quả mô phỏng và muốn biết các kết quả đó được tạo ra như thế nào và có thể tin cậy đến mức nào. Loạt bài giả định người đọc đã biết giải tích, đại số tuyến tính cơ bản và các phương trình vi phân thường đã gặp trong loạt bài về hệ thống điều khiển. Qua năm bài, loạt bài đi từ các phương trình truyền nhiệt, phương trình sóng, phương trình Poisson và điều kiện biên của chúng đến các lược đồ sai phân hữu hạn và tính ổn định của chúng; từ các hệ tuyến tính thưa (sparse) mà quá trình rời rạc hóa tạo ra đến các phương pháp giải trực tiếp và phương pháp lặp; từ dạng yếu (weak form) của một bài toán biên đến phần tử hữu hạn trong một và hai chiều; và cuối cùng đến kiểm chứng và thẩm định: đo bậc chính xác (order of accuracy) của một chương trình, ước lượng sai số số của một kết quả, và so sánh một mô hình với số liệu đo. Loạt bài kiểm tra các tốc độ hội tụ và giới hạn ổn định chính của mình bằng các thí nghiệm Python ngắn.
