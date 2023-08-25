#we don't have to send data to the server
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.1) 
#method to try a connection - return integer
code = client.connect_ex(("bancocn.com", 80))
#return 0 if the connection is established
print(code)