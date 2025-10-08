
## 7. **docs/TROUBLESHOOTING.md**

```markdown
# Troubleshooting Guide

## Common Issues and Solutions

### Permission Errors

**Issue:** `PermissionError: [Errno 1] Operation not permitted`

**Solutions:**
- **Linux/macOS**: Use `sudo`
- **Windows**: Run as Administrator
- **Check specific permissions**: `ls -l /dev/bpf*` (macOS)

### Interface Not Found

**Issue:** `OSError: [Errno 19] No such device`

**Solutions:**
1. List available interfaces:
```bash
python -c "from scapy.all import get_if_list; print(get_if_list())"
