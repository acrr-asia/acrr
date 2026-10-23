---
title: "Học máy từ nền tảng"
description: "Ba mươi bài xây dựng học máy cổ điển từ đại số tuyến tính và xác suất đến hồi quy, mạng nơ-ron, hệ gợi ý, PCA, tối ưu lồi và máy vector hỗ trợ."
category: "AI and Machine Learning"
status: "in-progress"
objectives:
  - "Sử dụng đại số tuyến tính, giải tích ma trận và xác suất làm nền cho học máy cổ điển, và ước lượng tham số mô hình bằng hợp lý cực đại (maximum likelihood) và hậu nghiệm cực đại (maximum a posteriori)."
  - "Xây dựng, huấn luyện và đánh giá các mô hình hồi quy, K lân cận, phân cụm, naive Bayes, perceptron, hồi quy logistic và softmax, và mạng nơ-ron đa tầng huấn luyện bằng lan truyền ngược (backpropagation)."
  - "Xây dựng hệ thống gợi ý dựa trên nội dung và lọc cộng tác (collaborative filtering), và giảm chiều dữ liệu bằng phân tích giá trị suy biến, phân tích thành phần chính và phân tích biệt thức tuyến tính."
  - "Nhận biết tập lồi, hàm lồi và bài toán tối ưu lồi, suy ra bài toán đối ngẫu Lagrange và điều kiện Karush-Kuhn-Tucker, và áp dụng chúng cho máy vector hỗ trợ lề cứng, lề mềm, hạt nhân và đa lớp."
plannedEntries:
  - title: "K lân cận"
  - title: "Phân cụm K-means"
  - title: "Bộ phân loại naive Bayes"
  - title: "Gradient descent"
  - title: "Thuật toán học perceptron"
  - title: "Hồi quy logistic"
  - title: "Hồi quy softmax"
  - title: "Mạng nơ-ron đa tầng và lan truyền ngược"
  - title: "Hệ thống gợi ý dựa trên nội dung"
  - title: "Lọc cộng tác dựa trên lân cận"
  - title: "Lọc cộng tác bằng phân tích ma trận"
  - title: "Phân tích giá trị suy biến"
  - title: "Phân tích thành phần chính"
  - title: "Phân tích biệt thức tuyến tính"
  - title: "Tập lồi và hàm lồi"
  - title: "Bài toán tối ưu lồi"
  - title: "Đối ngẫu Lagrange"
  - title: "Máy vector hỗ trợ"
  - title: "Máy vector hỗ trợ lề mềm"
  - title: "Máy vector hỗ trợ hạt nhân"
  - title: "Máy vector hỗ trợ đa lớp"
  - title: "Phương pháp nhân tử Lagrange"
---

Loạt bài này được viết bằng tiếng Việt trước và được đăng dần theo từng phần; bản tiếng Anh của các bài đang ở trạng thái dự kiến.

Ba mươi bài được chia thành tám phần. Phần I (bài 1 đến 4) ôn tập đại số tuyến tính, giải tích ma trận và xác suất, và giới thiệu ước lượng hợp lý cực đại và hậu nghiệm cực đại. Phần II (bài 5 đến 8) trình bày các khái niệm cơ bản của học máy, xây dựng đặc trưng, hồi quy tuyến tính và quá khớp. Phần III (bài 9 đến 11) giới thiệu ba phương pháp đơn giản: K lân cận, phân cụm K-means và bộ phân loại naive Bayes. Phần IV (bài 12 đến 16) đi từ gradient descent qua perceptron, hồi quy logistic và hồi quy softmax đến mạng nơ-ron đa tầng và lan truyền ngược. Phần V (bài 17 đến 19) xây dựng hệ thống gợi ý. Phần VI (bài 20 đến 22) trình bày giảm chiều dữ liệu bằng phân tích giá trị suy biến, phân tích thành phần chính và phân tích biệt thức tuyến tính. Phần VII (bài 23 đến 25) giới thiệu tập lồi, hàm lồi, bài toán tối ưu lồi và đối ngẫu Lagrange, và Phần VIII (bài 26 đến 29) áp dụng chúng cho máy vector hỗ trợ. Bài 30 trình bày phương pháp nhân tử Lagrange mà nhiều bài trước sử dụng.

Nội dung loạt bài được chuyển thể sát văn bản của cuốn *Machine Learning cơ bản*: mỗi bài là một chương của sách (bài 30 là Phụ lục A), giữ nguyên số hiệu mục và công thức, và ghi rõ nguồn ở đầu bài. Các hình minh họa của sách không được đưa vào; chú thích của chúng được giữ lại.
