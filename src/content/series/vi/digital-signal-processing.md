---
title: "Xử lý tín hiệu số cho kỹ sư"
description: "Loạt bài dự kiến về xử lý tín hiệu đã lấy mẫu: tín hiệu và hệ thống thời gian rời rạc (discrete-time signals and systems), biến đổi z (z-transform), phân tích tần số bằng DFT và FFT, thiết kế bộ lọc số (digital filter), và bước chuyển từ xử lý tín hiệu sang điều khiển số (digital control)."
category: "Mathematical Foundations"
status: "planned"
objectives:
  - "Mô tả tín hiệu thời gian rời rạc và hệ thống tuyến tính bất biến theo thời gian (linear time-invariant system) bằng phương trình sai phân (difference equation), đáp ứng xung (impulse response) và tích chập (convolution)."
  - "Dùng biến đổi z để phân tích tính ổn định và đáp ứng tần số (frequency response)."
  - "Tính toán và diễn giải phổ bằng DFT và FFT, bao gồm hiện tượng rò rỉ phổ (leakage) và việc dùng hàm cửa sổ (windowing)."
  - "Thiết kế bộ lọc FIR và IIR theo một đặc tả cho trước và hiện thực chúng trong giới hạn của phần cứng."
plannedEntries:
  - title: "Tín hiệu và hệ thống trong miền thời gian rời rạc"
    description: "Dãy, phương trình sai phân, đáp ứng xung, tích chập và những tính chất giúp hệ thống tuyến tính bất biến theo thời gian trở nên dễ phân tích."
  - title: "Biến đổi z, điểm cực và tính ổn định"
    description: "Từ phương trình sai phân đến hàm truyền (transfer function), đồ thị điểm cực – điểm không (pole-zero plot) và tính ổn định vào bị chặn – ra bị chặn (bounded-input bounded-output stability)."
  - title: "Phổ: DFT và FFT"
    description: "Biến đổi Fourier rời rạc (discrete Fourier transform) tính ra điều gì, vì sao FFT nhanh, và rò rỉ phổ cùng hàm cửa sổ ảnh hưởng thế nào đến một phổ đo được."
  - title: "Thiết kế bộ lọc FIR và IIR"
    description: "Các phương pháp thiết kế bằng hàm cửa sổ và bằng biến đổi song tuyến tính (bilinear transform), pha tuyến tính (linear phase), và ảnh hưởng của độ dài từ hữu hạn (finite word length)."
  - title: "Từ xử lý tín hiệu đến điều khiển số"
    description: "Rời rạc hóa một bộ điều khiển, lựa chọn tốc độ lấy mẫu, và vì sao một vòng điều khiển là một hệ thống xử lý tín hiệu có phản hồi."
---

Loạt bài này đang được lên kế hoạch và chưa bắt đầu xuất bản. Loạt bài giả định người đọc đã biết giải tích, số phức và đại số tuyến tính cơ bản. Đề cương dưới đây mô tả phạm vi dự kiến và có thể thay đổi trước khi bất kỳ bài nào được viết.
