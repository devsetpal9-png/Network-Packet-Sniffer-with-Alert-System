import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
import logging
from database_manager import DatabaseManager

class AlertSystem:
    def __init__(self, config=None):
        self.config = config or {}
        self.db_manager = DatabaseManager()
        
        # Setup logging
        logging.basicConfig(
            filename='network_sniffer.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()
        
    def send_alert(self, anomaly_type, packet_info):
        """Send alert for detected anomaly"""
        severity = self.determine_severity(anomaly_type)
        description = self.generate_alert_description(anomaly_type, packet_info)
        
        # Log alert
        self.logger.warning(f"ALERT: {anomaly_type} - {description}")
        
        # Store in database
        self.db_manager.insert_alert(
            anomaly_type, 
            severity, 
            packet_info.get('src_ip', 'Unknown'), 
            description, 
            packet_info
        )
        
        # Send email alert if configured
        if self.config.get('email_alerts', False):
            self.send_email_alert(anomaly_type, severity, description, packet_info)
            
        # Print to console
        print(f"🚨 ALERT [{severity}]: {anomaly_type} - {description}")
    
    def determine_severity(self, anomaly_type):
        """Determine severity level for different anomaly types"""
        severity_map = {
            'PORT_SCAN': 'HIGH',
            'PACKET_FLOOD': 'HIGH',
            'SUSPICIOUS_PORT': 'MEDIUM',
            'UNUSUAL_FLAGS': 'MEDIUM'
        }
        return severity_map.get(anomaly_type, 'LOW')
    
    def generate_alert_description(self, anomaly_type, packet_info):
        """Generate descriptive alert message"""
        descriptions = {
            'PORT_SCAN': f"Port scanning detected from {packet_info.get('src_ip', 'Unknown')}",
            'PACKET_FLOOD': f"Packet flooding detected from {packet_info.get('src_ip', 'Unknown')}",
            'SUSPICIOUS_PORT': f"Connection to suspicious port {packet_info.get('dst_port', 'Unknown')}",
            'UNUSUAL_FLAGS': f"Unusual TCP flags: {packet_info.get('flags', 'Unknown')}"
        }
        return descriptions.get(anomaly_type, "Unknown anomaly detected")
    
    def send_email_alert(self, anomaly_type, severity, description, packet_info):
        """Send email alert (requires SMTP configuration)"""
        try:
            smtp_config = self.config.get('smtp', {})
            
            if not all(key in smtp_config for key in ['server', 'port', 'username', 'password', 'to_email']):
                return
                
            msg = MimeMultipart()
            msg['From'] = smtp_config['username']
            msg['To'] = smtp_config['to_email']
            msg['Subject'] = f"Network Security Alert: {anomaly_type}"
            
            body = f"""
            Network Security Alert
            
            Type: {anomaly_type}
            Severity: {severity}
            Description: {description}
            
            Packet Details:
            - Source IP: {packet_info.get('src_ip', 'Unknown')}
            - Destination IP: {packet_info.get('dst_ip', 'Unknown')}
            - Protocol: {packet_info.get('protocol', 'Unknown')}
            - Timestamp: {packet_info.get('timestamp', 'Unknown')}
            
            This is an automated alert from your Network Packet Sniffer.
            """
            
            msg.attach(MimeText(body, 'plain'))
            
            server = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
            server.starttls()
            server.login(smtp_config['username'], smtp_config['password'])
            server.send_message(msg)
            server.quit()
            
            self.logger.info(f"Email alert sent for {anomaly_type}")
            
        except Exception as e:
            self.logger.error(f"Failed to send email alert: {e}")
