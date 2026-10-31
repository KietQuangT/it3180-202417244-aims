# Báo cáo thảo luận Lab 03: Bugfix Flow, Xung đột & Hoàn tác

## Câu hỏi thảo luận (Slide 43)

### Câu hỏi 1: Merge base là gì?
**Trả lời:**
- **Định nghĩa:** Merge base giữa hai nhánh (hoặc hai commit cụ thể A và B) là commit tổ tiên chung gần nhất (best common ancestor) của cả hai nhánh đó trong đồ thị có hướng không chu trình (DAG) của Git.
- **Vai trò trong quá trình hợp nhất (3-way merge):**
  - Khi thực hiện lệnh merge hoặc giải quyết xung đột, Git không chỉ so sánh trực tiếp nhánh A với nhánh B mà dùng thuật toán 3 chiều (3-way merge) dựa trên 3 điểm:
    1. Trạng thái tại `merge base` (gốc chung ban đầu).
    2. Trạng thái tại đầu nhánh A (nhánh đích).
    3. Trạng thái tại đầu nhánh B (nhánh nguồn).
  - Bằng cách so sánh xem tệp tin đã thay đổi như thế nào từ `merge base` tới từng nhánh, Git có thể tự động tích hợp các thay đổi không trùng dòng và chỉ gắn cờ xung đột (conflict markers `<<<<<<<`, `=======`, `>>>>>>>`) khi cả hai nhánh cùng sửa đổi cùng một vùng dòng mã so với gốc chung `merge base`.
- Có thể tìm SHA của merge base bằng lệnh: `git merge-base branchA branchB`.

---

### Câu hỏi 2: Vì sao `master` / `release/*` phải dùng `revert` thay vì `reset`?
**Trả lời:**
- **Cơ chế hoạt động:**
  - `git reset` (nhất là `--hard`) dịch chuyển con trỏ nhánh lùi về quá khứ và **xóa bỏ/viết lại lịch sử** commit. Các commit phía sau vị trí reset sẽ bị tách khỏi nhánh.
  - `git revert` giữ nguyên toàn bộ lịch sử cũ và **tạo thêm một commit mới** có nội dung đảo ngược hoàn toàn (inverse diff) các thay đổi của commit/merge commit muốn hủy bỏ.
- **Lý do phải dùng revert trên master và release/*:**
  - **Bảo toàn môi trường cộng tác (Public branch safety):** Nhánh `master` và `release/*` là nhánh dùng chung mà các thành viên khác trong nhóm đã đồng bộ (`pull`) về máy của họ. Nếu ta dùng `reset` rồi cố tình force push (`push --force`), cây lịch sử của các thành viên khác sẽ bị lỗi lệch gốc, gây hỗn loạn và nguy cơ mất code nghiêm trọng.
  - **Tính truy vết (SCM Audit & Traceability):** Trong quản lý cấu hình chuẩn, mọi hành động sửa đổi hay thu hồi đều phải được ghi vết rõ ràng. `git revert` tạo ra một commit ghi nhận minh bạch nguyên nhân hoàn tác (ví dụ: revert PR bị lỗi), giúp đội ngũ kiểm toán cấu hình nắm rõ tại sao một thay đổi từng được tích hợp rồi lại bị thu hồi.
