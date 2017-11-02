#!/usr/bin/env python

import socket
import binascii

def ipToInteger(ip_address):
	for version in (socket.AF_INET, socket.AF_INET6):
		try:
			ip_hex = socket.inet_pton(version, ip_address)
			ip_integer = int(binascii.hexlify(ip_hex), 16)

			return ip_integer
		except:
			pass

	raise ValueError("invalid ip address")

def recv_until(conn, str):
	buf = ''
	while not str in buf:
		buf += conn.recv(1)
	return buf

def getValidSubnet(host):
	return host + '/32'

def countHosts(subnet):
	countSubnet = 32 - int(subnet[subnet.find('/')+1:])
	if countSubnet > 0 :
		return str(2 << (countSubnet - 1))
	else :
		return str(2 >> 1)

def isSubnetValid(subnet, host):
	subnetPart = subnet.split('/')
	subnetBinary = long(ipToInteger(subnetPart[0]))
	mask = long(subnetPart[1])
	subnetMask = ''
	for i in range (0, mask):
		subnetMask = subnetMask + '1'
	for i in range (0, 32-mask):
		subnetMask = subnetMask + '0'
	subnetMask = long(subnetMask, 2)
	hostBinary = long(ipToInteger(host))
	andMaskSubnet = str(bin(subnetBinary & subnetMask))
	andMaskHost = str(bin(hostBinary & subnetMask)) 
	if (andMaskHost == andMaskSubnet):
		return 'T'
	else:
		return 'F'
	
TCP_IP = 'hmif.cf'
TCP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = recv_until(s, 'NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

data = recv_until(s, 'Verify NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

print(recv_until(s, '\n')[:-1])

# Phase 1
for i in range(100):
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	recv_until(s, 'Subnet: ')
	s.send(getValidSubnet(host) + '\n')
print(recv_until(s, '\n')[:-1])

# Phase 2
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Number of Hosts: ')
	s.send(countHosts(subnet) + '\n')
print(recv_until(s, '\n')[:-1])

# Phase 3
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	s.send(isSubnetValid(subnet, host) + '\n')
print(recv_until(s, '\n')[:-1])

s.close()