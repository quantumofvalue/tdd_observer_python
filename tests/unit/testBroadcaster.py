import unittest
from mock import MagicMock

from receiver import Receiver
from broadcaster import Broadcaster

from create_interface_mock import *

# the create_interface_mock(Receiver) below will create the following type
# class ReceiverMock(MagicMock):
#    implements(Receiver)

class BroadcasterTests(unittest.TestCase):
    globals().update(create_interface_mock(Receiver))

    def test_broadcaster_created_without_receivers(self):
        broadcaster = Broadcaster()
        self.assertFalse(broadcaster.has_receivers())

    def test_broadcaster_created_with_a_receiver_registered(self):
        broadcaster = Broadcaster()
        receiver = ReceiverMock()
        broadcaster.register(receiver)
        self.assertTrue(broadcaster.has_receivers())

    def test_receiver_receives_broadcast(self):
        broadcaster = Broadcaster()
        receiver = ReceiverMock()
        broadcaster.register(receiver)
        broadcaster.broadcast()
        receiver.notify.assert_called_with()

    def test_using_zope_interface(self):
        broadcaster = Broadcaster()        
        receiver = ReceiverMock()
        broadcaster.register(receiver)
        broadcaster.broadcast()
        receiver.notify.assert_called_with()
