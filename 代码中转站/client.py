import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect_ex(("192.168.153.1", 8080))

while True:
	data = input("发送的数据：")
	client.send(data.encode("utf-8"))
	response = client.recv(1024)
	print(response.decode("utf-8"))

