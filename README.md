# OS-Scanner 🛡️

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Kali Linux](https://img.shields.io/badge/Kali%20Linux-Compatible-black?logo=kali-linux)](https://www.kali.org/)

**Professional Penetration Testing Scanner** for authorized Cybersecurity Professionals. TCP/UDP Port Scanning, Service Detection, OS Fingerprinting with **Nmap Integration**.

## 📋 Table of Contents
- [Features](#-features)
- [Quickstart](#-quickstart)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Output](#-example-output)
- [Requirements](#-requirements)
- [Extensions](#-extensions)
- [Troubleshooting](#-troubleshooting)
- [Legal Notices](#️-legal-notices)
- [License](#-license)

## 🚀 Features
| Feature | Status |
|---------|--------|
| TCP Port Scan (21+ Ports) | ✅ |
| Service Detection | ✅ |
| Hostname Resolution | ✅ |
| Nmap `-sV -sC` Integration | ✅ |
| SMB Null Session Enum | ✅ |
| Local System Info | ✅ |
| Timeout & Error Handling | ✅ |

## ⚡ Quickstart
```bash
# 1. Download
curl -O https://raw.githubusercontent.com/YOUR_USERNAME/os-scanner/main/os_scanner.py

# 2. Run
chmod +x os_scanner.py
python3 os_scanner.py 10.10.10.5

```
## 🛠️ Installation
**Kali Linux / Debian / Ubuntu**

```bash
sudo apt update
sudo apt install python3 nmap smbclient
git clone https://github.com/YOUR_USERNAME/os-scanner.git
cd os-scanner
chmod +x os_scanner.py
```

## 🎯 Usage
```bash
# Hilfe
python3 os_scanner.py --help

# Basis Scan
python3 os_scanner.py 172.105.246.250
python3 os_scanner.py scanme.nmap.org

# Mit lokaler System Info
python3 os_scanner.py 10.10.10.5 --local
```

## 📊 Example Output
```bash
*------------------------------------------*
          TARGET SCAN: 172.105.246.250
          Time: 2026-01-19 14:23:45
*------------------------------------------*
TCP Port Scan (Common Ports)...
  PORT 22/tcp  open  ssh     OpenSSH 8.2p1
  PORT 80/tcp  open  http    Apache 2.4.41
  PORT 443/tcp open  https   Apache 2.4.41

Hostname Resolution...
  Hostname: webserver.example.com

Nmap Scan...
Nmap scan report for webserver.example.com (172.105.246.250)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu (Ubuntu Linux)
80/tcp  open  http     Apache httpd 2.4.41
443/tcp open  https    Apache httpd 2.4.41
```

## ⚠️ Legal Notices
```bash
🔴 ONLY for AUTHORIZED Tests!
🔴 NEVER without written permission!
✅ HackTheBox • TryHackMe • CTFs
✅ Bug Bounty • Red Team Engagements
✅ Own Systems / Lab Environment
```
