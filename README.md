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
  - [Mirror](#mirror)
  - [Features](#features)
- **[Project](#project)**
  - [#1: Basic Packet Sniffer](#packetsniffer)
    - [Option 1: Python](#packetsniffer---option-1-python)
  - [#2: ](#configuring)
  - [#3: ](#developing)
- **[Community](#community)**
  - [Contributing](#contributing)
  - [Bugs](#reporting-bugs)
  - [Support](#supporting)
- **[License](#license)**

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


