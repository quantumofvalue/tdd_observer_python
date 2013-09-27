from zope.interface import Interface

class Receiver(Interface):
    def notify():
        """ Each receiver can be notified about an event. """