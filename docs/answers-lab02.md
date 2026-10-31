# Báo cáo thảo luận Lab 02: Feature/Topic Flow & Pull Request

## Câu hỏi thảo luận (Slide 35)

### Câu hỏi 1: Vì sao phải đồng bộ master trước khi PR?
**Trả lời:**
- **Nguyên lý Shift Left & Giảm xung đột:** Trong môi trường làm việc song song nhiều nhánh/nhiều lập trình viên, nhánh `master` liên tục tiến lên phía trước do các PR khác được merge vào.
- Khi nhánh tính năng được đồng bộ với `master` (thông qua `git fetch origin` và `git merge origin/master`), lập trình viên có thể phát hiện và xử lý mọi xung đột phát sinh ngay tại máy cá nhân (local environment), thay vì đẩy xung đột lên GitHub.
- **Đảm bảo tính tương thích tích hợp:** Giúp lập trình viên chạy thử nghiệm kiểm thử (`main.py`, unit test) trên mã nguồn đã tích hợp để xác nhận rằng tính năng mới hoạt động hài hòa với những thay đổi mới nhất của hệ thống trước khi gửi PR cho CCB/Reviewer phê duyệt.

---

### Câu hỏi 2: Khi nào không được rebase?
**Trả lời:**
- **Quy tắc vàng của Git Rebase:** Không bao giờ thực hiện rebase trên các nhánh công khai/đã được chia sẻ (public/shared branches) như `master`, `main`, `release/*` hoặc nhánh đang có nhiều người cùng làm việc chung.
- **Lý do:** Lệnh rebase sẽ viết lại toàn bộ lịch sử commit (tạo ra các commit hash/SHA mới thay thế commit cũ). Khi người khác pull về, cây lịch sử Git cục bộ của họ sẽ bị rẽ nhánh xung đột nghiêm trọng với remote, dẫn đến thảm họa hợp nhất (merge hell) và mất dấu vết lịch sử.
- **Chỉ sử dụng rebase khi:** Làm việc trên nhánh riêng tư của bản thân (local feature branch) chưa từng push lên remote, hoặc nhánh chỉ một mình mình kiểm soát nhằm mục đích làm gọn gàng lịch sử commit trước khi tạo PR.

---

### Câu hỏi 3: `feature/*` khác `topic/*` ra sao?
**Trả lời:**
- **Nhánh `feature/*` (Feature branch):**
  - Dùng để phát triển các tính năng nghiệp vụ cụ thể của sản phẩm phần mềm (ví dụ: `feature/cart-print`, `feature/discount`, `feature/search-by-title`).
  - Trực tiếp sửa đổi hoặc mở rộng logic nghiệp vụ trong mã nguồn ứng dụng (`aims/cart.py`, `aims/search.py`).
  - Thường có vòng đời theo tiến độ của tính năng và đi kèm các bài kiểm thử chức năng (functional tests).
- **Nhánh `topic/*` (Topic branch):**
  - Dùng cho các chủ đề ngắn hạn, công việc hỗ trợ kỹ thuật hoặc tài liệu phi chức năng (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/prepare-release-1.0.0`).
  - Phạm vi thay đổi thường tập trung vào cấu hình dự án, quy trình (`.github/`), tài liệu kỹ thuật (`docs/`) hoặc chuẩn bị phiên bản phát hành (`CHANGELOG.md`).
