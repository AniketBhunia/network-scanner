**Network-scanner** 


# Working
This network-scanner does basically is , it scans the network and shows how many devices are connected to that network and what is their id address and mac address.

# Requirments
* Linux OS
* Scapy

# Steps and Definition
* First, we need to install scapy , So for that put ```pip install scapy``` in the terminal.

* Second, we gonna need to import essential methods from scapy:
``` from scapy.all import ARP, Ether, srp ```

* Third, we gonna need to make an ARP request as shown in the following image:
![alt text](https://www.thepythoncode.com/media/articles/building-network-scanner-using-scapy/arp_request1.jpg)
The network scanner will send the ARP request indicating who has some specific IP address, let's say "192.168.1.1", the owner of that IP address ( the target ) will automatically respond saying that he is "192.168.1.1", with that response, the MAC address will also be included in the packet, this allows us to successfully retrieve all network users' IP and MAC addresses simultaneously when we send a broadcast packet ( sending a packet to all the devices in the network ).

The arp example is like shown in the follwowing image:
![alt text]<img src = "https://www.thepythoncode.com/media/articles/building-network-scanner-using-scapy/hacker.jpg" width = '500'>

So lets create packets:
```
target_ip = "192.168.1.1/24"
# IP Address for the destination
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
```
Now we have created these packets, we need to send them using srp() function which sends and receives packets at layer 2, we set the timeout to 3 so the script won't get stuck:
``` result = srp(packet, timeout=3)[0] ```
Result now is a list of pairs that is of the format (sent_packet, received_packet), let's iterate over them:
``` 
clients = []
for sent, received in result:
     clients.append({'ip': received.psrc, 'mac': received.hwsrc})
```

Now lets Print:
```
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
```

