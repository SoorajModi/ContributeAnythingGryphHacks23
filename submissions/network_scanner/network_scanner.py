#Pritesh Gandhi(pgandh05@uoguelph.ca) Lab07

import argparse
from ipaddress import IPv4Network
import random
from scapy.all import *
import socket


def scan_host(ips):

	addr = IPv4Network(ips)
	
	for dp in addr:
		packet = sr1(IP(dst=str(dp))/ICMP(),timeout=2,verbose=0,)
		if packet is None:
			print(f"{dp} is down or not responding.")
		elif (int(packet.getlayer(ICMP).type)==3 and int(packet.getlayer(ICMP).code) in [1,2,3,9,10,13]):
			print(f"{dp} is blocking ICMP.")
		else:
			print(f"{dp} is up.")

def scan_port(ip,port):

	packet_tcp = IP(dst=ip)/TCP(dport=port, flags="S")
	tcp = sr1(packet_tcp, timeout=1, verbose=0)
	if tcp is not None and tcp.haslayer(TCP) and tcp[TCP].flags == "SA":
		print("TCP scan indicates " + str(port) + " on " + str(ip) + " is open")
		
	packet_udp = IP(dst=ip)/UDP(dport=port)
	udp = sr1(packet_udp, timeout=1, verbose=0)
	if udp is not None and udp.haslayer(UDP):
		print("UDP scan indicates " + str(port) + " on " + str(ip) + " is open")


def scan_http_server(ip,port):
	
	http_str = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
	http_bytes = bytes(http_str, "utf-8")
	
	http = IP(dst=ip)/TCP(dport=port)/Raw(load=http_bytes)
	ans = sr1(http, timeout=1, verbose=False)
	if ans and TCP in ans and ans.haslayer(Raw) and "HTTP/1.1" in str(ans[Raw].load):
		print("Found http server on " + str(port) + " on " + str(ip))
	else:
		print("Not Found http server on " + str(port) + " on " + str(ip))


def scan_ftp_server(ip,port):

	ftp = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=1, verbose=0)

	if ftp is None:
		print("Port "+ str(port) +" is closed or filtered.")
	elif ftp.haslayer(TCP) and ftp[TCP].flags & 18 == 18:
		print("Found ftp server on " + str(port) + " on " + str(ip))
	else:
		print("Not Found ftp server on " + str(port) + " on " + str(ip))
	
def is_valid_args(ip,port):
	
	try:
		socket.inet_aton(ip)
		return True
	except socket.error:
		return False

	try:
		port = int(port)
		if port < 1 or port > 65535:
			return False
		else:
			return True
	except ValueError:
		return False
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('-s', action='store', dest='scan_type',
		help='scan type <host|port|http|ftp>', required=True)

	parser.add_argument('-t', action='store', dest='target',
		help='target_ipv4_address:port', required=True)

	parser.add_argument('--version', action='version', version='%(prog)s 1.0')

	args = parser.parse_args()
	
	ip, port = args.target.split(":")
	
	if is_valid_args(ip,port) == False:
		print("Invalid IP or Port!!!")
		exit(0)
	
	if args.scan_type=="host":
		scan_host(ip)
	elif args.scan_type=="port":
		scan_port(ip,int(port))
	elif args.scan_type=="http":
		scan_http_server(ip,int(port))
	elif args.scan_type=="ftp":
		scan_ftp_server(ip,int(port))
	else:
		print("Invalid option!!! Try --help to get the options.")
    #TODO: validate args, call functions, print returned strings

"""
References
[1]https://scapy.readthedocs.io/en/latest/usage.html
[2]https://www.youtube.com/watch?v=4Y-MR-Hec5Y
[3]https://null-byte.wonderhowto.com/how-to/build-stealth-port-scanner-with-scapy-and-python-0164779/

"""
