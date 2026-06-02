# Basic Network Sniffer

## Overview

The Basic Network Sniffer is a Python-based cybersecurity project developed using the Scapy library. This application captures and analyzes live network traffic packets, providing detailed insights into network communications and protocol behavior.

The project is designed to help understand packet structures, network protocols, and the flow of data across computer networks. It serves as an educational tool for learning network monitoring and packet analysis fundamentals.

---

## Features

- Capture live network packets in real time
- Analyze Ethernet layer information
- Extract source and destination IP addresses
- Display source and destination MAC addresses
- Identify network protocols such as TCP, UDP, and ICMP
- Display source and destination port numbers
- Analyze packet payload data
- Generate packet summaries
- Monitor network traffic continuously

---

## Technologies Used

- Python
- Scapy
- TCP/IP Networking
- Network Protocol Analysis
- Cybersecurity Fundamentals

---

## Project Structure

```text
CodeAlpha_Network_Sniffer/
│
├── packet_sniffer.py
├── README.md
└── Output
    └── Network Sniffer Output.jpeg

```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/CodeAlpha_Network_Sniffer.git
```

### Navigate to the Project Directory

```bash
cd CodeAlpha_Network_Sniffer
```

### Install Required Dependencies

```bash
pip install scapy
```

---

## Usage

### Windows

Run Command Prompt as Administrator and execute:

```bash
python packet_sniffer.py
```

### Linux / Kali Linux

```bash
sudo python3 packet_sniffer.py
```

---

## Sample Output

```text
============================================================
         NETWORK PACKET CAPTURED
============================================================

[ Ethernet Layer ]

Source MAC Address      : 00:11:22:33:44:55
Destination MAC Address : aa:bb:cc:dd:ee:ff

[ IP Layer ]

Source IP Address       : 192.168.1.10
Destination IP Address  : 142.250.183.14
IP Version              : 4
TTL                     : 128
Protocol                : TCP

[ TCP Layer ]

Source Port             : 50432
Destination Port        : 443

[ Packet Summary ]

Ether / IP / TCP 192.168.1.10:50432 > 142.250.183.14:https
============================================================
```

---

## How It Works

1. Captures packets from the network interface.
2. Extracts Ethernet header information.
3. Analyzes IP header details.
4. Identifies transport layer protocols.
5. Displays packet information in a readable format.
6. Monitors network traffic in real time.

---

## Supported Protocols

- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)
- ICMP (Internet Control Message Protocol)
- IP (Internet Protocol)
- Ethernet

---

## Learning Outcomes

This project provides practical exposure to:

- Packet sniffing techniques
- Network traffic monitoring
- Protocol analysis
- TCP/IP communication
- Ethernet frame analysis
- Cybersecurity fundamentals
- Real-time packet inspection

---

## Future Enhancements

- Graphical User Interface (GUI)
- Packet filtering options
- Export captured packets to PCAP files
- DNS traffic analysis
- HTTP traffic monitoring
- Intrusion detection capabilities
- CSV log export functionality
- Network traffic statistics dashboard

---

## Educational Purpose

This project was developed as part of the CodeAlpha Cyber Security Internship Program to gain practical experience in network monitoring, packet analysis, and cybersecurity concepts.

---

## Disclaimer

This project is intended strictly for educational and authorized environments only.

Do not use this application to monitor networks without proper authorization.

---

## Author

**THIRUKUMARAN S**

Cyber Security Enthusiast | Python Developer

---

## Acknowledgment

This project was completed as part of the **CodeAlpha Cyber Security Internship Program**.

---

## License

This project is intended for educational and learning purposes.
