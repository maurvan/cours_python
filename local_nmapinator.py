import ipaddress
from tqdm import tqdm
from scapy.all import *
from datetime import date
from os import popen as zsh
from os import system as command
from os.path import isfile, isdir
from libnmap.parser import NmapParser, NmapParserException

# defini si le host est up
def isup(target):
    el_packet = IP(dst=target) / ICMP()

    response = sr1(el_packet, timeout=1, verbose=False)

    if not response:
        return False

    else:
        return True

# nous permet d'avoir les ips
def get_range():
    right_line = [rng for rng in zsh("ip a").read().splitlines() if "inet " in rng and "127.0.0.1" not in rng][0]
    range_ip = ipaddress.IPv4Network([l for l in right_line.split(' ') if '/' in l][0], strict=False)
    all_ips = [str(ip_addr) for ip_addr in list(range_ip.hosts())]

    return all_ips

# toutes les mauvaises conditions, sinon ca envoie une liste de ports
def get_port(ip, day):
    if not isfile(f"report/{day}/{ip}.xml"):
        return False

    try:
        result = NmapParser.parse_fromfile(f"report/{day}/{ip}.xml")
    except NmapParserException:
        tqdm.write(f"Warning: Incomplete output for {ip}")
        return False
    
    if len(result.hosts) == 0:
        tqdm.write(f"Warning: {ip} seems down")
        return False

    scan = result.hosts[0]
    if len([port for port in scan.services if port.state == "open"]) == 0:
        tqdm.write(f"Warning: No open port on {ip}")
        return False

    portlst = ",".join([str(port.port) for port in scan.services if port.state == "open"])
    if "9100" in portlst:
        tqdm.write("No scan printer you fool !!!!!!!!1!!")
        return False

    return portlst

def main():
    today = date.today()
    command(f"mkdir -p report/{today}")
    network = get_range()

    for host in tqdm(network, unit="hosts"):
        if isdir(f"report/{today}/{host}"):
            continue

        if not isup(host):
            continue

        if not isfile(f"report/{today}/{host}.xml"):
            tqdm.write(f"~~~  Scanning 65535 ports for {host}  ~~~")

            command(f"sudo nmap -p- -Pn -vv {host} -oX report/{today}/{host}.xml | grep 'done;'")

        ports = get_port(host, today)

        if not ports:
            tqdm.write("Error: host either crashed/has no open port/is a printer")
            continue

        tqdm.write(f"~~~  Launching script scan for {host}  ~~~")

        command(f"mkdir -p report/{today}/{host}")
        command(f"nmap -p {ports} -Pn -vv -A {host} -oA report/{today}/{host}/nmap_results 2>&1 | grep 'done;'")

main()
