---
title: "Mô phỏng số cho kỹ sư"
description: "Năm bài về cách tính ra những gì phương trình vi phân dự đoán, từ rời rạc hóa và sai phân hữu hạn đến bộ giải tuyến tính, phần tử hữu hạn và kiểm chứng."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Rời rạc hóa (discretize) một phương trình đạo hàm riêng (partial differential equation) cùng các điều kiện biên (boundary condition) và điều kiện ban đầu (initial condition) của nó thành một bài toán đại số hữu hạn, và nêu bậc chính xác (order of accuracy) của kết quả."
  - "Phân tích độ chính xác và tính ổn định của các lược đồ sai phân hữu hạn (finite-difference scheme) hiển (explicit) và ẩn (implicit), và chọn bước thời gian tương ứng."
  - "Lựa chọn phương pháp trực tiếp (direct) hoặc phương pháp lặp (iterative) cho các hệ tuyến tính thưa (sparse) cỡ lớn mà quá trình rời rạc hóa tạo ra, và dự đoán chi phí tính toán của phương pháp đó."
  - "Xây dựng phương pháp phần tử hữu hạn (finite element method) từ dạng yếu (weak form) của một bài toán biên, và giải thích sai số của nó phụ thuộc vào kích thước lưới (mesh size) và bậc phần tử như thế nào."
  - "Kiểm chứng (verify) một chương trình mô phỏng và kết quả của nó bằng cách đo bậc chính xác quan sát được và ước lượng sai số số, và thẩm định (validate) một mô hình so với số liệu đo có độ không đảm bảo được nêu rõ."
---

Loạt bài này dành cho kỹ sư và sinh viên sử dụng kết quả mô phỏng và muốn biết các kết quả đó được tạo ra như thế nào và có thể tin cậy đến mức nào. Loạt bài giả định người đọc đã biết giải tích, đại số tuyến tính cơ bản và các phương trình vi phân thường (ordinary differential equation, ODE) của loạt bài [Cơ sở hệ thống điều khiển](/vi/series/foundations-of-control-systems); bài [Ghi chú về tích phân số phương trình vi phân thường](/vi/blog/numerical-integration-notes) là kiến thức nền hữu ích cho việc bước theo thời gian (time stepping) ở bài thứ hai.

Năm bài theo một mô phỏng từ các phương trình của nó đến một kết quả có thể bảo vệ được, và mỗi bài cung cấp những gì bài tiếp theo cần. Bài thứ nhất giới thiệu phương trình truyền nhiệt, phương trình sóng và phương trình Poisson, biến một phương trình vi phân thành một tập hữu hạn các phương trình đại số, và định nghĩa từ vựng về sai số. Bài thứ hai thêm thời gian vào và chỉ ra rằng việc chọn giữa lược đồ hiển và lược đồ ẩn được quyết định bởi tính ổn định. Cả hai loại bài toán đều dẫn đến các hệ tuyến tính thưa cỡ lớn, mà bài thứ ba giải bằng phương pháp trực tiếp và phương pháp lặp. Bài thứ tư xây dựng cùng loại hệ đó theo một cách thứ hai, từ dạng yếu của phương trình, để lưới có thể bám theo mọi hình dạng. Bài thứ năm hỏi kết quả của toàn bộ chuỗi này có thể tin cậy đến mức nào: nó kiểm chứng chương trình và lời giải, và thẩm định mô hình so với số liệu đo.

Mọi bài dùng chung một vài quy ước. Phương trình Poisson được viết là $-\nabla^2 u = f$, để các ma trận mà nó tạo ra là xác định dương; chữ hoa $U$ ký hiệu một nghiệm xấp xỉ rời rạc và chữ thường $u$ ký hiệu nghiệm chính xác; các đại lượng tính theo đơn vị SI. Mã dùng Python 3 với NumPy ở độ chính xác kép (double precision), và các tốc độ hội tụ cùng giới hạn ổn định chính được kiểm tra bằng các thí nghiệm ngắn có hiển thị kết quả in ra.
