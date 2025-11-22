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
