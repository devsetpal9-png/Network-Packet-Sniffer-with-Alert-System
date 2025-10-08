import argparse
import sys
from packet_sniffer import PacketSniffer
from alert_system import AlertSystem
from database_manager import DatabaseManager
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

class CLIInterface:
    def __init__(self):
        self.sniffer = None
        self.alert_system = AlertSystem()
        
    def handle_alert(self, anomaly_type, packet_info):
        """Handle incoming alerts"""
        self.alert_system.send_alert(anomaly_type, packet_info)
        
    def start_sniffing(self, interface=None, count=0):
        """Start the packet sniffer"""
        print("🚀 Starting Network Packet Sniffer with Alert System")
        print("Press Ctrl+C to stop sniffing")
        
        self.sniffer = PacketSniffer(interface=interface, alert_callback=self.handle_alert)
        
        try:
            self.sniffer.start_sniffing(packet_count=count)
        except KeyboardInterrupt:
            self.sniffer.stop_sniffing()
            self.show_statistics()
            
    def show_statistics(self):
        """Display sniffing statistics"""
        if self.sniffer:
            stats = self.sniffer.get_statistics()
            print("\n" + "="*50)
            print("SNIFFING STATISTICS")
            print("="*50)
            print(f"Total Packets: {stats['total_packets']}")
            print(f"TCP Packets: {stats['tcp_packets']}")
            print(f"UDP Packets: {stats['udp_packets']}")
            print(f"ICMP Packets: {stats['icmp_packets']}")
            print(f"Suspicious Activities: {stats['suspicious_activities']}")
            print(f"Duration: {stats['duration_seconds']:.2f} seconds")
            print(f"Packets/Second: {stats['packets_per_second']:.2f}")
            
    def show_recent_packets(self, limit=20):
        """Show recent packets from database"""
        db_manager = DatabaseManager()
        packets = db_manager.get_recent_packets(limit)
        
        print(f"\n{'='*60}")
        print(f"RECENT PACKETS (Last {limit})")
        print(f"{'='*60}")
        print(f"{'Time':<20} {'Source IP':<15} {'Dest IP':<15} {'Protocol':<8} {'Length':<6}")
        print(f"{'-'*60}")
        
        for packet in packets:
            timestamp = packet[1][11:19]  # Extract time only
            print(f"{timestamp:<20} {packet[2]:<15} {packet[3]:<15} {packet[6]:<8} {packet[7]:<6}")
            
    def show_alerts(self, limit=10):
        """Show recent alerts"""
        db_manager = DatabaseManager()
        alerts = db_manager.get_alerts(limit)
        
        print(f"\n{'='*70}")
        print(f"RECENT ALERTS (Last {limit})")
        print(f"{'='*70}")
        print(f"{'Time':<20} {'Type':<15} {'Severity':<10} {'Source IP':<15}")
        print(f"{'-'*70}")
        
        for alert in alerts:
            timestamp = alert[1][11:19]
            print(f"{timestamp:<20} {alert[2]:<15} {alert[3]:<10} {alert[4]:<15}")
            
    def generate_traffic_report(self, hours=1):
        """Generate traffic summary report"""
        conn = DatabaseManager().conn
        query = """
        SELECT 
            strftime('%H:%M', timestamp) as time_window,
            COUNT(*) as packet_count,
            SUM(CASE WHEN protocol = 'TCP' THEN 1 ELSE 0 END) as tcp_count,
            SUM(CASE WHEN protocol = 'UDP' THEN 1 ELSE 0 END) as udp_count,
            SUM(CASE WHEN anomaly_detected = 1 THEN 1 ELSE 0 END) as anomaly_count
        FROM packets 
        WHERE timestamp >= datetime('now', ?)
        GROUP BY time_window
        ORDER BY time_window
        """
        
        df = pd.read_sql_query(query, conn, params=(f'-{hours} hours',))
        
        if not df.empty:
            plt.figure(figsize=(12, 8))
            
            plt.subplot(2, 2, 1)
            plt.plot(df['time_window'], df['packet_count'], 'b-', label='Total Packets')
            plt.title('Total Packets Over Time')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 2, 2)
            plt.bar(df['time_window'], df['tcp_count'], alpha=0.7, label='TCP')
            plt.bar(df['time_window'], df['udp_count'], alpha=0.7, label='UDP')
            plt.title('Protocol Distribution')
            plt.xticks(rotation=45)
            plt.legend()
            
            plt.subplot(2, 2, 3)
            plt.plot(df['time_window'], df['anomaly_count'], 'r-', label='Anomalies')
            plt.title('Anomalies Detected')
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            plt.savefig('traffic_report.png')
            print("📊 Traffic report saved as 'traffic_report.png'")
        else:
            print("No data available for the specified time period.")

def main():
    parser = argparse.ArgumentParser(description='Network Packet Sniffer with Alert System')
    parser.add_argument('--interface', '-i', help='Network interface to sniff on')
    parser.add_argument('--count', '-c', type=int, default=0, help='Number of packets to capture (0 for infinite)')
    parser.add_argument('--show-packets', action='store_true', help='Show recent packets from database')
    parser.add_argument('--show-alerts', action='store_true', help='Show recent alerts')
    parser.add_argument('--generate-report', action='store_true', help='Generate traffic report')
    
    args = parser.parse_args()
    cli = CLIInterface()
    
    if args.show_packets:
        cli.show_recent_packets()
    elif args.show_alerts:
        cli.show_alerts()
    elif args.generate_report:
        cli.generate_traffic_report()
    else:
        cli.start_sniffing(interface=args.interface, count=args.count)

if __name__ == "__main__":
    main()
