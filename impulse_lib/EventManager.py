from impulse_lib.Listener import Listener


class EventManager:

    def __init__(self):
        self.listeners = []
        print "EventManager Initialized"

    def add_listener(self, listener):
        if isinstance(listener, Listener):
            self.listeners.append(listener)
        else:
            raise TypeError("Expected type 'Listener' for method: add_listener(listener)")

    def debug_listeners(self):
        print self.listeners

    def fire(self, event):
        for listener in self.listeners:
            if listener.event_type == event.event_type:
                listener.run(event)

EventManager = EventManager()
