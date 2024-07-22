# _       __     __                             ______         ________       
#| |     / /__  / /________  ____ ___  ___     /_  __/___     /_  __/ /_  ___ 
#| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \     / / / __ \     / / / __ \/ _ \
#| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/    / / / /_/ /    / / / / / /  __/
#|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/    /_/  \____/    /_/ /_/ /_/\___/ 
#                                                                             
#    ____  ____  ____  ______   _____ _________    _   ___   _____    __  __
#   / __ \/ __ \/ __ \/_  __/  / ___// ____/   |  / | / / | / /   |  / / / /
#  / /_/ / / / / /_/ / / /     \__ \/ /   / /| | /  |/ /  |/ / /| | / /_/ / 
# / ____/ /_/ / _, _/ / /     ___/ / /___/ ___ |/ /|  / /|  / ___ |/ __  /  
#/_/    \____/_/ |_| /_/     /____/\____/_/  |_/_/ |_/_/ |_/_/  |_/_/ /_/   
#
 
import sys
import socket
import pyfiglet

from pyfiglet import Figlet
banner = Figlet(font='script')
print(banner.renderText('Welcome \n to tha  \n Port Scannah'))

#Enter your target IP
ip = 'xx.xx.xx.xx' 
open_ports =[] 

#Enter your port range
ports = range(1, 65535)


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("No open ports found:(")


                                                                        
