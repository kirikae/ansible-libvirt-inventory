#!/usr/bin/env python

from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

conn = libvirt.open('qemu:///system')

if conn == None:
    print('Failed to connect to hypervisor', file=sys.stderr)
    exit(1)

domains = conn.listAllDomains(0)
if len(domains) == 0:
    print('No Domains found')
else:
    for domain in domains:

        print('DOMAIN: ' + domain.name())
        ifaces = domain.interfaceAddresses(0) # Currently only retieves first IP, not all...
        for (name, val) in ifaces.items():
            if val['addrs']:
                for ipaddr in val['addrs']:
                    if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                        ip4 = ipaddr['addr']
                    elif ipaddr['type'] == ibvirt.VIR_IP_ADDR_TYPE_IPV6:
                        ipv6 = ipaddr['addr']
                    print('IPv4 Address: ' + ip4)
                    #print('IPv6 Address: ' + ip6 # Need a way to ignore ipv6 if no ipv6 address present

conn.close()

