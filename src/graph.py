import Peer

class Vertice:
    def __init__(self, peer1, peer2, ping):
        self.peer1 = peer1
        self.peer2 = peer2
        self.ping = ping

class Graph:

    def __init__(self, peers, vertices):
        self.peers = peers
        self.vertices = vertices


