from abc import ABCMeta, abstractmethod


class Application(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Application, self).__init__()

        self.running = True

    def run(self):
        self.setup()

        while self.running:
            self.loop()

    def done(self):
        self.running = False

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def loop(self):
        pass
