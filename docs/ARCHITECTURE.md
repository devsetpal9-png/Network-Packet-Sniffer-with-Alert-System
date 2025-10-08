
## 3. **docs/ARCHITECTURE.md**

```markdown
# System Architecture

## Overview

The Network Packet Sniffer is built with a modular, extensible architecture that separates concerns and allows for easy maintenance and feature additions.

## Component Diagram
┌─────────────────┐ ┌──────────────────┐ ┌─────────────────┐
│ Packet │ │ Anomaly │ │ Alert │
│ Sniffer │───▶│ Detector │───▶│ System │
└─────────────────┘ └──────────────────┘ └─────────────────┘
│ │ │
▼ ▼ ▼
┌─────────────────┐ ┌──────────────────┐ ┌─────────────────┐
│ Database │ │ Configuration │ │ Logging │
│ Manager │ │ Manager │ │ System │
└─────────────────┘ └──────────────────┘ └─────────────────┘
```

## Core Components

### 1. Packet Sniffer (`src/packet_sniffer.py`)
**Responsibilities:**
- Raw packet capture from network interfaces
- Packet parsing and header extraction
- Protocol identification (TCP, UDP, ICMP)
- Data preprocessing for analysis

**Key Features:**
- Interface-agnostic capture
- Real-time packet processing
- Efficient memory management
- Error handling and recovery

### 2. Anomaly Detector (`src/anomaly_detector.py`)
**Responsibilities:**
- Statistical analysis of network traffic
- Pattern recognition for security threats
- Threshold-based alert triggering
- Behavioral analysis

**Detection Algorithms:**
- **Port Scan Detection**: Rate-based analysis of connection attempts
- **Flood Detection**: Packet volume analysis over time windows
- **Suspicious Activity**: Signature-based port monitoring

### 3. Alert System (`src/alert_system.py`)
**Responsibilities:**
- Multi-channel notification management
- Alert severity classification
- Logging and persistence
- External integration (email, SMS)

**Notification Channels:**
- Console output (real-time)
- File logging (persistent)
- Email alerts (configurable)
- System logs

### 4. Database Manager (`src/database_manager.py`)
**Responsibilities:**
- Data persistence and retrieval
- Schema management
- Query optimization
- Data cleanup and maintenance

**Data Models:**
- Packet records with full metadata
- Alert history with severity levels
- Statistical summaries
- System configuration

## Data Flow

1. **Capture** → Packets captured from network interface
2. **Parse** → Headers extracted and normalized
3. **Analyze** → Statistical and pattern analysis
4. **Detect** → Anomaly identification and classification
5. **Alert** → Notification generation and delivery
6. **Store** → Data persistence for future analysis

## Design Patterns

### Observer Pattern
- Packet processors subscribe to capture events
- Loose coupling between components

### Strategy Pattern
- Pluggable detection algorithms
- Configurable analysis methods

### Factory Pattern
- Flexible packet parsing based on protocol
- Extensible alert generation

## Security Considerations

- **Least Privilege**: Only requires necessary permissions
- **Data Minimization**: Captures only required packet headers
- **Secure Storage**: Local database with access controls
- **Input Validation**: Comprehensive packet validation
