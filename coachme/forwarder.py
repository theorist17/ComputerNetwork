import SocketServer
import threading

class Handler(SocketServer.StreamRequestHandler):

    def handle(self):
        print(self.client_address,'connected')
        self.server.add_client(self.request)
        while 1:
            data = self.request.recv(1024)
            if not data: break
            self.server.send(self.request,data)
        self.server.remove_client(self.request)

class Server(SocketServer.ThreadingTCPServer):

    def __init__(self,*args,**kwargs):
        SocketServer.ThreadingTCPServer.__init__(self,*args,**kwargs)
        self.clients = []
        self.lock = threading.Lock()

    def add_client(self,c):
        with self.lock:
            self.clients.append(c)

    def remove_client(self,c):
        with self.lock:
            self.clients.remove(c)

    def send(self,sender,data):
        with self.lock:
            for c in self.clients:
                if c is not sender:
                    c.sendall(data)

s = Server(('',17171),Handler)
s.serve_forever()
