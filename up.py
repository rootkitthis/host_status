import socket

# Function to check if a server is up and running
def server_up(ip, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Try to connect to the host to see if it is up
            socket.setdefaulttimeout(timeout)
            s.connect((ip, port))
        except (socket.error, ConnectionRefusedError):
            return False
        else:
            return True

# Checks for various servers if they are up and running and prints text in green if up and red if down

def proxmox():
    if server_up("10.10.0.99", 8006) == True:
        print("\033[32mProxmox VM Server is up and running\033[0m")
    else:
        print("\033[31mProx VM Server is down!!!! Please investigate!!!!\033[0m")

def casaos():
    if server_up("10.10.0.25", 80) == True:
        print("\033[32mCasaOS is up and running\033[0m")
    else:
        print("\033[31mCasaOS is down!!!! Please investigate!!!!\033[0m")

def nvr():
    if server_up("10.10.0.649", 80) == True:
        print("\033[32mNVR is up and running\033[0m")
    else:
        print("\033[31mNVR is down!!!!! Please investigate!!!!\033[0m")

def UDM():
    if server_up("10.10.0.1", 80) == True:
        print("\033[32mUDM is up and running\033[0m")
    else:
        print("\033[31mUDM is down!!!!! Please investigate!!!!\033[0m")

def officeap():
    if server_up("10.10.0.254", 8080) == True:
        print("\033[32mOffice AP is up and running\033[0m")
    else:
        print("\033[31mOffice AP is down!!!!! Please investigate!!!!\033[0m")

def LRap():
    if server_up("10.10.0.253", 8080) == True:
        print("\033[32mLiving Room AP is up and running\033[0m")
    else:
        print("\033[31mLiving Room AP is down!!!!! Please investigate!!!!\033[0m")

def printers():
    if server_up("10.10.0.70", 80) == True:
        print("\033[32mEpson XP-4205 is up\033[0m")
    else:
        print("\033[31mEpson XP-4205 is down!!!!! Please investigate!!!!\033[0m")

# Output messages for different categories of devices
print("\nServers:\n")
proxmox()
casaos()
nvr()
print("\n" + "*" * 20 + "\n")
print("Networking Devices:\n")
UDM()
officeap()
LRap()
print("\n" + "*" * 20 + "\n")
print("Printers:\n")
printers()
