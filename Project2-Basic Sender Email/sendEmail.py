#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Lấy đường dẫn thư mục chứa file code này
# Giúp tránh lỗi "File not found" khi chạy bằng Cron trên Linux
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- 1. HÀM TẠO FILE JSON GIẢ LẬP ---
def tao_file_json_demo():
    # File sẽ được lưu cùng thư mục với script
    ten_file = os.path.join(BASE_DIR, "ket_qua_scan.json")
    
    data = {
        "id_may_tram": "Linux_Server_01",
        "he_dieu_hanh": "Ubuntu/CentOS",
        "trang_thai": "Hoat dong tot",
        "nhiet_do_cpu": 45.5,
        "thong_tin_admin": {
            "ten": "Admin Linux",
            "email": "admin@example.com"
        }
    }
    
    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"1️⃣  Đã tạo file tại: {ten_file}")
    return ten_file

# --- 2. HÀM GỬI EMAIL ---
def gui_email_kem_json(my_email, my_app_pass):
    smtp_server = "smtp.gmail.com"
    port = 587
    
    file_path = tao_file_json_demo()

    try:
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = my_email
        msg['Subject'] = "🐧 Báo cáo từ Linux Server (JSON)"
        
        body = "Chào bạn,\n\nĐây là báo cáo tự động gửi từ máy chủ Linux.\nFile JSON được đính kèm bên dưới.\n"
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Đính kèm file
        if os.path.exists(file_path):
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            
            # Chỉ lấy tên file (bỏ đường dẫn dài dòng) để hiển thị trong mail
            ten_file_hien_thi = os.path.basename(file_path)
            
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {ten_file_hien_thi}",
            )
            msg.attach(part)
        else:
            print("⚠️ Không tìm thấy file JSON để đính kèm!")

        # Gửi mail
        print("2️⃣  Đang kết nối server Gmail...")
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        
        print("3️⃣  Đang đăng nhập...")
        server.login(my_email, my_app_pass)
        
        print(f"4️⃣  Đang gửi đến {my_email}...")
        server.sendmail(my_email, my_email, msg.as_string())
        
        print("\n✅ THÀNH CÔNG! Đã gửi mail trên Linux.")

    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        
    finally:
        try:
            server.quit()
        except:
            pass
        
        # Dọn dẹp file tạm trên Linux (Bỏ comment dòng dưới nếu muốn xóa file sau khi gửi)
        # if os.path.exists(file_path):
        #     os.remove(file_path)

# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    # ⚠️ HÃY DÙNG MẬT KHẨU MỚI, KHÔNG DÙNG CÁI CŨ ĐÃ LỘ
    EMAIL_CUA_BAN = "ngoisaouocmo010@gmail.com"
    MAT_KHAU_APP = "ntnw jsit ifsi rrjy" # <-- Điền lại mật khẩu mới vào đây

    gui_email_kem_json(EMAIL_CUA_BAN, MAT_KHAU_APP)