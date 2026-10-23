---
title: "Học sâu Bayes"
description: "Độ bất định được hiệu chuẩn cho mạng nơ-ron: hậu nghiệm, lấy mẫu, Laplace, suy luận biến phân, tổ hợp mô hình, quá trình Gauss, tiên nghiệm và quy mô."
category: "AI and Machine Learning"
status: "in-progress"
objectives:
  - "Giải thích phân phối hậu nghiệm (posterior distribution) trên các tham số hoặc các hàm của mạng là gì, phân phối dự đoán hậu nghiệm (posterior predictive) được hình thành như thế nào, và độ bất định nhận thức (epistemic uncertainty) khác độ bất định ngẫu nhiên (aleatoric uncertainty) ra sao."
  - "So sánh các họ suy luận xấp xỉ (approximate inference) chính cho mạng nơ-ron (Monte Carlo xích Markov, xấp xỉ Laplace, suy luận biến phân và tổ hợp mô hình) theo giả định, chi phí và các kiểu thất bại của chúng."
  - "Liên hệ mạng nơ-ron với quá trình Gauss (Gaussian process) và các phương pháp hàm nhân (kernel method), và giải thích tiên nghiệm (prior), tính đối xứng (symmetry) và tính khả định danh (identifiability) định hình một mạng nơ-ron Bayes như thế nào."
  - "Chọn một phương pháp mở rộng được cho một mô hình và một tập dữ liệu cho trước, và đánh giá độ bất định dự đoán bằng hiệu chuẩn (calibration), quy tắc chấm điểm thích đáng (proper scoring rule) và dự đoán có chọn lọc (selective prediction)."
  - "Mô tả các hướng nghiên cứu hiện nay của học sâu Bayes và nêu các bài toán mở mà mỗi hướng giải quyết."
plannedEntries:
  - title: "Chương 12: Giới thiệu về suy luận biến phân"
  - title: "Chương 13: Suy luận biến phân trường trung bình Gauss"
  - title: "Chương 14: Suy luận biến phân dựa trên dropout"
  - title: "Chương 15: Suy luận biến phân dựa trên gradient tự nhiên"
  - title: "Chương 16: Suy luận biến phân dựa trên hạt"
  - title: "Chương 17: Suy luận biến phân trong không gian hàm"
  - title: "Chương 18: Suy luận biến phân tuần tự"
  - title: "Chương 19: Tổ hợp mô hình: giới thiệu và mối liên hệ với suy luận Bayes xấp xỉ"
  - title: "Chương 20: Các phương pháp lấy mẫu tổ hợp lai"
  - title: "Chương 21: Ứng dụng thực tế của tổ hợp sâu"
  - title: "Chương 22: Tổ hợp mạng nơ-ron sâu theo PAC-Bayes"
  - title: "Chương 23: Giới thiệu về các phương pháp hàm nhân"
  - title: "Chương 24: Học hàm nhân sâu"
  - title: "Chương 25: Quá trình Gauss sâu"
  - title: "Chương 26: Quá trình hàm nhân sâu và máy hàm nhân sâu"
  - title: "Chương 27: Học siêu cấp quá trình Gauss với hàm nhân sâu"
  - title: "Chương 28: Giới thiệu về tiên nghiệm"
  - title: "Chương 29: Các tính chất thống kê của tiên nghiệm"
  - title: "Chương 30: Tiên nghiệm có thông tin"
  - title: "Chương 31: Tiên nghiệm trong không gian hàm"
  - title: "Chương 32: Tính đối xứng trong mạng nơ-ron Bayes"
  - title: "Chương 33: Tính đối xứng và lấy mẫu"
  - title: "Chương 34: Học thiên hướng quy nạp và tính đối xứng"
  - title: "Chương 35: Mô hình sinh sâu diễn giải được và khả định danh qua kim tự tháp Bayes"
  - title: "Chương 36: Hỗn hợp chuyên gia Bayes trong học sâu Bayes"
  - title: "Chương 37: Học sâu Bayes mở rộng được bằng suy luận một lượt truyền xuôi"
  - title: "Chương 38: Quá trình Gauss mở rộng được"
  - title: "Chương 39: Suy luận lớp cuối"
  - title: "Chương 40: Xấp xỉ Laplace mở rộng được"
  - title: "Chương 41: Nén học được với mã tất định"
  - title: "Chương 42: Nén học được với mã ngẫu nhiên"
  - title: "Chương 43: Mô hình ngôn ngữ lớn Bayes"
  - title: "Chương 44: Phân loại có chọn lọc dựa trên độ tự tin"
  - title: "Chương 45: Điền khuyết dữ liệu y sinh"
  - title: "Chương 46: Mô hình hóa không gian – thời gian Bayes sâu cho cháy rừng"
  - title: "Chương 47: Phần mềm cho học sâu Bayes"
  - title: "Chương 48: Suy luận trong không gian con"
  - title: "Chương 49: Các quy tắc dự đoán Bayes ngầm định"
  - title: "Chương 50: Mô hình khuếch tán"
  - title: "Chương 51: Mạng khớp sẵn tiên nghiệm"
  - title: "Chương 52: Những tiến bộ của lý thuyết học kỳ dị cho học sâu Bayes"
  - title: "Chương 53: Học chủ động và thiết kế thí nghiệm"
  - title: "Chương 54: Học sâu Bayes có nhận biết nhân quả"
  - title: "Chương 55: Học sâu Bayes credal và xác suất không chính xác"
  - title: "Chương 56: Học tăng cường Bayes"

