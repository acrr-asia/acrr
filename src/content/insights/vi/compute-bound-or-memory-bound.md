---
title: "Giới hạn bởi tính toán hay bởi bộ nhớ? Ý tưởng roofline"
description: "Mô hình roofline kết hợp thông lượng số học và băng thông bộ nhớ thành một cận hiệu năng duy nhất như thế nào, và chỉ ra tài nguyên nào đáng để tối ưu."
publishedAt: 2026-10-05
kind: "Concept explanation"
tags:
  - performance
  - parallel computing
  - engineering
---

Trước khi tối ưu một nhân tính toán (kernel) số, nên biết tài nguyên nào đang giới hạn nó: khả năng tính toán số học của bộ xử lý hay việc đưa dữ liệu từ bộ nhớ đến. Công sức bỏ vào sai tài nguyên sẽ không thay đổi được gì. Ghi chú này giải thích mô hình roofline, một cận đơn giản trả lời câu hỏi đó từ hai thông số của máy và một tính chất của mã, và chỉ ra câu trả lời không còn đáng tin cậy từ đâu.

## Đã xác lập

Tốc độ của một kernel bị giới hạn hoặc bởi tốc độ bộ xử lý thực hiện phép tính số học, hoặc bởi tốc độ dữ liệu đến được bộ xử lý. **Mô hình roofline** (roofline model) của Williams, Waterman và Patterson (*Communications of the ACM*, vol. 52, no. 4, pp. 65–76, 2009) phát biểu điều này dưới dạng một cận trên: $P \le \min(P_{\mathrm{peak}},\, B\,I)$. Ở đây $P$ là hiệu năng có thể đạt được, $P_{\mathrm{peak}}$ là thông lượng số học đỉnh, $B$ là băng thông bộ nhớ duy trì được, và $I$ là **cường độ số học** (arithmetic intensity; bài báo gốc gọi là cường độ thao tác, operational intensity), tức số phép tính thực hiện trên mỗi byte được chuyển giữa bộ nhớ chính và bộ xử lý.

Hai giới hạn gặp nhau tại điểm gãy (ridge point) $I^* = P_{\mathrm{peak}}/B$. Dưới điểm này, một kernel không thể vượt quá giới hạn băng thông; trên điểm này, giới hạn số học có hiệu lực. Cận này không phải là một dự đoán: độ trễ, việc vector hóa kém hay sự mất cân bằng tải có thể giữ mã thực tế ở mức thấp hơn nhiều.

Xét một máy giả định có $P_{\mathrm{peak}} = 1000$ giga phép tính dấu phẩy động mỗi giây (GFLOP/s) và $B = 100$ gigabyte mỗi giây (GB/s), nên $I^* = 10$ phép tính dấu phẩy động (FLOP) trên mỗi byte. Phép cập nhật $y \leftarrow y + a x$ trên các vector độ chính xác kép (double precision) thực hiện 2 phép tính trên mỗi phần tử. Nếu mỗi toán hạng đi qua giao diện bộ nhớ đúng một lần (các vector lớn hơn nhiều so với bộ nhớ đệm, nên không có gì được dùng lại giữa các lượt quét), phép cập nhật chuyển 24 byte trên mỗi phần tử: đọc $x$, đọc $y$, ghi $y$. Khi đó $I = 2/24 \approx 0.083$ FLOP/byte và $B\,I \approx 8.3$ GFLOP/s, khoảng 1/120 giá trị đỉnh.

## Diễn giải

Mô hình này hoạt động như một công cụ phân loại ưu tiên: tính $I$, so sánh với $I^*$, rồi chọn nơi đầu tư công sức. Trong ví dụ trên, tăng gấp đôi thông lượng số học vẫn để cận ở mức 8.3 GFLOP/s, còn tăng gấp đôi băng thông thì cận tăng gấp đôi. Công sức vector hóa nhiều khả năng sẽ uổng phí; hướng hiệu quả là chuyển ít byte hơn, chẳng hạn bằng cách gộp các vòng lặp duyệt cùng một dữ liệu. Ngược lại, một kernel có $I$ cao hơn hẳn $I^*$ mà hiệu năng đo được lại thấp xa dưới "mái" gợi ý cần tìm nguyên nhân ngoài băng thông, chẳng hạn ở tổ hợp lệnh hay sự mất cân bằng tải, hoặc ở lưu lượng bộ nhớ lớn hơn số byte lý tưởng hóa.

Cường độ số học thuộc về thuật toán và cách bố trí dữ liệu chẳng kém gì thuộc về máy, và $I^*$ khác nhau giữa các máy, nên cùng một chương trình có thể bị giới hạn bởi bộ nhớ (memory-bound) trên máy này và bị giới hạn bởi tính toán (compute-bound) trên máy khác. Riêng số phép tính, chẳng hạn số flop được dùng để so sánh các bộ giải tuyến tính trong bài [Solving Large Linear Systems](/blog/solving-large-linear-systems#7-direct-or-iterative), chỉ chặn phía số học; roofline bổ sung phía dữ liệu, mà với ma trận thưa có ít phép tính trên mỗi phần tử được lưu thì đó thường là phía quyết định giới hạn.

## Câu hỏi còn mở

- Một con số đỉnh và một con số băng thông mô tả tốt đến đâu những máy có nhiều cấp bộ nhớ đệm, nhiều loại lệnh trộn lẫn, hoặc có bộ tăng tốc?
- Với truy cập không đều, chẳng hạn cấu trúc thưa hay cấu trúc dựa trên con trỏ, có thể định nghĩa $I$ mà không cần chạy mã hay không, khi số byte được chuyển phụ thuộc vào hành vi của bộ nhớ đệm và vào dữ liệu đầu vào?
- Nếu một kernel bị giới hạn bởi độ trễ bộ nhớ chứ không phải băng thông, cách phân loại này sẽ dẫn sai hướng. Làm thế nào để nhận ra trường hợp đó từ số liệu đo một cách ít tốn kém?
