import socket
import uuid
import requests

# Private IP
hostname = socket.gethostname()
private_ip = socket.gethostbyname(hostname)

# Public IP
public_ip = requests.get("https://api.ipify.org").text

# MAC address
mac = uuid.getnode()
mac_address = ':'.join(['{:02x}'.format((mac >> ele) & 0xff)
                        for ele in range(40, -1, -8)])

print("Private IP:", private_ip)
print("Public IP :", public_ip)
print("MAC Addr  :", mac_address)