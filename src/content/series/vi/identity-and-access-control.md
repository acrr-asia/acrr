---
title: "Định danh và kiểm soát truy cập"
description: "Loạt bài về cách các hệ thống mạng xác định ai đang gửi yêu cầu và bên đó được phép làm gì, từ mô hình kiểm soát truy cập (access control) xuống đến các giao thức và định dạng token."
category: "Computing Systems"
status: "published"
objectives:
  - "Phân biệt định danh (identification), xác thực (authentication), phân quyền (authorization) và kiểm toán (audit), và chỉ ra cơ chế nào trả lời câu hỏi nào."
  - "So sánh phiên (session) phía máy chủ với token tự chứa (self-contained token) xét theo nơi lưu trạng thái, cách thu hồi (revocation) hoạt động và những gì bên xác minh (verifier) cần có."
  - "Giải thích phân quyền ủy nhiệm (delegated authorization) với OAuth 2.0 và xác thực liên kết (federated authentication) với OpenID Connect, bao gồm lý do các client công khai (public client) cần PKCE."
  - "Xác minh access token một cách đúng đắn và thực thi phân quyền ở mức đối tượng (object-level authorization) tại máy chủ tài nguyên (resource server)."
---

Loạt bài này dành cho người đọc xây dựng hoặc rà soát phần mềm mạng và muốn có một mô hình kiểm soát truy cập không phụ thuộc vào một framework hay nhà cung cấp cụ thể nào. Bài thứ nhất trình bày toàn cảnh từ trên xuống; mỗi bài sau đó lấy một tầng của bức tranh ấy và đi sâu hơn vào tầng đó.
