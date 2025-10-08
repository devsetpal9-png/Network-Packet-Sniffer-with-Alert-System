
## 8. **docs/SECURITY.md**

```markdown
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Active support  |

## Reporting a Vulnerability

**Please do NOT open GitHub issues for security vulnerabilities.**

### Private Reporting Process
1. Email: your-email@example.com
2. Describe the vulnerability
3. Include steps to reproduce
4. We'll respond within 48 hours

### What to Include
- Vulnerability description
- Potential impact
- Steps to reproduce
- Suggested fix (if any)

## Security Considerations

### Data Handling
- Packet payloads are not captured by default
- All data stored locally
- No external data transmission without configuration

### Access Controls
- Requires explicit user permissions
- No automatic privilege escalation
- Clear documentation of required privileges

### Network Security
- Operates in passive monitoring mode
- Does not transmit packets
- No network service exposure

## Best Practices for Users

### Secure Deployment
1. **Run with minimum required privileges**
2. **Store data in secure locations**
3. **Regularly update dependencies**
4. **Monitor access logs**

### Network Monitoring Ethics
1. **Only monitor authorized networks**
2. **Respect privacy laws and regulations**
3. **Secure captured data appropriately**
4. **Obtain proper permissions**

## Dependency Security

We regularly monitor and update dependencies for security patches. See `requirements.txt` for current versions.
