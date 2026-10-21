---
title: "Tư duy phản biện và lập luận"
description: "Lập luận rõ ràng về điều nên tin và nên làm: ý nghĩa, lập luận, logic hình thức, bằng chứng khoa học và thống kê, giá trị, quyết định, ngụy biện và sáng tạo."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Giải thích tư duy phản biện (critical thinking) là gì và phân tích một nhận định hay một lập luận thành ý nghĩa, tiền đề, kết luận và các giả định ẩn của nó."
  - "Đánh giá tính hợp lệ (validity), tính đúng đắn (soundness) và độ mạnh quy nạp (inductive strength) của lập luận, dùng biểu đồ Venn, bảng chân trị, suy diễn tự nhiên (natural deduction) và logic lượng từ khi lập luận có cấu trúc hình thức."
  - "Thẩm định các nhận định nhân quả, khoa học và thống kê: thiết kế một phép so sánh công bằng, áp dụng các quy tắc xác suất và định lý Bayes, diễn giải mẫu và kiểm định ý nghĩa."
  - "Phân tích các phán đoán giá trị và các quyết định: tách tiền đề sự kiện khỏi tiền đề đánh giá, kiểm tra tính nhất quán của các nguyên tắc và so sánh các phương án bằng tiêu chí tường minh."
  - "Nhận diện các ngụy biện (fallacy) và thiên kiến nhận thức (cognitive bias) thường gặp trong lập luận thực tế, và áp dụng các kỹ thuật có cấu trúc để tạo ra và phát triển ý tưởng mới."
---

Loạt bài này viết cho người đọc muốn lập luận cẩn thận hơn về cả câu hỏi kỹ thuật lẫn câu hỏi đời thường: một nhận định có nghĩa là gì, bằng chứng cho nó có tốt không, và điều gì suy ra được từ nó. Loạt bài không đòi hỏi kiến thức nền về triết học hay logic. Các bài thứ tư, thứ chín và thứ mười hai có vài đoạn mã Python 3 ngắn, và các bài về xác suất và thống kê dùng đại số phổ thông; ngoài các kiến thức nền thông thường của trang, không cần gì thêm.

Loạt bài là một phần nhập môn, không phải một khóa học đầy đủ về bất kỳ lĩnh vực nào trong số đó. Loạt bài không bàn đến logic tình thái (modal logic) và các logic phi cổ điển khác, lý thuyết chứng minh và siêu lý thuyết của logic ngoài việc phát biểu các kết quả chính, các phương pháp thống kê ngoài các kiểm định ý nghĩa và khoảng tin cậy cơ bản, cũng như lịch sử và các trường phái đạo đức học ngoài những gì cần để lập luận về một phán đoán giá trị.

Thứ tự các bài theo thứ tự mà một người lập luận cẩn thận gặp một nhận định. Bài thứ nhất nói tư duy phản biện là gì và vì sao chỉ dựa vào trực giác là chưa đủ. Bài thứ hai bàn về ý nghĩa, vì một nhận định mơ hồ (ambiguous) hay không rõ ranh giới (vague) thì chưa thể đánh giá được. Bài thứ ba giới thiệu lập luận: tiền đề và kết luận, giả định ẩn và sự khác nhau giữa tính hợp lệ diễn dịch và độ mạnh quy nạp.

Các bài từ thứ tư đến thứ bảy là một khóa ngắn về logic hình thức. Bài thứ tư giải thích logic học nghiên cứu gì và vì sao tính hợp lệ phụ thuộc vào hình thức. Bài thứ năm xét các mệnh đề định danh (categorical statement) và tam đoạn luận (syllogism) bằng biểu đồ Venn. Bài thứ sáu xây dựng logic mệnh đề (sentential logic), từ bảng chân trị đến chứng minh bằng suy diễn tự nhiên, và bài thứ bảy mở rộng nó thành logic vị từ (predicate logic) với các lượng từ.

Bài thứ tám và thứ chín chuyển từ suy diễn sang bằng chứng. Bài thứ tám bàn về phương pháp khoa học và lập luận nhân quả; bài thứ chín bàn về xác suất, định lý Bayes và cách diễn giải số liệu thống kê. Bài thứ mười hỏi cách lập luận về giá trị, nơi bằng chứng sự kiện tự nó không giải quyết được câu hỏi, và bài thứ mười một áp dụng mọi điều đã học vào quyết định và chiến lược. Bài thứ mười hai tập hợp các ngụy biện và thiên kiến nhận thức mà các bài trước đã gặp từng cái một, và bài cuối cùng chuyển từ đánh giá ý tưởng sang tạo ra ý tưởng.

Ký hiệu logic theo cách dùng phổ biến trong giáo trình: ¬ (không), ∧ (và), ∨ (hoặc), → (nếu ... thì) và ↔ (khi và chỉ khi), cùng ∀ và ∃ cho các lượng từ. Chủ đề và thứ tự của loạt bài được gợi ý từ *Critical Thinking Web* của Đại học Hồng Kông, một bộ bài hướng dẫn mở của Joe Lau và Jonathan Chan; văn bản, ví dụ và hình vẽ của loạt bài này là nguyên bản.

## Tài liệu tham khảo

- J. Y. F. Lau and J. Chan, *Critical Thinking Web*, Department of Philosophy, The University of Hong Kong, 2004–2026. https://philosophy.hku.hk/think/
