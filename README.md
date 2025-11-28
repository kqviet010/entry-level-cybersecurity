<h1 align="center">CyberSecurity Projects</h1>


<p align="center">
<img src="https://i.ibb.co/d0M0R81j/6420571.jpg" width="96" /><br />
<b><i>Entry-level Security</i></b>
<br />
<b>🌐 <a href="https://github.com/kqviet010/entry-level-cybersecurity">kqviet010</a></b><br />

</p>

---
<p align="center">
  <sup>Kindly supported by:</sup><br>
<a href="https://github.com/kqviet010/entry-level-cybersecurity">
  <img src="https://i.ibb.co/JWnSzt5c/122.png" width="300" alt="GitHub">
  <br>
  <strong>The $HOME of all things in the terminal.</strong>
</a>
</p>

---

#### Contents

- **[About](#about)**
  - [Screenshot](#screenshot)
  - [Live Demo](#live-demo)
  - [Features](#features)
- **[Project](#project)**
  - [#1: Basic Packet Sniffer](#packetsniffer)
    - [Option 1: Python](#packetsniffer---option-1-python)
  - [#2: Basic Sender Email](#configuring)
  - [#3: ](#developing)

---

## About
This project is a lightweight web reconnaissance tool designed to help beginners understand the fundamentals of Passive Reconnaissance and OSINT (Open Source Intelligence).

The goal of this tool is to automate the gathering of publicly available information about a target website. By analyzing server headers, SSL configurations, and DNS records, this dashboard helps visualize the "attack surface" of a web application.

Current capabilities:

- Infrastructure Analysis: Identifies server location, IP data, and associated hostnames.

- Security Auditing: Scans for insecure HTTP headers and cookie attributes.

- Network Mapping: Performs traceroutes and open port detection to map the network path.


## #Project 1: Basic Packet Sniffer
```bash
#!/usr/bin/env python3
import scapy.all as scapy

def sniff_packets(interface):
    # store=False tells Scapy not to keep packets in memory (saves RAM)
    # prn=process_packet tells Scapy to send every packet to our function
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    # Check if the packet has an IP layer to avoid errors with non-IP traffic
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        
        print(f"[+] New Packet: {src_ip} -> {dst_ip} | Protocol: {protocol}")

        # If it's a TCP packet, we can look deeper (optional)
        if packet.haslayer(scapy.TCP):
             src_port = packet[scapy.TCP].sport
             dst_port = packet[scapy.TCP].dport
             print(f"    L Port: {src_port} -> {dst_port}")

# --- Main Execution ---
# "eth0" is usually the default connection in Kali VMs. 
# If you are on WiFi, change "eth0" to "wlan0"
interface_name = "eth0" 

print(f"[*] Starting Sniffer on {interface_name}...")
sniff_packets(interface_name)
```

## #Project 2: Basic Sender Email
```bash
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
    EMAIL_CUA_BAN = "ngoisaouocmo010@gmail.com"
    MAT_KHAU_APP = "ntnw jsit ifsi xxxx" #

    gui_email_kem_json(EMAIL_CUA_BAN, MAT_KHAU_APP)
```


