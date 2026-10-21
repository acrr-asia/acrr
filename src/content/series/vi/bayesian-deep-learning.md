---
title: "Học sâu Bayes"
description: "Mang lại độ bất định được hiệu chỉnh cho mạng nơ-ron: phân phối hậu nghiệm, lấy mẫu, Laplace, suy luận biến phân, tổ hợp mô hình, quá trình Gauss, tiên nghiệm và mở rộng quy mô."
category: "AI and Machine Learning"
status: "published"
objectives:
  - "Giải thích phân phối hậu nghiệm (posterior distribution) trên các tham số hoặc các hàm của mạng là gì, phân phối dự đoán hậu nghiệm (posterior predictive) được hình thành như thế nào, và độ bất định nhận thức (epistemic uncertainty) khác độ bất định ngẫu nhiên (aleatoric uncertainty) ra sao."
  - "So sánh các họ suy luận xấp xỉ (approximate inference) chính cho mạng nơ-ron (xích Markov Monte Carlo, xấp xỉ Laplace, suy luận biến phân và tổ hợp mô hình) theo giả định, chi phí và các kiểu thất bại của chúng."
  - "Liên hệ mạng nơ-ron với quá trình Gauss (Gaussian process) và các phương pháp nhân (kernel method), và giải thích tiên nghiệm (prior), tính đối xứng (symmetry) và tính khả định danh (identifiability) định hình một mạng nơ-ron Bayes như thế nào."
  - "Chọn một phương pháp mở rộng được cho một mô hình và một tập dữ liệu cho trước, và đánh giá độ bất định dự đoán bằng độ hiệu chỉnh (calibration), quy tắc chấm điểm thích đáng (proper scoring rule) và dự đoán có chọn lọc (selective prediction)."
  - "Mô tả các hướng nghiên cứu hiện nay của học sâu Bayes và nêu các bài toán mở mà mỗi hướng giải quyết."
---

Loạt bài này dành cho người đọc đã từng huấn luyện mạng nơ-ron và muốn biết nên tin vào các dự đoán của chúng đến mức nào. Loạt bài giả định người đọc đã nắm nội dung của loạt bài [Cơ sở học máy](/vi/series/machine-learning-fundamentals) (rủi ro thực nghiệm, hạ gradient, chính quy hóa và đánh giá trung thực), xác suất cơ bản bao gồm định lý Bayes, và đại số tuyến tính ở mức trị riêng và ma trận xác định dương. Các ví dụ mã dùng Python 3.13 và chỉ NumPy 2.5.3, để mọi phép tính đều hiện rõ; mỗi đoạn mã ghi rõ hạt giống ngẫu nhiên (random seed) và kết quả thực của nó.

Các chủ đề và thứ tự của chúng đi theo một bộ ghi chép hai tập về học sâu Bayes do ACRR biên soạn. Các bài cô đọng tài liệu đó cho trang web; văn bản, ví dụ và hình vẽ của chúng được viết riêng cho loạt bài này, và chúng trích dẫn trực tiếp các tài liệu gốc.

Bài thứ nhất trình bày bài toán mà mọi bài sau giải quyết: phân phối hậu nghiệm trên các tham số, phân phối dự đoán hậu nghiệm, và lý do không thể tính chính xác nó cho một mạng nơ-ron. Bốn bài tiếp theo trình bày các họ suy luận xấp xỉ chính, theo thứ tự giảm dần về mức độ trực tiếp nhắm tới phân phối hậu nghiệm chính xác: các phương pháp lấy mẫu rút mẫu từ chính phân phối hậu nghiệm, xấp xỉ Laplace khớp một phân phối Gauss tại một mode, suy luận biến phân tối ưu hóa phần tử tốt nhất của một họ phân phối dễ tính, và tổ hợp mô hình (ensemble) kết hợp nhiều mode được huấn luyện độc lập.

Bài thứ sáu chuyển góc nhìn từ trọng số sang hàm, thông qua hàm nhân và quá trình Gauss. Bài thứ bảy hỏi một tiên nghiệm trên trọng số hoặc trên hàm của mạng nói lên điều gì, và tính đối xứng của một mạng làm cho các tham số của nó không khả định danh như thế nào. Bài thứ tám bàn về chi phí: các phương pháp đưa suy luận Bayes đến các mô hình lớn, chẳng hạn suy luận ở lớp cuối (last-layer inference) và các phương pháp chỉ cần một lượt truyền xuôi (single-forward-pass method). Bài thứ chín chuyển sang thực hành: độ bất định dự đoán được đánh giá và sử dụng như thế nào, trong phân loại có chọn lọc, học chủ động và các mô hình ngôn ngữ lớn. Bài cuối cùng điểm qua các hướng nghiên cứu hiện nay.

Ký hiệu được dùng chung trong toàn loạt bài. $\theta$ ký hiệu các tham số, $\mathcal{D} = \{(x_n, y_n)\}_{n=1}^N$ là dữ liệu huấn luyện, $p(\theta)$ là tiên nghiệm, $p(\mathcal{D} \mid \theta)$ là hàm hợp lý (likelihood) và $p(\theta \mid \mathcal{D})$ là phân phối hậu nghiệm; $x^*$ và $y^*$ là một đầu vào kiểm tra và đầu ra của nó. $P$ là số tham số, $C$ là số lớp và $\sigma$ là độ lệch chuẩn của nhiễu quan sát Gauss. Một tiên nghiệm Gauss trên mỗi trọng số có độ lệch chuẩn $s_0$ (hoặc độ chính xác (precision) $\alpha = 1/s_0^2$ khi cách viết đó rõ hơn), $M$ là số mẫu Monte Carlo và $J$ là số thành viên của tổ hợp.
