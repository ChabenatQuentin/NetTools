import socket
from errorHandling import ServCreationError
import threading


class ClientHandle(threading.Thread):

    def __init__(self, connexion):
        threading.Thread.__init__(self)
        self.con = connexion

    def run(self):
        ### data recv ###
        # data = self.con.recv(256)
        # data = data.decode("utf8")
        # print(f"{data}")
        ### data sending ###
        data = "test"
        con.sendall(data.encode("utf8"))


SERVSET = ('', 5050)
serv = None

try:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(SERVSET)
except socket.error as e:
    print("Error during server creation.\n")
    raise ServCreationError(e)
except TypeError as e:
    print(e)
else:
    print("Server ready to operate !")
    try:
        while True:
            serv.listen(5)
            con, add = serv.accept()
            print(f"Connection accepted from {add}\nData received:\n")
            ClientHandle(con).start()
    except socket.error as e:
        print(e)
    finally:
        con.close()
        serv.close()
