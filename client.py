import socket

SERVSET = ('localhost', 5050)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(SERVSET)
    print("Client connected !")
    ### data send ###
    # data = "test"
    # data = data.encode("utf8")
    # client.sendall(data)
    ### data recv ###
    data = client.recv(256)
    print(f"{data.decode()}")

except socket.error as e:
    print(e)
