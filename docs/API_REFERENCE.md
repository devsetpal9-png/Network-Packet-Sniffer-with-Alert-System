# API Reference

## PacketSniffer Class

### Constructor
```python
PacketSniffer(interface=None, alert_callback=None)
Parameters:

interface (str): Network interface name

alert_callback (callable): Function to handle alerts

Methods
start_sniffing(packet_count=0)
Starts packet capture.

Parameters:

packet_count (int): Number of packets to capture (0=infinite)

stop_sniffing()
Stops packet capture.

get_statistics()
Returns capture statistics.

Returns: dict with packet counts and timing information

AnomalyDetector Class
Methods
analyze_packet(packet_info)
Analyzes packet for security anomalies.

Parameters:

packet_info (dict): Packet metadata

Returns: List of detected anomaly types or None

Configuration Methods
set_port_scan_threshold(threshold)

set_flood_threshold(threshold)

add_suspicious_port(port)

DatabaseManager Class
Methods
insert_packet(packet_info)
Stores packet data in database.

get_recent_packets(limit=50)
Retrieves recent packets.

insert_alert(alert_data)
Stores security alert.

AlertSystem Class
Methods
send_alert(alert_type, packet_info, severity="MEDIUM")
Sends security alert through configured channels.

configure_email_smtp(smtp_config)
Configures email alert settings.
