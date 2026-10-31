# Báo cáo thảo luận Lab 04: Release Flow & Phiên bản phát hành

## 1. Câu hỏi nhanh (Slide 47)
### Câu hỏi: Vì sao chuẩn bị trên `master` trước, không sửa trên nhánh release?
**Trả lời:**
- **Nguyên tắc cốt lõi của Release Flow:** Nhánh `release/*` chỉ là nhánh phái sinh phục vụ phát hành và đóng băng baseline, **tuyệt đối không bao giờ merge ngược lại vào nhánh `master`**.
- Do đó, mọi công việc chuẩn bị cho phiên bản phát hành như: cập nhật số phiên bản (`__version__`), chỉnh sửa `CHANGELOG.md`, kiểm tra tính ổn định mã nguồn đều phải được thực hiện hoàn chỉnh trên nhánh `master` trước (thông qua nhánh chuẩn bị `topic/prepare-release-x.x.x` và PR).
- Khi `master` đã ở trạng thái hoàn hảo nhất, ta mới rẽ nhánh `release/labXX` từ commit đó. Nếu sửa trực tiếp trên `release/*`, các thay đổi về phiên bản và tài liệu sẽ bị kẹt lại trên nhánh release và không bao giờ tự động có mặt trên `master`, dẫn đến sai lệch cấu hình trong các phiên bản tương lai.

---

## 2. Câu hỏi thảo luận (Slide 52)
### Câu hỏi 1: Vì sao `release/*` không merge vào master? So sánh với GitFlow.
**Trả lời:**
- **Trong Release Flow:**
  - Nhánh `master` luôn luôn đi thẳng về phía trước theo dòng chảy liên tục (continuous delivery mindset). Nhánh `release/*` chỉ rẽ nhánh để làm nhiệm vụ đóng băng và bảo trì phiên bản (maintenance line).
  - Không merge `release/*` ngược lại vào `master` giúp nhánh chính không bị ô nhiễm bởi các commit trung gian, tránh tạo ra các merge commit lộn xộn hoặc vô tình ghi đè các tính năng mới đang phát triển trên `master`. Khi cần đưa bản sửa lỗi từ release về master, ta sử dụng công cụ `cherry-pick -x` để nhặt chính xác từng commit sửa lỗi cụ thể.
- **So sánh với GitFlow:**
  - GitFlow duy trì đồng thời 2 nhánh vĩnh viễn: `main` (sản xuất) và `develop` (phát triển tích hợp). Nhánh `release` được tạo từ `develop`, và khi hoàn tất phải merge vào **cả** `main` lẫn `develop`.
  - Hạn chế của GitFlow: Cấu trúc merge 2 chiều rất phức tạp, dễ gây ra tình trạng xung đột kép (merge hell), khó quản lý khi có nhiều phiên bản cùng chạy đồng thời và làm chậm chu kỳ phát hành nhanh hiện đại.

### Câu hỏi 2: Vì sao lên `1.0.0` mà không phải `0.4.0`?
**Trả lời:**
- **Quy tắc Semantic Versioning (SemVer):**
  - Định dạng phiên bản: `MAJOR.MINOR.PATCH`.
  - Các phiên bản `0.y.z` đại diện cho giai đoạn phát triển ban đầu (Initial Development Phase), khi phần mềm chưa hoàn thiện, API có thể thay đổi bất kỳ lúc nào và chưa có cam kết ổn định.
  - Phiên bản `1.0.0` đánh dấu cột mốc quan trọng: **Sản phẩm chính thức đạt trạng thái hoàn thiện đầu tiên (First Public/Production Release)**. Tại thời điểm Lab 04, dự án `AIMS-mini` đã có cấu trúc package chuẩn mực, các tính năng cốt lõi (Cart, DVD, tìm kiếm, giảm giá, in hóa đơn), bộ unit test đầy đủ và tài liệu ca sử dụng.
  - Việc gắn số `1.0.0` xác lập một baseline chính thức, đưa ra cam kết về tính ổn định và tương thích cho người sử dụng thay vì coi nó chỉ là bản thử nghiệm `0.4.0`.
