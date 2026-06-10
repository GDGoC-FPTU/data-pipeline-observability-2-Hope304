[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24113017&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** 26ai.hungnd3@vinuni.edu.vn 
**Name:** Nguyễn Duy Hưng 

---

## Mo ta
Bài lab này xây dựng một ETL pipeline đơn giản bằng Python và Pandas để xử lý dữ liệu sản phẩm từ file `raw_data.json`.
Pipeline gồm 4 bước chính:

1. **Extract:** Đọc dữ liệu nguồn từ file JSON.
2. **Validate:** Kiểm tra chất lượng dữ liệu và loại bỏ các record không hợp lệ, bao gồm:
   - Giá sản phẩm `price <= 0`.
   - Category bị rỗng hoặc thiếu.
3. **Transform:** Chuẩn hóa dữ liệu hợp lệ:
   - Tính cột `discounted_price` với mức giảm giá 10%.
   - Chuẩn hóa `category` sang dạng Title Case.
   - Thêm cột `processed_at` để ghi nhận thời điểm xử lý.
4. **Load:** Lưu dữ liệu đã xử lý vào file `processed_data.csv`.

Ngoài ra, project có phần mô phỏng AI Agent trong `agent_simulation.py` để so sánh tác động của dữ liệu sạch và dữ liệu rác đối với câu trả lời của agent.
---

## Cach chay (How to Run)

### Prerequisites

Cai dat thu vien can thiet:

```bash
pip install pandas
```

### Chay ETL Pipeline


```bash
python solution.py
```


### Chay Agent Simulation (Stress Test)

```bash
python agent_simulation.py
```

Thi nghiem nay dung 2 bo du lieu:

- **Clean Data:** `processed_data.csv` duoc tao tu pipeline sau khi da validate va transform.
- **Garbage Data:** `garbage_data.csv` chua cac van de nhu duplicate ID, sai kieu du lieu, outlier, null value va category rong.

Agent se tra loi cau hoi:

```text
What is the best electronic product?
```

Muc tieu la quan sat viec du lieu kem chat luong co the lam agent dua ra cau tra loi sai hoac khong dang tin cay.

---

## Cau truc thu muc

```text
├── solution.py              # ETL Pipeline script
├── processed_data.csv       # Output cua pipeline                                                                                                          
├── experiment_report.md     # Bao cao thi nghiem                                                                                                           
└── README.md                # File nay  
```

---

## Ket qua

SSau khi chạy pipeline với dữ liệu trong `raw_data.json`:

- Tổng số record ban đầu: **5**
- Số record hợp lệ được giữ lại: **3**
- Số record bị loại: **2**
  - Record có `price <= 0`: **1**
  - Record thiếu/rỗng `category`: **1**
- File output: `processed_data.csv`

---

## Các record hợp lệ sau khi xử lý:

| id | product | price | category | discounted_price |
|----|---------|-------|----------|------------------|
| 1 | Laptop | 1200 | Electronics | 1080.0 |
| 2 | Chair | 45 | Furniture | 40.5 |
| 5 | Monitor | 300 | Electronics | 270.0 |

---

## Nhận xét

Pipeline giúp đảm bảo dữ liệu đầu vào có chất lượng tốt hơn trước khi được sử dụng bởi hệ thống phân tích hoặc AI Agent. Nếu dữ liệu bị lỗi như sai kiểu dữ liệu, duplicate ID, giá trị quá lớn bất thường hoặc thiếu category, agent có thể đưa ra câu trả lời sai. Vì vậy, data validation và observability là bước quan trọng trong mọi data pipeline.
