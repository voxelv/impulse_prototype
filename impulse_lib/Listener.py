

class Listener:
    def __init__(self, event_type):
        if isinstance(event_type, str):
            self.event_type = event_type
        else:
            raise TypeError("Expected type 'str' for method: __init__(event_type)")

    def run(self):
        raise NotImplementedError("Method 'run' must be overriden for a 'Listener' object.")
