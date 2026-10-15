---
title: "Cơ sở học máy"
description: "Bốn bài xây dựng học có giám sát từ nguyên lý cơ bản: bài toán học, hạ gradient, quá khớp và chính quy hóa, và cách đánh giá mô hình một cách trung thực."
category: "AI and Machine Learning"
status: "published"
objectives:
  - "Phát biểu một bài toán học có giám sát (supervised learning) dưới dạng một mô hình, một hàm mất mát (loss function) và một tập dữ liệu."
  - "Giải thích tối ưu hóa dựa trên gradient (gradient-based optimization) và vai trò của tốc độ học (learning rate)."
  - "Phân biệt sai số huấn luyện (training error) với sai số tổng quát hóa (generalization error), và giải thích vì sao việc đánh giá trên dữ liệu được giữ riêng (held-out evaluation) lại quan trọng."
  - "Nhận diện các nguồn rò rỉ dữ liệu (data leakage) và thiên lệch (bias) thường gặp trong một thiết lập đánh giá."
---

Loạt bài này dành cho người đọc biết lập trình và đã quen với đạo hàm, vector và ma trận, cùng các khái niệm cơ bản của xác suất (kỳ vọng, phương sai, phân phối chuẩn). Mỗi bài nhắc lại mọi ý tưởng bổ sung mà nó cần, chẳng hạn trị riêng, ma trận hiệp phương sai (covariance matrix) hay một bất đẳng thức tập trung (concentration inequality), tại chỗ ý tưởng đó được dùng lần đầu.

Bốn bài đi theo các câu hỏi mà một bài toán học đặt ra, theo đúng thứ tự chúng xuất hiện. Bài thứ nhất, *Learning from Data* (Học từ dữ liệu), phát biểu bài toán: một mô hình, một hàm mất mát và một tập dữ liệu, với rủi ro (risk) là đại lượng cần làm cho nhỏ và sai số huấn luyện là một ước lượng lạc quan của nó. Bài thứ hai, *Gradient Descent and Its Variants* (Hạ gradient và các biến thể), trả lời câu hỏi sai số huấn luyện được cực tiểu hóa như thế nào khi không có nghiệm dạng đóng, và vì sao tốc độ học quyết định phép lặp có hội tụ hay không. Bài thứ ba, *Generalization, Overfitting, and Regularization* (Tổng quát hóa, quá khớp và chính quy hóa), hỏi sai số huấn luyện đã được cực tiểu hóa có thể lệch xa rủi ro đến mức nào khi mô hình ngày càng linh hoạt, và các hàm phạt (penalty) cùng việc dừng sớm (early stopping) hạn chế độ lệch đó ra sao. Bài thứ tư, *Evaluating Models Honestly* (Đánh giá mô hình một cách trung thực), chỉ ra cách ước lượng rủi ro từ dữ liệu hữu hạn mà không tự đánh lừa mình: tập kiểm định (validation set) và tập kiểm tra (test set), kiểm định chéo (cross-validation), rò rỉ dữ liệu, thiên lệch trong thiết lập đánh giá, và báo cáo kết quả kèm độ bất định (uncertainty).

Mọi bài dùng chung một số quy ước. Các ví dụ được viết bằng Python 3 với NumPy, và các kết quả được trích dẫn được tạo ra bằng Python 3.13 và NumPy 2.5.3. Mọi tập dữ liệu đều là dữ liệu tổng hợp (synthetic data), được sinh với một hạt giống (seed) được nêu rõ, nên quan hệ thực và sai số không thể giảm (irreducible error) được biết trước và mỗi con số đều có thể tái lập với phiên bản NumPy đã nêu (các phiên bản khác có thể sinh ra các dãy ngẫu nhiên khác). Sai số bình phương trung bình (mean squared error) là trung bình thông thường của các bình phương sai số (không có hệ số một nửa), các lớp trong phân loại nhị phân được mã hóa là 0 và 1, và các mục được đánh số để các bài sau có thể dẫn chiếu.
