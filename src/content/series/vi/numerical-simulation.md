---
title: "Mô phỏng số cho kỹ sư"
description: "Loạt bài dự kiến về việc tính ra những gì các phương trình dự đoán: rời rạc hóa (discretisation) phương trình vi phân, sai phân hữu hạn (finite differences) cho bài toán truyền nhiệt và sóng, giải hệ phương trình tuyến tính cỡ lớn, phương pháp phần tử hữu hạn (finite element method), và kiểm tra để có thể tin cậy một mô phỏng."
category: "Mathematical Foundations"
status: "planned"
objectives:
  - "Chuyển các phương trình đạo hàm riêng (partial differential equation) kèm điều kiện biên (boundary condition) thành các bài toán hữu hạn chiều."
  - "Phân tích độ chính xác và tính ổn định của các lược đồ sai phân hữu hạn hiện (explicit) và ẩn (implicit)."
  - "Lựa chọn phương pháp trực tiếp (direct) hoặc phương pháp lặp (iterative) cho các hệ tuyến tính cỡ lớn mà quá trình rời rạc hóa tạo ra."
  - "Giải thích phương pháp phần tử hữu hạn từ dạng biến phân (variational form) của nó, và kiểm chứng (verification) và thẩm định (validation) một mô phỏng."
plannedEntries:
  - title: "Từ phương trình vi phân đến bài toán rời rạc"
    description: "Các phương trình truyền nhiệt, sóng và trường, điều kiện biên, và ý tưởng rời rạc hóa."
  - title: "Sai phân hữu hạn cho bài toán truyền nhiệt và sóng"
    description: "Các lược đồ hiện, ẩn và Crank-Nicolson, và cách phân tích độ chính xác và tính ổn định."
  - title: "Giải hệ phương trình tuyến tính cỡ lớn"
    description: "Phép khử Gauss (Gaussian elimination) và phân tích Cholesky (Cholesky factorisation), cùng các phương pháp lặp từ Jacobi đến gradient liên hợp (conjugate gradients)."
  - title: "Phương pháp phần tử hữu hạn"
    description: "Dạng yếu (weak form), phương pháp Galerkin, phần tử và lưới (mesh), từ một chiều đến hai chiều."
  - title: "Kiểm chứng và thẩm định một mô phỏng"
    description: "Nghiên cứu hội tụ (convergence study), so sánh với các nghiệm đã biết và với thí nghiệm, và báo cáo các giới hạn của một mô hình."
---

Loạt bài này đang được lên kế hoạch và chưa bắt đầu xuất bản. Loạt bài giả định người đọc đã biết giải tích, đại số tuyến tính cơ bản và các phương trình vi phân thường đã gặp trong loạt bài về hệ thống điều khiển. Đề cương dưới đây mô tả phạm vi dự kiến và có thể thay đổi trước khi bất kỳ bài nào được viết.
