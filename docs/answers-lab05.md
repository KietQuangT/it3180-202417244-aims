# Báo cáo thảo luận Lab 05: Hotfix Flow & Bảo trì nhiều phiên bản

## 1. Câu hỏi nhanh (Slide 60)
### Câu hỏi: Vì sao ở Phần A chưa gắn tag `v1.1.0`? Nếu đã gắn rồi thì bây giờ phải phát hành `v1.1.1`?
**Trả lời:**
- **Nguyên lý tính bất biến của Tag (Tag Immutability):** Trong Git và SCM, một annotated tag đã được tạo và chia sẻ (`push`) lên remote đại diện cho một mốc cấu hình đóng băng tuyệt đối, không được phép thay đổi, dịch chuyển hoặc xóa bỏ.
- Ở Phần A, nhánh `release/lab05` mới chỉ được chuẩn bị xong các tính năng mới cho phiên bản 1.1.0 nhưng vẫn đang trong giai đoạn nghiệm thu/kiểm thử trước khi phát hành chính thức. Nếu ta vội vàng gắn tag `v1.1.0` ngay lúc đó, thì khi phát hiện ra lỗi case-sensitive trong tìm kiếm (Issue #18/#20) và đưa bản vá vào, theo quy tắc Semantic Versioning, mốc `v1.1.0` đã bị "đóng gói", ta bắt buộc phải nâng số PATCH lên thành `v1.1.1` để phát hành bản sửa lỗi.
- Do đó, ta trì hoãn việc gắn tag `v1.1.0` cho tới khi nhánh `release/lab05` đã tích hợp xong toàn bộ các hotfix cần thiết. Nhờ vậy, phiên bản phát hành đầu tiên của chu kỳ này vẫn mang đúng mã định danh `v1.1.0`.

---

## 2. Câu hỏi thảo luận (Slide 64)
### Câu hỏi 1: Ưu, nhược điểm của Upstream First so với Release First?
**Trả lời:**
- **Release First (Mô hình học phần áp dụng):**
  - *Cách làm:* Tạo nhánh `hotfix/*` trực tiếp từ nhánh release đang bị lỗi (`origin/release/lab04`), vá lỗi và phát hành ngay bản vá `v1.0.1`, sau đó mới lan truyền (cherry-pick) bản sửa lỗi về `master` và các nhánh release khác.
  - *Ưu điểm:* Xử lý khẩn cấp và đưa bản vá tới tay người dùng phiên bản bị lỗi nhanh nhất; phạm vi sửa đổi tối thiểu và cách ly rủi ro đối với hệ thống sản xuất.
  - *Nhược điểm:* Đội ngũ phát triển dễ quên lan truyền (cherry-pick) bản sửa ngược về nhánh chính `master` hoặc các dòng phát hành kế tiếp, dẫn đến hiện tượng lỗi tái xuất hiện (regression bug) trong các phiên bản sau.
- **Upstream First (Mô hình Microsoft khuyến nghị):**
  - *Cách làm:* Sửa lỗi và kiểm thử kỹ lưỡng tại nhánh phát triển chính (`master`/upstream) trước tiên, sau đó mới cherry-pick commit sửa lỗi đó ngược về các nhánh `release/*` đang cần bảo trì.
  - *Ưu điểm:* Đảm bảo chắc chắn rằng nhánh `master` và tất cả các phiên bản tương lai không bao giờ bị sót lỗi đó; tư duy phát triển nhất quán.
  - *Nhược điểm:* Đôi khi mã nguồn trên `master` đã phát triển quá xa so với nhánh release cũ, chứa nhiều kiến trúc mới khiến việc trích xuất và cherry-pick ngược trở lại các phiên bản cũ gặp xung đột mã phức tạp.

---

### Câu hỏi 2: Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
**Trả lời:**
1. **Lệnh kiểm tra hành vi tự động bằng vòng lặp shell (Behavior Audit):**
   ```bash
   for ref in v1.0.1 v1.1.0 master; do
       git switch --detach -q $ref; printf "%-8s " $ref
       python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
                  print(len(search_by_title([D('The Lion King')], 'lion')))"
   done; git switch -q master
   ```
   - Kỳ vọng khi đã lan truyền đầy đủ: Cả 3 phiên bản đều in ra kết quả `1`.
   - Nếu quên lan truyền sang `release/lab05` (tag `v1.1.0`), tại dòng `v1.1.0` lệnh sẽ in ra kết quả `0` (tìm kiếm không ra do phân biệt hoa thường), từ đó phát hiện ngay vi phạm.

2. **Lệnh kiểm toán commit cherry-pick qua nhật ký:**
   ```bash
   git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
   ```
   - Kỳ vọng: Phải tìm thấy đủ **2 commit** cherry-pick (một commit trên `master` và một commit trên `release/lab05`).
   - Nếu thiếu trên `release/lab05`, lệnh này chỉ hiển thị duy nhất 1 commit (trên `master`).

3. **Lệnh đối chuẩn commit bằng `git cherry`:**
   ```bash
   git cherry -v origin/release/lab05 origin/release/lab04
   ```
   - Lệnh này so sánh các commit giữa hai nhánh dựa trên nội dung thay đổi (patch-id).
   - Nếu bản sửa lỗi chưa có trên `release/lab05`, commit `fix: make search_by_title case-insensitive` sẽ xuất hiện với tiền tố dấu `+` (nghĩa là nhánh đích chưa có bản vá tương đương). Ngược lại, nếu đã có sẽ hiển thị dấu `-`.
