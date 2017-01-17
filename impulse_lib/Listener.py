from abc import abstractmethod, ABCMeta


class Listener:
    __metaclass__ = ABCMeta

    def __init__(self, event_type):
        if isinstance(event_type, str):
            self.event_type = event_type
        else:
            raise TypeError("Expected type 'str' for method: __init__(event_type)")

    @abstractmethod
    def run(self, event):
        pass
