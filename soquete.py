import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("bancocn.com", 80))
client.send(b"hello world")
resposta = client.recv(1024)
print(resposta.decode())