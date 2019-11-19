import asyncio


class ClientServerProtocol(asyncio.Protocol):
    storage = dict()
    
    def connection_made(self, transport):
        self.transport = transport
    
    def data_received(self, data):
        resp = ClientServerProtocol.process_data(data.decode())
        self.transport.write(resp.encode())
    
    @classmethod
    def process_data(cls, data):
        msg = data.strip().split(" ")
        if msg[0] == 'put':
            print("PUT")
            if msg[1] not in cls.storage.keys():
                cls.storage[msg[1]] = list()
            n_e = True
            for _, b in cls.storage[msg[1]]:
                if int(msg[3]) == b:
                    n_e &= False
            if n_e:
                cls.storage[msg[1]].append((msg[2], (int(msg[3]))))
                cls.storage[msg[1]].sort(key=lambda kv:kv[1])
            print(cls.storage)
            return 'ok\n\n'
        elif msg[0] == 'get':
            print("GET")
            if msg[1] == '*':
                string = "ok\n"
                for i in cls.storage.keys():
                    for j in cls.storage[i]:
                        string += " ".join([i, j[0], str(j[1])]) + "\n"
                string += "\n"
                return string
            elif msg[1] not in cls.storage.keys():
                string = "ok\n\n"
                return string
            else:
                string = "ok\n"
                for j in cls.storage[msg[1]]:
                    string += " ".join([msg[1], j[0], str(j[1])]) + "\n"
                string += "\n"
                return string
        else:
            return "error\nwrong command\n\n"    


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server("127.0.0.1", 8889)
