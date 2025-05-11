

# **Cyclomatic Complexity Analyzer**

## 🚀 Tổng quan

**Cyclomatic Complexity Analyzer** là một công cụ giúp phân tích độ phức tạp mã nguồn của chương trình Python dựa trên **McCabe's Cyclomatic Complexity**. Công cụ này giúp xác định mức độ phức tạp của các hàm trong mã nguồn, đồng thời đưa ra các gợi ý để **refactor** (tái cấu trúc) mã nguồn từ **API Gemini**. Ngoài ra, công cụ còn vẽ **biểu đồ Control Flow Graph (CFG)** để người dùng dễ dàng hình dung cấu trúc luồng điều khiển của mỗi hàm.

### **Mục tiêu của dự án:**
1. **Phân tích độ phức tạp McCabe**: Tính toán độ phức tạp McCabe của từng hàm trong mã nguồn.
2. **Gợi ý refactor**: Tích hợp với **API Gemini** để đưa ra các gợi ý về cách cải thiện mã nguồn.
3. **Vẽ Control Flow Graph (CFG)**: Sinh và vẽ đồ thị luồng điều khiển để người dùng dễ dàng phân tích.
4. **Tính toán LOC và Comment**: Đếm số dòng mã (LOC) và số dòng comment trong mã nguồn.

---

## Công thức tính Cyclomatic Complexity (CC)

Cyclomatic Complexity (CC) là một chỉ số đo lường độ phức tạp của một chương trình bằng cách đếm số lượng các đường đi độc lập trong mã nguồn. Công thức tính CC như sau:

### Công thức:
\[
CC = E - N + 2P
\]

- **E**: Số lượng cạnh (edges) trong đồ thị điều khiển (control flow graph).
- **N**: Số lượng đỉnh (nodes) trong đồ thị điều khiển.
- **P**: Số lượng các thành phần liên kết (connected components) trong đồ thị (thường là 1 đối với một chương trình duy nhất).

### Cách áp dụng Cyclomatic Complexity:
- CC = 1: Chương trình có độ phức tạp thấp, không có nhánh điều kiện.
- CC = 2 đến 10: Độ phức tạp vừa phải, ít nhánh điều kiện.
- CC > 10: Độ phức tạp cao, cần được xem xét lại hoặc tái cấu trúc.

### Ví dụ:
Giả sử chúng ta có một đoạn mã với một nhánh điều kiện đơn giản:

```python
def example(x):
    if x > 0:
        return True
    else:
        return False
```
---

## 🛠️ Các công cụ và thư viện sử dụng

- **Python 3.x**: Ngôn ngữ lập trình chính.
- **Streamlit**: Thư viện giao diện người dùng (UI) cho phép tạo ứng dụng web nhanh chóng.
- **NetworkX**: Thư viện vẽ đồ thị, sử dụng để vẽ **Control Flow Graph (CFG)**.
- **Matplotlib**: Thư viện vẽ biểu đồ.
- **Google Gemini API**: Sử dụng để đưa ra các gợi ý refactor mã nguồn.
- **dotenv**: Để quản lý các biến môi trường như API key.

---

## 🚀 Cài đặt và cấu hình

### 1. **Cài đặt thư viện**

Để cài đặt các thư viện cần thiết, bạn có thể sử dụng **pip**:

```bash
pip install -r requirements.txt
```

### 2. **Cấu hình API Key**

Để sử dụng API **Gemini** từ Google, bạn cần có **API Key**:

- Tạo một tài khoản trên Google Cloud và kích hoạt **Google Gemini API**.
- Lưu **API key** vào file `.env` trong thư mục gốc của dự án:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 🧑‍💻 Hướng dẫn sử dụng

1. **Chạy ứng dụng Streamlit**

   Sau khi cài đặt các thư viện và cấu hình API key, bạn có thể chạy ứng dụng bằng cách sử dụng câu lệnh sau:

   ```bash
   streamlit run webapp.py
   ```

