# Network Packet Sniffer with Alert System 🔍🚨

A professional real-time network traffic monitoring tool with advanced anomaly detection capabilities, built for cybersecurity analysis and network monitoring.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)

## Features ✨

- **Real-time Packet Capture**: Monitor network traffic on any interface
- **Advanced Anomaly Detection**: Detect port scanning, packet flooding, and suspicious activities
- **Multi-channel Alert System**: Real-time alerts via console, logs, and email
- **Data Persistence**: SQLite database for packet logging and analysis
- **Traffic Visualization**: Generate interactive reports and graphs
- **CLI & GUI Interfaces**: Flexible user interfaces for different use cases
- **Modular Architecture**: Easy to extend and customize

## Installation 🚀

### Prerequisites
- Python 3.8 or higher
- Administrative/root privileges for packet capture

### Quick Start
```bash
# Clone the repository
git clone https://github.com/devsetpal9-png/Network-Packet-Sniffer-with-Alert-System.git
cd Network-Packet-Sniffer-with-Alert-System

# Install dependencies
pip install -r requirements.txt

# Run with admin privileges
sudo python src/cli_interface.py --help
```

---

## Usage 📖

### Basic Packet Sniffing
```bash
sudo python src/cli_interface.py --interface eth0
```

### Capture Specific Number of Packets
```bash
sudo python src/cli_interface.py --count 100 --interface wlan0
```

### View Recent Packets
```bash
python src/cli_interface.py --show-packets
```

### View Security Alerts
```bash
python src/cli_interface.py --show-alerts
```

### Generate Traffic Report
```bash
python src/cli_interface.py --generate-report
```
---

## Project Structure 🏗️
```
Network-Packet-Sniffer-with-Alert-System/
├── src/                    # Source code
│   ├── packet_sniffer.py   # Core packet capture engine
│   ├── anomaly_detector.py # Anomaly detection algorithms
│   ├── database_manager.py # Database operations
│   ├── alert_system.py     # Alert management
│   ├── cli_interface.py    # Command-line interface
│   └── gui_dashboard.py    # Graphical interface (optional)
├── data/                   # Database files (auto-generated)
├── docs/                   # Documentation
├── tests/                  # Unit tests
├── requirements.txt        # Python dependencies
├── config.py              # Configuration settings
└── README.md              # Project documentation
```
