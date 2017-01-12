#!/usr/bin/env python
from impulse_lib import Application, IntMenu, EventManager as Events
from impulse_lib.Actions import print_text
from impulse_lib.Listener import Listener

do_menu = IntMenu("What would you like to do?", [
    {'text': "Eat a donut", 'action': print_text, 'args': ("ate a donut",)},
    {'text': "Fly a kite", 'action': print_text, 'args': ("flew a kite",)},
    {'text': "Create a module", 'action': print_text, 'args': ("created a module",)},
])


class ImpulsePrototype(Application):
    counter = 0

    def __init__(self):
        super(ImpulsePrototype, self).__init__()

        wow_listener = Listener("INIT")

        Events.add_listener(wow_listener)
        Events.debug_listeners()

        print "Hello world"

    def setup(self):
        print "NOW HEAR THIS! THE APP IS SET UP!"

    def loop(self):
        do_menu.show()

        if self.counter > 9:
            self.done()
        else:
            self.counter += 1

    def done(self):
        super(ImpulsePrototype, self).done()


if __name__ == '__main__':
    app = ImpulsePrototype()
    app.run()
