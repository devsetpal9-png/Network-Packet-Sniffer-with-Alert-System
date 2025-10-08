
## 6. **docs/FAQ.md**

```markdown
# Frequently Asked Questions

## General Questions

### What is this project for?
This is a network security monitoring tool that captures and analyzes network traffic in real-time, detecting potential security threats and anomalies.

### Is this legal to use?
Yes, when used properly. Only monitor networks you own or have explicit permission to monitor. Unauthorized network monitoring may be illegal.

### What platforms are supported?
- Linux (Recommended)
- Windows 10/11
- macOS

## Technical Questions

### Why do I need admin/root privileges?
Packet capture requires low-level network access that typically needs elevated permissions.

### How do I find my network interface names?
**Linux/macOS:**
```bash
ip link show
# or
ifconfig
