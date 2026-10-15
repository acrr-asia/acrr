---
title: "Xử lý tín hiệu số cho kỹ sư"
description: "Cách phân tích tín hiệu và hệ thống đã lấy mẫu bằng biến đổi z và DFT, thiết kế bộ lọc số và đưa cùng những công cụ đó vào điều khiển số."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Mô tả tín hiệu thời gian rời rạc (discrete-time signal) và hệ thống tuyến tính bất biến theo thời gian (linear time-invariant system) bằng phương trình sai phân (difference equation), đáp ứng xung (impulse response) và tích chập (convolution)."
  - "Dùng biến đổi z (z-transform) để phân tích tính ổn định và đáp ứng tần số (frequency response)."
  - "Tính toán và diễn giải phổ bằng DFT và FFT, bao gồm hiện tượng rò rỉ phổ (leakage) và việc dùng hàm cửa sổ (windowing)."
  - "Thiết kế bộ lọc FIR và IIR theo một đặc tả cho trước và hiện thực chúng trong giới hạn của phần cứng."
  - "Xem một vòng điều khiển số như một hệ thống xử lý tín hiệu: rời rạc hóa (discretize) đối tượng điều khiển (plant) và bộ điều khiển, và tính đến thời gian trễ (delay) do lấy mẫu, giữ mẫu và lọc gây ra khi chọn tốc độ lấy mẫu."
---

Loạt bài này dành cho các kỹ sư làm việc với tín hiệu đã lấy mẫu và muốn nắm được phần lý thuyết giúp họ suy luận về những gì mã chương trình của mình làm với các tín hiệu đó. Loạt bài giả định người đọc đã biết giải tích, số phức và đại số tuyến tính cơ bản, cùng với khái niệm lấy mẫu (sampling) được bài [Lấy mẫu, lượng tử hóa và chuyển đổi dữ liệu](/vi/blog/sampling-quantization-and-data-conversion) giới thiệu trong loạt bài [Hệ thống cảm biến](/vi/series/sensor-systems). Bài 2, 4 và 5 còn dùng biến đổi Laplace và các điểm cực (pole) trong mặt phẳng $s$, và bài thứ năm dùng thêm từ vựng của phản hồi (feedback); bài [Nhập môn hệ thống điều khiển](/vi/blog/introduction-to-control-systems) giới thiệu cả hai. Các ví dụ tính toán dùng Python 3 với NumPy.

Năm bài được sắp xếp sao cho mỗi bài dùng các công cụ của bài trước. Bài thứ nhất xây dựng tín hiệu thời gian rời rạc và hệ thống tuyến tính bất biến theo thời gian (LTI) từ những nguyên lý cơ bản, trong miền thời gian: phương trình sai phân, đáp ứng xung và tích chập. Bài thứ hai giới thiệu biến đổi z, công cụ thay các tổng trong miền thời gian đó bằng phép tính đại số và đọc ra tính ổn định cùng đáp ứng tần số từ vị trí của các điểm cực và điểm không (zero). Bài thứ ba chuyển từ hệ thống sang tín hiệu và đo phổ bằng biến đổi Fourier rời rạc (discrete Fourier transform, DFT) và biến đổi Fourier nhanh (fast Fourier transform, FFT). Bài thứ tư kết hợp cả ba để thiết kế bộ lọc đáp ứng xung hữu hạn và vô hạn (FIR và IIR) trong giới hạn của độ dài từ hữu hạn (finite word length). Bài thứ năm đặt một bộ lọc số vào trong một vòng phản hồi để làm bộ điều khiển số (digital controller) và xem toàn bộ vòng như một hệ thống xử lý tín hiệu.

Mọi bài dùng chung các quy ước của bài thứ nhất: bảng ký hiệu của nó (tần số tính bằng radian trên mẫu), quy ước dấu cho phương trình sai phân, và giả thiết rằng hệ thống bắt đầu ở trạng thái nghỉ.
