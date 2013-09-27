from mock import MagicMock
from zope.interface import classImplements
import types

def create_interface_mock(interface_class):
    """Dynamically create a Mock sub class that implements the given Zope interface class."""

    # the init method, automatically specifying the interface methods
    def init(self, *args, **kwargs):
        MagicMock.__init__(self, spec=interface_class.names(),
                      *args, **kwargs)

    # we derive the sub class name from the interface name
    name = interface_class.__name__ + "Mock"

    # create the class object and provide the init method
    klass = types.TypeType(name, (MagicMock, ), {"__init__": init})

    # the new class should implement the interface
    classImplements(klass, interface_class)

    # make the class available to unit tests
    return {name:klass}
    # globals()[name] = klass

