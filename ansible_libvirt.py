#!/usr/bin/env python

from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

libvirt_uri = 'qemu:///system'

connection = libvirt.open(libvirt_uri)

if connection == None:
    print('Failed to connection.ct to hypervisor', file=sys.stderr)
    exit(1)

domains = connection.listAllDomains(0)
if len(domains) == 0:
    print('No Domains found')
else:
    for domain in domains:

        print("DOMAIN: {0}".format(domain.name()))
        ifaces = domain.interfaceAddresses(0) # Currently only retieves first IP, not all...
        for (name, val) in ifaces.items():
            if val['addrs']:
                for ipaddr in val['addrs']:
                    if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                        ipv4 = ipaddr['addr']
                        if ipv4 != None:
                            print("IPv4 Address: {0}".format(ipv4))
                    elif ipaddr['type'] == ibvirt.VIR_IP_ADDR_TYPE_IPV6:
                        ipv6 = ipaddr['addr']
                        if ipv6 != None:
                            print("IPv6 Address: {0}".format(ipv6))

connection.close()
