from collections import defaultdict, deque
import time
from datetime import datetime

class AnomalyDetector:
    def __init__(self):
        # Port scanning detection
        self.port_scan_threshold = 10  # ports per second
        self.src_ports = defaultdict(lambda: deque(maxlen=100))
        
        # Flooding detection
        self.packet_flood_threshold = 100  # packets per second
        self.src_packets = defaultdict(lambda: deque(maxlen=1000))
        
        # Suspicious ports
        self.suspicious_ports = {21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1433, 3306, 3389, 5432}
        
    def analyze_packet(self, packet_info):
        """Analyze packet for anomalies"""
        anomalies = []
        
        # Check for port scanning
        if self.detect_port_scan(packet_info):
            anomalies.append("PORT_SCAN")
            
        # Check for packet flooding
        if self.detect_packet_flood(packet_info):
            anomalies.append("PACKET_FLOOD")
            
        # Check for suspicious ports
        if self.detect_suspicious_port(packet_info):
            anomalies.append("SUSPICIOUS_PORT")
            
        # Check for unusual flags
        if self.detect_unusual_flags(packet_info):
            anomalies.append("UNUSUAL_FLAGS")
            
        return anomalies if anomalies else None
    
    def detect_port_scan(self, packet_info):
        """Detect port scanning activity"""
        if not packet_info['src_ip'] or not packet_info['dst_port']:
            return False
            
        current_time = time.time()
        self.src_ports[packet_info['src_ip']].append((packet_info['dst_port'], current_time))
        
        # Check if same source IP is scanning multiple ports
        ports = self.src_ports[packet_info['src_ip']]
        recent_ports = [(port, ts) for port, ts in ports if current_time - ts < 5]  # 5-second window
        
        unique_ports = len(set(port for port, ts in recent_ports))
        
        return unique_ports > self.port_scan_threshold
    
    def detect_packet_flood(self, packet_info):
        """Detect packet flooding (DDoS attempt)"""
        if not packet_info['src_ip']:
            return False
            
        current_time = time.time()
        self.src_packets[packet_info['src_ip']].append(current_time)
        
        # Count packets in last second
        packets = self.src_packets[packet_info['src_ip']]
        recent_packets = [ts for ts in packets if current_time - ts < 1]
        
        return len(recent_packets) > self.packet_flood_threshold
    
    def detect_suspicious_port(self, packet_info):
        """Detect connections to suspicious ports"""
        if packet_info['dst_port'] in self.suspicious_ports:
            return True
        return False
    
    def detect_unusual_flags(self, packet_info):
        """Detect packets with unusual TCP flags"""
        if packet_info['protocol'] == 'TCP' and packet_info['flags']:
            # Check for NULL scan
            if packet_info['flags'] == '0':
                return True
            # Check for XMAS scan
            if 'F' in packet_info['flags'] and 'P' in packet_info['flags'] and 'U' in packet_info['flags']:
                return True
        return False
