from receiver import Receiver


class Broadcaster(object):

    def __init__(self):
        self._receiver = None

    def register(self, receiver):
        self._receiver = Receiver(receiver)

    def has_receivers(self):
        if self._receiver:
            return True
        else:
            return False

    def broadcast(self):
        self._receiver.notify()
