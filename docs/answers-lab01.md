# Báo cáo thảo luận Lab 01: Thiết lập môi trường & Refactor Flow

## 1. Câu hỏi nhanh (Slide 19)
### Câu hỏi: Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
**Trả lời:**
- **Nơi lưu trữ:**
  - Cấu hình `--global` được lưu trong tệp `.gitconfig` tại thư mục người dùng (`~/.gitconfig` trên Linux/macOS hoặc `C:\Users\<Username>\.gitconfig` trên Windows).
  - Cấu hình `--local` được lưu trong tệp `.git/config` ngay tại thư mục gốc của repository đang làm việc.
- **Sự khác biệt:**
  - Phạm vi ảnh hưởng: `--global` áp dụng cho toàn bộ các repository trên máy tính đối với user hiện tại; `--local` chỉ áp dụng riêng cho chính repository đó.
  - Mức độ ưu tiên: Cấu hình `--local` có độ ưu tiên cao hơn và sẽ ghi đè lên cấu hình `--global` nếu có xung đột cấu hình (ví dụ: dùng email công việc cho một repo cụ thể thay vì email cá nhân chung).

---

## 2. Câu hỏi thảo luận (Slide 26)
### Câu hỏi 1: Vì sao dùng `git mv`?
**Trả lời:**
- Lệnh `git mv` vừa di chuyển/đổi tên file trong working directory, vừa tự động cập nhật và ghi nhận hành vi đổi tên vào staging area (`index`).
- Giúp Git giữ được tính liên tục của lịch sử quản lý phiên bản (bảo toàn commit history). Nhờ đó, ta có thể truy vết lịch sử các phiên bản cũ của tệp sau khi đổi tên bằng lệnh `git log --follow <đường_dẫn_mới>`.
- Nếu chỉ dùng lệnh `mv` hoặc di chuyển file thủ công bằng hệ điều hành, Git ban đầu sẽ xem đó là hành động xóa tệp cũ (deleted) và tạo tệp mới hoàn toàn (untracked), dễ dẫn đến sai sót khi stage và mất tính trực quan trong lịch sử thay đổi.

### Câu hỏi 2: `release/lab01` có phải baseline không?
**Trả lời:**
- **Có.** Trong Quản lý cấu hình phần mềm (SCM), Baseline là một cấu hình mốc chuẩn đã được kiểm thử, nghiệm thu và thống nhất tại một thời điểm xác định.
- Nhánh `release/lab01` đánh dấu trạng thái ổn định đầu tiên của mã nguồn sau khi đã hoàn thành tái cấu trúc (refactor package `aims/`, kiểm tra chạy `python main.py` ra đúng kết quả `63.89 $`).
- Baseline này được "đóng băng" để nộp bài và làm cơ sở đối chuẩn cho các giai đoạn phát triển tiếp theo; không được phép sửa đổi tùy tiện mà chỉ được cập nhật qua quy trình kiểm soát thay đổi chặt chẽ.

### Câu hỏi 3: Vì sao không commit thẳng master dù làm một mình?
**Trả lời:**
- **Tuân thủ nguyên tắc SCM (Change Control):** Việc không commit trực tiếp lên `master` giúp hình thành kỷ luật quy trình làm việc chuẩn nghiệp nghiệp. Mọi thay đổi đều phải được cô lập trên một nhánh riêng (feature/refactor branch).
- **Kiểm soát rủi ro và tự review (Self-Review):** Khi tạo Pull Request, lập trình viên có cơ hội nhìn lại toàn bộ diff (`Files changed`) để rà soát lỗi cú pháp, tệp thừa (như `__pycache__`) trước khi hợp nhất.
- **Tích hợp tự động và khả năng mở rộng:** Nhánh `master` luôn luôn ở trạng thái "Deployable" (có thể phát hành/chạy được). Nếu sau này có cộng sự hoặc tích hợp hệ thống kiểm thử CI/CD, quy trình PR sẽ bảo vệ nhánh chính không bao giờ bị phá vỡ.
