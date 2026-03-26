# Log Threat Detector

## Overview

This project is a Python-based log analysis and threat detection tool designed to identify suspicious activity in authentication logs. It simulates real-world Security Operations Center (SOC) workflows by detecting patterns such as brute-force attacks and potential account compromise.


## Features

* Detects repeated failed login attempts (brute-force attacks)
* Identifies successful logins following multiple failures
* Flags high-frequency activity from suspicious IP addresses
* Generates structured alert reports with severity levels
* Supports command-line input for flexible log analysis


## Technologies Used

* Python 3
* Regular Expressions (Regex)
* Command-Line Interface (CLI)


## Detection Capabilities

### 🔴 High Severity

* **Brute Force Attack Detection**

  * Flags IPs with excessive failed login attempts

### 🟡 Medium Severity

* **Potential Account Compromise**

  * Detects successful login after multiple failed attempts
* **High Activity IP Detection**

  * Identifies IPs with unusually high login volume


## MITRE ATT&CK Mapping

* **T1110 – Brute Force**

  * Detection of repeated authentication failures


## Project Structure

```
log-threat-detector/
│
├── logs/
│   └── sample.log
├── detector.py
├── alerts.txt
├── README.md
└── requirements.txt
```


## How to Run

### 1. Clone the repository

```
git clone https://github.com/Andrew-Zmolik/log-threat-detector.git
cd log-threat-detector
```

### 2. Run the detector

```
python3 detector.py logs/sample.log
```

### 3. View results

Alerts will be printed in the terminal and saved to:

```
alerts.txt
```


## Sample Output

```
=== Threat Detection Report ===

[HIGH] Brute force suspected from 192.168.1.10 (4 failed attempts)
[MEDIUM] Possible account compromise: admin from 192.168.1.10
```


## Future Improvements

* Real-time log monitoring
* Additional detection rules (e.g., time-based anomalies)
* Integration with SIEM platforms
* Web-based visualization dashboard


## Author

Andrew Zmolik


## License

This project is for educational and demonstration purposes.
