# Installation Guide

## Prerequisites

- **Python 3.8 or higher**
- **Administrative/root privileges** (for packet capture)
- **Supported Operating Systems:**
  - Linux (Recommended)
  - Windows 10/11
  - macOS

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/network-packet-sniffer.git
cd network-packet-sniffer
```
### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run Setup Script
```bash
python setup.py
```
### 4. Verify Installation
```bash
python src/cli_interface.py --help
```
## Platform-Specific Setup

### 🐧 Linux (Ubuntu/Debian)
```bash
# Install required system packages
sudo apt-get update
sudo apt-get install libpcap-dev tcpdump

# Run the sniffer
sudo python src/cli_interface.py --interface eth0
```
### 🪟 Windows
```cmd
python src/cli_interface.py --interface "Ethernet"
```
### 🍎 macOS
```bash
# Install required tools
xcode-select --install

# Run with sudo
sudo python src/cli_interface.py --interface en0
```
