# SYN Flood DOS Attack Script

This script demonstrates how to perform a SYN flood attack using Python and the Scapy library. A SYN flood attack is a type of Denial of Service (DoS) attack that aims to overwhelm a target system by sending a large number of SYN packets.

Note: This script is intended for educational purposes only. Performing a SYN flood attack without authorization is illegal and unethical. Use this script responsibly and only on systems you own or have explicit permission to test.


## Prerequisites
• Python 3 <br>
• Scapy library <br>
• Installation <br>


## Clone this repository:
**git clone https://github.com/dhananjay-c/dhananjay-c-SYN-Flood-DOS-Attack-Script.git** <br>
**cd syn-flood-script**


## Install the required Python packages:
**pip install scapy**


## Usage
**python syn_flood_ddos.py <target_ip> <target_port> [-c COUNT] [-i INTERVAL]**

• <target_ip>: Target IP address<br>
• <target_port>: Target port number<br>
• -c COUNT, --count COUNT: Number of packets to send (default: 1000)<br>
• -i INTERVAL, --interval INTERVAL: Interval between packets in seconds (default: 0.01)<br>


## Example
To send 500 SYN packets to 192.168.1.10 on port 80 with an interval of 0.05 seconds:
**python syn_flood_ddos.py 192.168.1.10 80 -c 500 -i 0.05**


## Disclaimer
This script is for educational purposes only. Unauthorized use of this script to attack systems without permission is illegal and unethical. The author is not responsible for any misuse or damage caused by this script. Always obtain proper authorization before conducting any security testing.
