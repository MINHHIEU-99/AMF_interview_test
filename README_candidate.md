# Bài test: Gộp BOM từ nhiều bản vẽ

**Thời gian đề xuất: 20 phút**

## Đề bài

Bạn nhận được kết quả bóc tách (giả lập) từ 3 bản vẽ khác nhau thuộc **cùng một dự án**. Mỗi bản vẽ trả về một danh sách chi tiết (part) ở cấp bản vẽ — xem `drawing_1.json`, `drawing_2.json`, `drawing_3.json`.

Nhiệm vụ của bạn: gộp chúng thành **1 BOM (Bill of Materials) duy nhất** cho toàn dự án.

## Yêu cầu

Các bản vẽ khác nhau có thể ghi mã/tên chi tiết theo cách hơi khác nhau cho **cùng một chi tiết vật lý** (viết tắt khác, cách đặt mã khác nhau giữa các kỹ sư vẽ, có/không có hậu tố revision...). Bạn cần:

1. **Gộp các chi tiết thực sự trùng nhau** thành 1 dòng, cộng dồn số lượng (`qty`) đúng.
2. **Không gộp nhầm** các chi tiết thực sự khác nhau dù mã/tên có vẻ giống nhau.
3. Với những cặp bạn **không chắc chắn** là trùng hay khác, đừng tự quyết định — đưa vào danh sách `needs_review` kèm lý do ngắn gọn, để con người xem lại.
4. Viết 1 giao diện web (bất kể ngôn ngữ) cho phép import file json trên vào, và hiển thị ra bảng kết quả cuối cùng.

## Lưu ý

- Bạn được tự do dùng bất kỳ thư viện nào có sẵn trong máy, hoặc cài thêm thư viện nếu muốn.
- Bạn được phép dùng AI coding assistant (Copilot, ChatGPT, Claude...)

