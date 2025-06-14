
"""
This script tests SSH conectivity to a Cisco IOS device using Netmiko. 
-It connects to the device
- Executes the command "show version"
- Prints the output
- Disconnects from the device
"""

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'c1sco_123',
}


connection = ConnectHandler(**device)
output = connection.send_command("show version")
print(output)
connection.disconnect()



