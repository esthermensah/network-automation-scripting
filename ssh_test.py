
"""
This script tests SSH connectivity to a Linux device using Netmiko. 
-It connects to the device
- Executes the command "show version"
- Prints the output
- Disconnects from the device
"""

from netmiko import ConnectHandler

device = {
    'device_type': 'linux',
    'ip': os.getenv("DEVICE_IP"),
    'username': os.getenv("DEVICE_USER"),
    'password': os.getenv("DEVICE_PASS"),
}


connection = ConnectHandler(**device)
output = connection.send_command("whoami")
print(output)
connection.disconnect()




