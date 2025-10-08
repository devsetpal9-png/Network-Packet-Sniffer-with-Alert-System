# Configuration for Network Packet Sniffer

# Sniffer Configuration
SNIFFER_CONFIG = {
    'default_interface': None,  # None for default interface
    'packet_count': 0,  # 0 for infinite
}

# Alert Configuration
ALERT_CONFIG = {
    'email_alerts': False,  # Enable email alerts
    'smtp': {
        'server': 'smtp.gmail.com',
        'port': 587,
        'username': 'your_email@gmail.com',
        'password': 'your_app_password',
        'to_email': 'recipient@gmail.com'
    }
}

# Anomaly Detection Thresholds
DETECTION_CONFIG = {
    'port_scan_threshold': 10,  # ports per second
    'packet_flood_threshold': 100,  # packets per second
}

# Database Configuration
DATABASE_CONFIG = {
    'path': 'data/network_traffic.db',
    'cleanup_days': 30  # Auto-delete records older than X days
}
