import os
import paramiko
from datetime import datetime

# Define "devices" – for now, just your own laptop with different aliases
devices = [
    {"name": "MyLaptop-1", "ip": os.getenv("DEVICE_IP")},
    {"name": "MyLaptop-2", "ip": os.getenv("DEVICE_IP")}
]

username = os.getenv("DEVICE_USER")
password = os.getenv("DEVICE_PASS")

# Commands to run
commands = [
    "echo Hello from Windows",
    "hostname"
]

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Loop through each "device"
for device in devices:
    print(f"\nConnecting to {device['name']} ({device['ip']})...")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(device["ip"], username=username, password=password)

        log_filename = f"logs/{device['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        with open(log_filename, "w") as log_file:
            for cmd in commands:
                stdin, stdout, stderr = ssh.exec_command(cmd)
                output = stdout.read().decode()
                error = stderr.read().decode()

                # Print and log
                print(f"\n[{device['name']}] $ {cmd}\n{output}")
                log_file.write(f"\n[{device['name']}] $ {cmd}\n{output}")
                if error:
                    print(f"[{device['name']}] Error: {error}")
                    log_file.write(f"[ERROR]: {error}")

        ssh.close()

    except Exception as e:
        print(f"Failed to connect to {device['name']}: {e}")






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

