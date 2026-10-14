---
title: "Sai số làm tròn dấu phẩy động trong các mô phỏng dài"
description: "Một ghi chú phương pháp ngắn về việc độ chính xác hữu hạn, thứ tự cộng dồn và sai số làm tròn tích lũy có thể ảnh hưởng thế nào đến các mô phỏng chạy qua rất nhiều bước."
publishedAt: 2026-10-07
kind: "Methodological note"
tags:
  - numerical methods
  - simulation
  - verification
---

## Đã xác lập

Máy tính lưu số thực với độ chính xác hữu hạn, nên phần lớn kết quả số học đều bị làm tròn. Trong số học dấu phẩy động (floating point) IEEE 754 với chế độ làm tròn về giá trị gần nhất, đơn vị làm tròn (unit roundoff) $u$ bằng $2^{-24} \approx 6\times10^{-8}$ đối với binary32 ("độ chính xác đơn") và $2^{-53} \approx 1.1\times10^{-16}$ đối với binary64 ("độ chính xác kép"). Mỗi phép toán cơ bản trả về kết quả được làm tròn đúng, nên sai số tương đối của nó không vượt quá $u$, trừ khi xảy ra tràn trên hoặc tràn dưới.

Phép cộng dấu phẩy động có tính giao hoán nhưng không có tính kết hợp: $(a+b)+c$ và $a+(b+c)$ có thể khác nhau. Ở độ chính xác kép, $(10^{16}+1)+1$ cho kết quả $10^{16}$, trong khi $10^{16}+(1+1)$ cho $10^{16}+2$. Vì vậy thứ tự cộng dồn có thể làm thay đổi kết quả, và một phép rút gọn song song (parallel reduction) có thứ tự thay đổi giữa các lần chạy có thể khiến kết quả khác nhau giữa các lần chạy.

Sai số làm tròn tích lũy dần. Với phép cộng dồn đệ quy thông thường gồm $n$ số hạng, cận sai số trong trường hợp xấu nhất theo chuẩn mực là khoảng $n\,u$ nhân với tổng các giá trị tuyệt đối của các số hạng. Với một trường hợp giả định gồm $10^6$ số hạng, $n\,u$ vào khoảng $0.06$ ở độ chính xác đơn và khoảng $10^{-10}$ ở độ chính xác kép. Đây là các cận, và sai số thực tế thường nhỏ hơn nhiều. Một bộ đếm độ chính xác đơn được tăng mỗi lần thêm 1 sẽ ngừng thay đổi tại $2^{24} = 16777216$.

## Diễn giải

Một cách hiểu là: trong một lần chạy ngắn, làm tròn thường chỉ là nguồn sai số thứ yếu, nhưng đáng được kiểm tra khi số phép tính tăng lên. Việc kiểm tra có vẻ cần thiết nhất khi lần chạy rất dài, khi kết quả là một hiệu nhỏ giữa các đại lượng lớn, khi hệ khuếch đại các nhiễu loạn nhỏ (như các hệ hỗn loạn), hoặc khi kết quả sẽ được dùng làm cơ sở cho một quyết định.

Từ đó có hai cách kiểm tra, và chi phí của chúng phụ thuộc vào mã nguồn. Chạy lại ở độ chính xác cao hơn, hoặc cộng dồn bằng một phương pháp có bù sai số (compensated) hay cộng theo cặp (pairwise), rồi so sánh. Hoặc đổi thứ tự cộng dồn rồi so sánh. Nếu các khác biệt nhỏ hơn hẳn sai số rời rạc hóa và mục tiêu độ chính xác đã nêu, làm tròn khó có thể là mối lo chính. Sự trùng khớp là bằng chứng chứ không phải chứng minh, vì nó chỉ thăm dò những biến thể đã được thử.

## Câu hỏi còn mở

- Nên chọn ngưỡng sai lệch cho phép trong một phép so sánh như vậy thế nào? Có lẽ nó phụ thuộc vào sai số rời rạc hóa và vào độ nhạy của đại lượng quan tâm đối với nhiễu loạn, nhưng chưa thấy một quy tắc chung nào.
- Trong một hệ hỗn loạn, các quỹ đạo ứng với các thứ tự cộng dồn khác nhau rốt cuộc sẽ tách xa nhau. Khi đó nên so sánh những đại lượng thống kê nào, và một khác biệt lớn đến đâu là chấp nhận được?
- Trong những điều kiện nào có thể dùng độ chính xác hỗn hợp (mixed precision) mà không làm thay đổi các kết luận rút ra từ một lần chạy?
