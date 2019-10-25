import socket
import time


class Client:
    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        if timeout is None:
            self.timeout = str(int(time.time()))
        else:
            self.timeout = timeout
        self.sock = socket.create_connection((addr, port), self.timeout)
        #self.sock.settimeout(1)
    
    def put(self, name, metric, timestamp=None):
        string = " ".join(["put", name, str(metric), str(timestamp)]) + "\n"
        print(string)
        self.sock.sendall(string.encode("utf8"))
        data = self.sock.recv(1024).decode("utf8")
        if data == "error\nwrong command\n\n":
            raise ClientError
            
    def get(self, key):
        string = " ".join(["get", key]) + "\n"
        self.sock.sendall(string.encode("utf8"))
        data = self.sock.recv(1024).decode("utf8")
        if data == "error\nwrong command\n\n":
            raise ClientError
        elif data == "ok\n\n":
            return dict()
        else:
            data = data[2:].strip().split("\n")
            d = dict()
            for j in data:
                j = j.split(" ")
                if j[0] not in d.keys():
                    d[j[0]] = [(int(j[2]), float(j[1]))]
                else:
                    d[j[0]] = d.get(j[0], []) + [(int(j[2]), float(j[1]))]
            return d


class ClientError(socket.error):
    pass
