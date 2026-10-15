---
title: "Định danh và kiểm soát truy cập"
description: "Cách các hệ thống mạng xác lập ai đang gửi yêu cầu và quyết định bên đó được làm gì, từ mô hình kiểm soát truy cập đến token và lời gọi giữa các dịch vụ."
category: "Computing Systems"
status: "published"
objectives:
  - "Phân biệt định danh (identification), xác thực (authentication), phân quyền (authorization) và kiểm toán (audit), và chỉ ra cơ chế nào trả lời câu hỏi nào."
  - "Đánh giá các phương tiện xác thực (authenticator) theo khả năng chống đoán trực tuyến, chống lộ dữ liệu của bên xác minh (verifier), chống phát lại và chống lừa đảo giả mạo (phishing), và giải thích vì sao thông tin xác thực khóa công khai gắn với nguồn gốc (origin) chống được phishing."
  - "So sánh phiên (session) phía máy chủ với token tự chứa (self-contained token) xét theo nơi lưu trạng thái, cách thu hồi (revocation) hoạt động và những gì bên xác minh cần có."
  - "Giải thích phân quyền ủy nhiệm (delegated authorization) với OAuth 2.0 và xác thực liên kết (federated authentication) với OpenID Connect, bao gồm lý do các client công khai (public client) cần PKCE."
  - "Xác minh access token một cách đúng đắn và thực thi phân quyền ở mức đối tượng (object-level authorization) tại máy chủ tài nguyên (resource server)."
  - "Thiết kế việc xác thực giữa các dịch vụ bằng danh tính workload, token ràng buộc bên gửi (sender-constrained token) và trao đổi token ở từng chặng, thay vì dựa vào vị trí mạng, token được chuyển tiếp hay trường tiêu đề được tin cậy."
---

Loạt bài này dành cho người đọc xây dựng hoặc rà soát phần mềm mạng, chẳng hạn một ứng dụng web, một API HTTP hay một tập dịch vụ back-end, và muốn có một mô hình kiểm soát truy cập (access control) không phụ thuộc vào một framework hay nhà cung cấp cụ thể nào. Loạt bài giả định người đọc đã viết hoặc đọc mã gửi và xử lý các yêu cầu web, và biết chữ ký số và hàm băm bảo đảm điều gì, không cần đến phần toán học của chúng. Mọi thứ khác mà loạt bài cần, từ HTTP và TLS đến cookie và JSON Web Token, đều được giới thiệu ở nơi chúng được dùng lần đầu.

Thứ tự các bài đi theo một yêu cầu qua hệ thống. Bài thứ nhất trình bày toàn cảnh từ trên xuống: bộ giám sát tham chiếu (reference monitor) phải thấy mọi yêu cầu, hai câu hỏi mà mọi yêu cầu đặt ra (*ai đang hỏi?* và *họ có được làm điều này không?*), và các token mang câu trả lời giữa các dịch vụ. Hai bài tiếp theo trả lời sâu câu hỏi thứ nhất. Bài thứ hai so sánh các phương tiện xác thực mà người dùng dùng để chứng minh một danh tính, từ mật khẩu đến passkey, còn bài thứ ba cho thấy một phiên web mang bằng chứng ấy từ yêu cầu này sang yêu cầu khác như thế nào và những cuộc tấn công nào nhắm vào nó. Bài thứ tư chuyển sang câu hỏi thứ hai và so sánh các mô hình dùng để viết chính sách phân quyền. Bài thứ năm trở lại OAuth 2.0 và xem xét cách từng loại client nhận token. Bài thứ sáu gắn các token đó với khóa để một bản sao bị đánh cắp trở nên vô dụng, và bài thứ bảy áp dụng cùng các nguyên tắc bên trong hệ thống, nơi các dịch vụ gọi nhau thay mặt người dùng.

Mọi bài đều dùng chung một vài quy ước. Các thông điệp HTTP được viết theo cú pháp văn bản của HTTP/1.1, và không điều gì trong loạt bài phụ thuộc vào phiên bản HTTP. Token, khóa, định danh và mốc thời gian trong các ví dụ là giá trị minh họa, nhất quán với nhau ở những chỗ bài viết nói rõ như vậy. Mã giả không gắn với ngôn ngữ lập trình nào. Các tiêu chuẩn được dẫn bằng số RFC hoặc số đặc tả trong bài, và được liệt kê đầy đủ trong phần tài liệu tham khảo của mỗi bài.