---

Loạt bài này dành cho người đọc đã từng huấn luyện mạng nơ-ron và muốn biết nên tin vào các dự đoán của chúng đến mức nào. Loạt bài giả định người đọc đã nắm nội dung của loạt bài [Cơ sở học máy](/vi/series/machine-learning-fundamentals) (rủi ro thực nghiệm, hạ gradient, chính quy hóa và đánh giá trung thực), xác suất cơ bản bao gồm định lý Bayes, và đại số tuyến tính ở mức trị riêng và ma trận xác định dương. Các ví dụ mã dùng Python 3.13 và chỉ NumPy 2.5.3, để mọi phép tính đều hiện rõ; mỗi đoạn mã ghi rõ hạt giống ngẫu nhiên (random seed) và kết quả thực của nó.

Loạt bài đăng toàn bộ bộ ghi chép hai tập về học sâu Bayes của ACRR: 56 chương của bộ ghi chép, chia thành mười phần, mỗi chương là một bài, với các dấu trích dẫn của bản gốc được lược bỏ và các hình vẽ được vẽ lại cho trang web. Mười bài tổng quan, được viết riêng cho trang web với các ví dụ NumPy của riêng chúng và các trích dẫn trực tiếp tài liệu gốc, giới thiệu loạt bài và từng phần. Bài tổng quan của một phần đứng trước, các chương của phần đó nối tiếp sau. Các chương chưa được đăng được liệt kê bên dưới dưới dạng dự kiến.

Bài thứ nhất trình bày bài toán mà mọi bài sau giải quyết: phân phối hậu nghiệm trên các tham số, phân phối dự đoán hậu nghiệm, và lý do không thể tính chính xác nó cho một mạng nơ-ron. Các phần I đến IV trình bày các họ suy luận xấp xỉ chính, theo thứ tự giảm dần về mức độ trực tiếp nhắm tới phân phối hậu nghiệm chính xác: các phương pháp lấy mẫu (phần I) rút mẫu từ chính phân phối hậu nghiệm, xấp xỉ Laplace (phần II) khớp một phân phối Gauss tại một mode, suy luận biến phân (phần III) tối ưu hóa phần tử tốt nhất của một họ phân phối dễ tính, và tổ hợp mô hình (ensemble, phần IV) kết hợp nhiều mode được huấn luyện độc lập.

Phần V chuyển góc nhìn từ trọng số sang hàm, thông qua hàm nhân và quá trình Gauss. Phần VI và VII hỏi một tiên nghiệm trên trọng số hoặc trên hàm của mạng nói lên điều gì, và tính đối xứng của một mạng làm cho các tham số của nó không khả định danh như thế nào. Phần VIII bàn về chi phí: các phương pháp đưa suy luận Bayes đến các mô hình lớn, chẳng hạn suy luận lớp cuối (last-layer inference) và các phương pháp một lượt truyền xuôi (single-forward-pass method). Phần IX chuyển sang thực hành: độ bất định dự đoán được đánh giá và sử dụng như thế nào, trong các mô hình ngôn ngữ lớn, phân loại có chọn lọc và các ứng dụng khoa học, và phần mềm nào hỗ trợ việc đó. Phần X điểm qua các hướng nghiên cứu hiện nay.

Các bài tổng quan dùng chung một hệ ký hiệu; các chương giữ ký hiệu của bản gốc, mỗi chương định nghĩa ký hiệu tại chỗ sử dụng. $\theta$ ký hiệu các tham số, $\mathcal{D} = \{(x_n, y_n)\}_{n=1}^N$ là dữ liệu huấn luyện, $p(\theta)$ là tiên nghiệm, $p(\mathcal{D} \mid \theta)$ là hàm hợp lý (likelihood) và $p(\theta \mid \mathcal{D})$ là phân phối hậu nghiệm; $x^*$ và $y^*$ là một đầu vào kiểm tra và đầu ra của nó. $P$ là số tham số, $C$ là số lớp và $\sigma$ là độ lệch chuẩn của nhiễu quan sát Gauss. Một tiên nghiệm Gauss trên mỗi trọng số có độ lệch chuẩn $s_0$ (hoặc độ chính xác (precision) $\alpha = 1/s_0^2$ khi cách viết đó rõ hơn), $M$ là số mẫu Monte Carlo và $J$ là số thành viên của tổ hợp.
