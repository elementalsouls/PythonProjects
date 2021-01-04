#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
   arp_request = scapy.ARP(pdst=ip )
   broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
   arp_request_broadcast = broadcast/arp_request
   answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
   return answered_list

   print("IP\t\t\tMAC_Address\n----------------------------------------------------------------------")
   for elements in answered_list:
       #print(elements[1].show())
       print(elements[1].psrc + "\t\t" + elements[1].hwsrc)

#Enter the ip address here that you want to scan.
scan("192.168.0.1/24")
