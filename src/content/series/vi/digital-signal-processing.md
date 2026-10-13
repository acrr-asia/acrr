---
title: "Xử lý tín hiệu số cho kỹ sư"
description: "Loạt bài về xử lý tín hiệu đã lấy mẫu: tín hiệu và hệ thống thời gian rời rạc (discrete-time signals and systems), biến đổi z (z-transform), phân tích tần số bằng DFT và FFT, thiết kế bộ lọc số (digital filter), và bước chuyển từ xử lý tín hiệu sang điều khiển số (digital control)."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Mô tả tín hiệu thời gian rời rạc và hệ thống tuyến tính bất biến theo thời gian (linear time-invariant system) bằng phương trình sai phân (difference equation), đáp ứng xung (impulse response) và tích chập (convolution)."
  - "Dùng biến đổi z để phân tích tính ổn định và đáp ứng tần số (frequency response)."
  - "Tính toán và diễn giải phổ bằng DFT và FFT, bao gồm hiện tượng rò rỉ phổ (leakage) và việc dùng hàm cửa sổ (windowing)."
  - "Thiết kế bộ lọc FIR và IIR theo một đặc tả cho trước và hiện thực chúng trong giới hạn của phần cứng."
---

Loạt bài này dành cho các kỹ sư làm việc với tín hiệu đã lấy mẫu và muốn nắm được phần lý thuyết giúp họ suy luận về những gì mã chương trình của mình làm với các tín hiệu đó. Loạt bài giả định người đọc đã biết giải tích, số phức và đại số tuyến tính cơ bản, cùng với khái niệm lấy mẫu (sampling) được giới thiệu trong loạt bài về cảm biến; các ví dụ tính toán dùng Python 3 với NumPy. Qua năm bài, loạt bài xây dựng tín hiệu thời gian rời rạc và hệ thống tuyến tính bất biến theo thời gian từ những nguyên lý cơ bản, phân tích chúng bằng biến đổi z, đo phổ bằng DFT và FFT, thiết kế bộ lọc FIR và IIR trong giới hạn của độ dài từ hữu hạn (finite word length), và kết thúc bằng việc đặt một bộ lọc số vào trong một vòng phản hồi (feedback loop) để nó làm nhiệm vụ của một bộ điều khiển số.