2. **Chọn loại input mã nguồn**

   Ứng dụng hỗ trợ 2 cách nhập mã nguồn:
   - **Nhập thủ công**: Bạn có thể dán mã Python vào ô nhập liệu.
   - **Tải file**: Bạn có thể tải lên file `.py` chứa mã nguồn cần phân tích.

3. **Phân tích mã nguồn**

   Sau khi nhập mã nguồn, nhấn nút **🔍 Phân tích**. Ứng dụng sẽ:
   - Phân tích độ phức tạp McCabe của từng hàm trong mã nguồn.
   - Hiển thị **gợi ý refactor** từ **API Gemini**.
   - Vẽ **Control Flow Graph (CFG)** cho mỗi hàm.
   - Hiển thị biểu đồ độ phức tạp của từng hàm.

---

## 🖥️ Các chức năng chính

1. **Phân tích độ phức tạp McCabe**:
   - Đo độ phức tạp của từng hàm và đưa ra mức độ phức tạp (Cyclomatic Complexity).
   - Mức độ phức tạp này giúp người lập trình hiểu rõ về mức độ phức tạp của hàm, từ đó có thể tối ưu hóa mã nguồn.

2. **Gợi ý Refactor**:
   - Dựa vào API **Gemini** của Google, ứng dụng sẽ đưa ra các gợi ý cải tiến mã nguồn cho từng hàm.

3. **Vẽ Control Flow Graph (CFG)**:
   - Sinh và vẽ đồ thị luồng điều khiển của mỗi hàm trong mã nguồn.
   - Dễ dàng hình dung các nhánh, vòng lặp và các điều kiện trong hàm.

4. **Đếm LOC và Comment**:
   - Đếm tổng số dòng mã (LOC) và số dòng comment trong mã nguồn giúp người lập trình đánh giá được mức độ tài liệu của mã.

---

## 📊 Biểu đồ và Kết quả

- **Biểu đồ Cyclomatic Complexity**: Hiển thị độ phức tạp McCabe của từng hàm. Các hàm có độ phức tạp cao sẽ được đánh dấu với màu đỏ, cho thấy cần được refactor.
- **Control Flow Graph**: Biểu đồ luồng điều khiển giúp người dùng hiểu rõ hơn về cách thức các câu lệnh trong hàm được thực thi và điều khiển.

---

## 🧑‍💻 Ví dụ đầu ra

### **Input**:
```python
def giai_pt_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    return x1, x2
```

### **Output**:

1. **Cyclomatic Complexity**: 2 (Số nhánh điều kiện trong hàm).
2. **Gợi ý Refactor**: "Có thể sử dụng thêm exception handling để xử lý trường hợp b^2 < 4ac."
3. **Biểu đồ CFG**: Hiển thị luồng điều khiển của hàm `giai_pt_bac_2`.
4. **Biểu đồ độ phức tạp**: Mức độ phức tạp của từng hàm sẽ được hiển thị dưới dạng biểu đồ thanh.

---

## ⚙️ Các file trong dự án

- **`main.py`**: File chính để chạy ứng dụng Streamlit.
- **`analyzer/complexity_analyzer.py`**: Xử lý phân tích độ phức tạp mã nguồn.
- **`utils/gpt_helper.py`**: Xử lý việc gọi **API Gemini** và lấy gợi ý refactor.
- **`utils/cfg_drawer.py`**: Sinh và vẽ **Control Flow Graph (CFG)**.
- **`utils/loc_counter.py`**: Đếm số dòng mã (LOC) và dòng comment.
- **`requirements.txt`**: File chứa các thư viện cần thiết cho dự án.

---

## 🔧 Các yêu cầu hệ thống

- Python 3.6 trở lên.
- Các thư viện Python: Streamlit, NetworkX, Matplotlib, Google Gemini API.

---

## Tác giả

- **hungnguyen26** - *Initial work and maintenance*

---
*Đăng nhập người dùng hiện tại: hungnguyen26*
