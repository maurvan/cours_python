from scapy.all import *

target = "192.168.2.225"

el_packet = IP(dst=target) / ICMP()

response = sr1(el_packet, timeout=1)
print(response)

if not response:
    print(f"Host {target} is down")

else:
    print(f"Host {target} is up")
