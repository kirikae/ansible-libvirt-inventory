# ansible-libvirt-inventory
Ansible Dynamic Inventory plugin for libvirt (WIP)


NOTE: in development.

End goal is to have an inventory plugin for Ansible to use libvirt (remote or local hypervisor) as an inventory source



## TODO
* variablise the libvirt URI structuring
  * user
  * hostname / ip address (of hypervisor being queried)
* convert to `libvirt.openAuth` when remote hypervisor
* pull more than just the initial IP address out of the domain (VM)
* output in `json` format
* convert to inventory plugin

Reference material for this:
* [libvirt Python API doco](https://libvirt.org/docs/libvirt-appdev-guide-python/en-US/pdf/Version-1.1-Libvirt_Application_Development_Guide_Using_Python-en-US.pdf#%5B%7B%22num%22%3A138%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C53.858%2C730.85095%2Cnull%5D)
* [ansible Inventory Plugin development](https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#developing-an-inventory-plugin)
* [Ansible inventory script development](https://docs.ansible.com/ansible-tower/latest/html/administration/custom_inventory_script.html#writing-inventory-scripts)
