
# # source venv/Scripts/activate


import os
import paramiko

ip = os.getenv("DEVICE_IP")
username = os.getenv("DEVICE_USER")
password = os.getenv("DEVICE_PASS")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(ip, username=username, password=password)

# stdin, stdout, stderr = ssh.exec_command('cmd /c echo Hello from Windows')
stdin, stdout, stderr = ssh.exec_command('echo Hello from Windows')

print("Command Output:\n", stdout.read().decode())


ssh.close()









# import os
# from netmiko import ConnectHandler

# """
# This script tests SSH connectivity to a Linux device using Netmiko. 
# -It connects to the device
# - Executes the command "show version"
# - Prints the output
# - Disconnects from the device
# """



# device = {
#     'device_type': 'generic_termserver',
#     'ip': os.getenv("DEVICE_IP"),
#     'username': os.getenv("DEVICE_USER"),
#     'password': os.getenv("DEVICE_PASS"),
#     'session_log': 'debug_output.txt',
#     'global_delay_factor': 2,
# }



# connection = ConnectHandler(**device)
# # output = connection.send_command("whoami", read_timeout=20)
# # output = connection.send_command("echo Hello from SSH", read_timeout=20)
# output = connection.send_command("cmd /c echo Hello from Windows")
# # output = connection.send_command("cmd /c hostname")

# print("Command Output:\n",output)
# connection.disconnect()

