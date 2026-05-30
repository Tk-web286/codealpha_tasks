from scapy.all import *

def packet_analyzer(packet):
    print("\n" + "=" * 60)
    print("NETWORK PACKET CAPTURED")
    print("=" * 60)

    if packet.haslayer(Ether):
        print("\n[ Ethernet Layer ]")
        print(f"Source MAC Address      : {packet[Ether].src}")
        print(f"Destination MAC Address : {packet[Ether].dst}")

    if packet.haslayer(IP):
        print("\n[ IP Layer ]")
        print(f"Source IP Address       : {packet[IP].src}")
        print(f"Destination IP Address  : {packet[IP].dst}")
        print(f"IP Version              : {packet[IP].version}")
        print(f"TTL                     : {packet[IP].ttl}")

        protocol_num = packet[IP].proto

        if protocol_num == 1:
            protocol_name = "ICMP"
        elif protocol_num == 6:
            protocol_name = "TCP"
        elif protocol_num == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "OTHER"

        print(f"Protocol                : {protocol_name}")

    if packet.haslayer(TCP):
        print("\n[ TCP Layer ]")
        print(f"Source Port             : {packet[TCP].sport}")
        print(f"Destination Port        : {packet[TCP].dport}")
        print(f"Sequence Number         : {packet[TCP].seq}")
        print(f"Acknowledgment Number   : {packet[TCP].ack}")

    elif packet.haslayer(UDP):
        print("\n[ UDP Layer ]")
        print(f"Source Port             : {packet[UDP].sport}")
        print(f"Destination Port        : {packet[UDP].dport}")

    elif packet.haslayer(ICMP):
        print("\n[ ICMP Layer ]")
        print(f"Type                    : {packet[ICMP].type}")
        print(f"Code                    : {packet[ICMP].code}")

    if packet.haslayer(Raw):
        print("\n[ Payload Data ]")

        try:
            payload = packet[Raw].load.decode(errors='ignore')
            print(payload[:500])

        except:
            print(packet[Raw].load)

    print("\n[ Packet Summary ]")
    print(packet.summary())
    print("=" * 60)

print("\nStarting Packet Sniffer...")
print("Press CTRL + C to Stop.\n")

sniff(prn=packet_analyzer, store=False)
