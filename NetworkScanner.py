import scapy.all as scapy 
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", dest="target", help="Target IP / IP Range")
    options = parser.parse_args()
    if not options.target:
        parser.error("[!] Please add an interface to proceed (like : 192.168.1.1/24), --help for more informations.")
    return options

def scan_network(target_ip):                            
   arp_request = scapy.ARP(pdst=target_ip)      # Creating ARP packets.
   broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
   packet = broadcast/arp_request 
   ask_list = scapy.srp(packet, timeout = 3, verbose = False)[0]
   
   packet_list = []
   for i in ask_list:
        packet_dict = {"ip" : i[1].psrc, "mac" : i[1].hwsrc}
        packet_list.append(packet_dict)
        return(packet_list)

print("Available devices in the network:")
print("IP" + " "*18+"MAC")

def print_result(res):
    print(""" __  _ ___ _____ _   _  __  ___ _  __    __   ___ __  __  _ __  _ ___ ___   
|  \| | __|_   _| | | |/__\| _ \ |/ /  /' _/ / _//  \|  \| |  \| | __| _ \  
| | ' | _|  | | | 'V' | \/ | v /   <   `._`.| \_| /\ | | ' | | ' | _|| v /  
|_|\__|___| |_| !_/ \_!\__/|_|_\_|\_\  |___/ \__/_||_|_|\__|_|\__|___|_|_\  """)
    print("=========================================")
    print("IP\t\t\tMAC Address\n=========================================")
    for n in res:
        print(n["ip"] + "\t\t" + n["mac"])

options = get_arguments()
scan_result = scan_network(options.target)
print_result(scan_result)
