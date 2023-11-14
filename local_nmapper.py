from icecream import ic
from os.path import isdir
from datetime import date
from os import popen as zsh
from os import system as command
from os.path import isfile as exists
from libnmap.parser import NmapParser, NmapParserException

today = date.today()

command(f"mkdir -p report/{today}")

# commande pour récuperer l'adresse ip via "ip a"
right_line = [rng for rng in zsh("ip a").read().splitlines() if "inet " in rng and "127.0.0.1" not in rng][0]
# right_line = []
# for rng in zsh("ip a").read().splitlines():
#     if "inet " in rng and "127.0.0.1" not in rng:
#         range_ip.append(rng)
range_ip = [l for l in right_line.split(' ') if '/' in l][0]

# au cas ou nmap plante
if not exists(f"report/{today}/network.xml"):
    command(f"nmap -sn -vv {range_ip} -oX report/{today}/network.xml | grep -Fai 'done; ETC'")

network = NmapParser.parse_fromfile(f"report/{today}/network.xml")

# check uniquement les hosts qui sont "up"
for host in network.hosts:
    if host.status == "up":
        if not exists(f"report/{today}/{host.address}.xml"):
            print(f"~~~  Scanning 65535 ports for {host.address}  ~~~")

            command(f"nmap -p- -Pn -vv {host.address} -oX report/{today}/{host.address}.xml | grep -Fai 'done; ETC'")

for host in network.hosts:
    if not exists(f"report/{today}/{host.address}.xml"):
        continue
    
    if not isdir(f"report/{today}/{host.address}"):
        print(f"~~~  Launching script scan for {host.address}  ~~~")

        try:
            result = NmapParser.parse_fromfile(f"report/{today}/{host.address}.xml")
        except NmapParserException:
            print(f"Warning: Incomplete output for {host.address}")
            continue

        if len(result.hosts) == 0:
            print(f"Warning: {host.address} seems down")
            continue

        scan = result.hosts[0]

        if len([port for port in scan.services if port.state == "open"]) == 0:
            continue

        portlst = ",".join([str(port.port) for port in scan.services if port.state == "open"])

        if "9100" in portlst:
            print("No scan printer DUH")
            continue

        command(f"mkdir -p report/{today}/{host.address}")
        ic(portlst)
        command(f"nmap -p {portlst} -vv -A {host.address} -oA report/{today}/{host.address}/nmap_results 2>&1 | grep -Fai 'done; ETC'")
