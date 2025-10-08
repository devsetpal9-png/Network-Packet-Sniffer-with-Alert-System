import sqlite3
from datetime import datetime
import os

class DatabaseManager:
    def __init__(self, db_path="data/network_traffic.db"):
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        self.db_path = db_path
        self.init_database()
        
    def init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Packets table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                src_ip TEXT,
                dst_ip TEXT,
                src_port INTEGER,
                dst_port INTEGER,
                protocol TEXT,
                length INTEGER,
                flags TEXT,
                anomaly_detected BOOLEAN DEFAULT FALSE
            )
        ''')
        
        # Alerts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                alert_type TEXT,
                severity TEXT,
                source_ip TEXT,
                description TEXT,
                packet_info TEXT
            )
        ''')
        
        # Statistics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS statistics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                total_packets INTEGER,
                tcp_packets INTEGER,
                udp_packets INTEGER,
                icmp_packets INTEGER,
                suspicious_activities INTEGER
            )
        ''')
        
        conn.commit()
        conn.close()
        
    def insert_packet(self, packet_info):
        """Insert packet information into database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO packets 
            (timestamp, src_ip, dst_ip, src_port, dst_port, protocol, length, flags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            packet_info['timestamp'],
            packet_info['src_ip'],
            packet_info['dst_ip'],
            packet_info['src_port'],
            packet_info['dst_port'],
            packet_info['protocol'],
            packet_info['length'],
            packet_info['flags']
        ))
        
        conn.commit()
        conn.close()
    
    def insert_alert(self, alert_type, severity, source_ip, description, packet_info):
        """Insert alert into database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO alerts 
            (timestamp, alert_type, severity, source_ip, description, packet_info)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            datetime.now(),
            alert_type,
            severity,
            source_ip,
            description,
            str(packet_info)
        ))
        
        conn.commit()
        conn.close()
    
    def get_recent_packets(self, limit=100):
        """Get recent packets from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM packets ORDER BY timestamp DESC LIMIT ?
        ''', (limit,))
        
        packets = cursor.fetchall()
        conn.close()
        return packets
    
    def get_alerts(self, limit=50):
        """Get recent alerts from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM alerts ORDER BY timestamp DESC LIMIT ?
        ''', (limit,))
        
        alerts = cursor.fetchall()
        conn.close()
        return alerts
