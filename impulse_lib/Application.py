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
        raise NotImplementedError("method 'setup' of Application must be overridden.")

    @abstractmethod
    def loop(self):
        raise NotImplementedError("method 'loop' of Application must be overridden.")
