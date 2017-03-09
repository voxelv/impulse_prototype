#!/usr/bin/env python
# from impulse_lib import Application, IntMenu, EventManager as Events
# from impulse_lib.Actions import print_text
# from impulse_lib.Listener import Listener
from impulse_lib import *

do_menu = IntMenu("What would you like to do?", [
    {'text': "Eat a donut", 'action': print_lines, 'args': ("ate a donut",)},
    {'text': "Fly a kite", 'action': print_lines, 'args': ("flew a kite",)},
    {'text': "Create a module", 'action': print_lines, 'args': ("created a module",)},
])


class ImpulsePrototype(Application):
    counter = 0

    def __init__(self):
        super(ImpulsePrototype, self).__init__()

        wow_listener = INIT_Listener()

        EventManager.add_listener(wow_listener)
        EventManager.debug_listeners()

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
