from BaseListener import BaseListener


class INIT_Listener(BaseListener):
    def run(self):
        print "RAN INIT LISTENER"

    def __init__(self):
        super(INIT_Listener, self).__init__("INIT")
