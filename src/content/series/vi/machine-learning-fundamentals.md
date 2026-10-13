---
title: "Cơ sở học máy"
description: "Loạt bài về các ý tưởng cốt lõi của việc học từ dữ liệu: mô hình, hàm mất mát (loss function), tối ưu hóa (optimization), và cách đánh giá những gì một mô hình đã học được."
category: "AI and Machine Learning"
status: "published"
objectives:
  - "Phát biểu một bài toán học có giám sát (supervised learning) dưới dạng một mô hình, một hàm mất mát và một tập dữ liệu."
  - "Giải thích tối ưu hóa dựa trên gradient (gradient-based optimization) và vai trò của tốc độ học (learning rate)."
  - "Phân biệt sai số huấn luyện (training error) với sai số tổng quát hóa (generalization error), và giải thích vì sao việc đánh giá trên dữ liệu được giữ riêng (held-out evaluation) lại quan trọng."
  - "Nhận diện các nguồn rò rỉ dữ liệu (data leakage) và thiên lệch (bias) thường gặp trong một thiết lập đánh giá."
---

Loạt bài này dành cho người đọc biết lập trình và đã quen với đạo hàm, vector và ma trận, cùng các khái niệm cơ bản của xác suất (kỳ vọng, phương sai, phân phối chuẩn). Loạt bài xây dựng học có giám sát từ các nguyên lý cơ bản: bài toán học như việc cực tiểu hóa mất mát trên các mẫu, hạ gradient (gradient descent) và các biến thể ngẫu nhiên (stochastic) của nó, vì sao các mô hình linh hoạt bị quá khớp (overfitting) và chính quy hóa (regularization) hạn chế điều đó ra sao, và cách đánh giá một mô hình một cách trung thực, tránh rò rỉ dữ liệu và báo cáo kết quả kèm theo độ bất định (uncertainty) của chúng. Mọi ví dụ đều dùng các tập dữ liệu tổng hợp (synthetic data) nhỏ bằng Python với numpy, để đáp án đúng được biết trước và mỗi con số đều có thể tái lập.
