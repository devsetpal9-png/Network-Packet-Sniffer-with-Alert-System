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
git clone https://github.com/YOUR_USERNAME/network-packet-sniffer.git
cd network-packet-sniffer

# Install dependencies
pip install -r requirements.txt

# Run with admin privileges
sudo python src/cli_interface.py --help
