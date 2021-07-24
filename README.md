# network-scanner


# Working
This network-scanner does basically is , it scans the network and shows how many devices are connected to that network and what is their id address and mac address.

# Requirments
* Linux 
* Scapy

# Steps and Definition
* First, we need to install scapy , So for that put ```pip install scapy``` in the terminal.

* Second, we gonna need to import essential methods from scapy:
``` from scapy.all import ARP, Ether, srp ```

* Third, we gonna need to make an ARP request as shown in the following image:
![alt text](https://www.thepythoncode.com/media/articles/building-network-scanner-using-scapy/arp_request1.jpg)
