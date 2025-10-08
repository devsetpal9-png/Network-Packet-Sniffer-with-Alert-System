from scapy.all import sniff, IP, TCP, UDP, ICMP
import sqlite3
from datetime import datetime
from anomaly_detector import AnomalyDetector
from database_manager import DatabaseManager
import threading
from collections import defaultdict
import time

class PacketSniffer:
    def __init__(self, interface=None, alert_callback=None):
        self.interface = interface
        self.alert_callback = alert_callback
        self.db_manager = DatabaseManager()
        self.anomaly_detector = AnomalyDetector()
        self.is_sniffing = False
        self.packet_count = 0
        self.start_time = None
        
        # Statistics
        self.stats = {
            'total_packets': 0,
            'tcp_packets': 0,
            'udp_packets': 0,
            'icmp_packets': 0,
            'suspicious_activities': 0
        }
        
    def start_sniffing(self, packet_count=0):
        """Start packet sniffing"""
        self.is_sniffing = True
        self.start_time = datetime.now()
        print(f"[+] Starting packet sniffer on interface {self.interface or 'default'}")
        
        try:
            sniff(iface=self.interface, 
                  prn=self.process_packet, 
                  count=packet_count,
                  store=False)
        except Exception as e:
            print(f"[-] Error starting sniffer: {e}")
            
    def stop_sniffing(self):
        """Stop packet sniffing"""
        self.is_sniffing = False
        print("[+] Stopping packet sniffer")
        
    def process_packet(self, packet):
        """Process each captured packet"""
        if not self.is_sniffing:
            return
            
        self.packet_count += 1
        self.stats['total_packets'] += 1
        
        packet_info = self.extract_packet_info(packet)
        
        if packet_info:
            # Store in database
            self.db_manager.insert_packet(packet_info)
            
            # Check for anomalies
            anomaly_detected = self.anomaly_detector.analyze_packet(packet_info)
            
            if anomaly_detected:
                self.stats['suspicious_activities'] += 1
                if self.alert_callback:
                    self.alert_callback(anomaly_detected, packet_info)
                    
    def extract_packet_info(self, packet):
        """Extract relevant information from packet"""
        packet_info = {
            'timestamp': datetime.now(),
            'src_ip': None,
            'dst_ip': None,
            'src_port': None,
            'dst_port': None,
            'protocol': None,
            'length': len(packet),
            'flags': None
        }
        
        if IP in packet:
            packet_info['src_ip'] = packet[IP].src
            packet_info['dst_ip'] = packet[IP].dst
            
            if TCP in packet:
                packet_info['protocol'] = 'TCP'
                packet_info['src_port'] = packet[TCP].sport
                packet_info['dst_port'] = packet[TCP].dport
                packet_info['flags'] = str(packet[TCP].flags)
                self.stats['tcp_packets'] += 1
                
            elif UDP in packet:
                packet_info['protocol'] = 'UDP'
                packet_info['src_port'] = packet[UDP].sport
                packet_info['dst_port'] = packet[UDP].dport
                self.stats['udp_packets'] += 1
                
            elif ICMP in packet:
                packet_info['protocol'] = 'ICMP'
                self.stats['icmp_packets'] += 1
                
        return packet_info
    
    def get_statistics(self):
        """Get current statistics"""
        duration = datetime.now() - self.start_time if self.start_time else 0
        return {
            **self.stats,
            'duration_seconds': duration.total_seconds() if duration else 0,
            'packets_per_second': self.stats['total_packets'] / duration.total_seconds() if duration and duration.total_seconds() > 0 else 0
        }
