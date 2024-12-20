import pdfplumber
import json

# Đường dẫn tới file PDF
file_path = 'FRT_INVNAIC0267284_9Billing.pdf'

# Danh sách để chứa tất cả các bảng
all_tables = []

# Mở file PDF
with pdfplumber.open(file_path) as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()  # Trích xuất bảng
        
        # Xử lý các bảng
        if tables:
            for table_index, table in enumerate(tables):
                json_table = []
                
                for row in table:
                    # Lưu mỗi hàng vào danh sách
                    json_table.append({"data": row})

                # Thêm bảng vào danh sách tổng
                all_tables.append({"page": i + 1, "table_index": table_index + 1, "data": json_table})

# Lưu tất cả bảng vào một file JSON
with open('all_tables_.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_tables, json_file, ensure_ascii=False, indent=4)
'''
import pdfplumber
import json

# Đường dẫn tới file PDF
file_path = 'FRT_INVNAIC0293419_5Billing.pdf'

# Danh sách để chứa tất cả các bảng
all_tables = []

# Mở file PDF
with pdfplumber.open(file_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()  # Trích xuất văn bản

        # Lưu nội dung văn bản vào file
        if text:
            with open(f'file_text_{i + 1}.txt', 'w', encoding='utf-8') as text_file:
                text_file.write(text)

        tables = page.extract_tables()  # Trích xuất bảng
        
        # Xử lý các bảng
        if tables:
            for table_index, table in enumerate(tables):
                print(f"Bảng {table_index + 1} trên trang {i + 1}:")
                
                # Chuyển đổi bảng thành danh sách từ điển
                headers = table[0]  # Giả định hàng đầu tiên là tiêu đề
                json_table = []
                
                for row in table[1:]:  # Bỏ qua hàng tiêu đề
                    json_table.append({headers[j]: row[j] for j in range(len(headers))})
                
                # Thêm bảng vào danh sách tổng
                all_tables.append({"page": i + 1, "table_index": table_index + 1, "data": json_table})

# Lưu tất cả bảng vào một file JSON
with open('all_tables_.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_tables, json_file, ensure_ascii=False, indent=4)

import PyPDF2

# Đường dẫn tới file PDF
file_path = 'FRT_INVNAIC0267284_9Billing.pdf'

# Mở file PDF
with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Lấy số trang trong PDF
    num_pages = len(reader.pages)
    print(f"Số trang: {num_pages}")

    # Đọc nội dung từng trang
    i=0
    for page in range(num_pages):
        text = reader.pages[page].extract_text()
        print(f"Nội dung trang {page + 1}:\n{text}\n")
        
        with open(f'file9{i+1}.txt','w',encoding='utf-8') as file:
          file.write(text)
        i+=1      
'''