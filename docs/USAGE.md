
## 2. **docs/USAGE.md**

```markdown
# Usage Guide

## Quick Start

```bash
# Basic packet capture (default interface)
sudo python src/cli_interface.py

# Capture on specific interface
sudo python src/cli_interface.py --interface wlan0

# Capture limited number of packets
sudo python src/cli_interface.py --count 100

# Verbose output with alerts
sudo python src/cli_interface.py --interface eth0 --verbose
