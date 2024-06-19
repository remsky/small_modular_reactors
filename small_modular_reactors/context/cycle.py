from ..manager.manager import Manager

class Cycle:
    def __init__(self, manager=None):
        self.manager = manager if manager else Manager()

    def handle_message(self, msg):
        return self.manager.handle_message(msg)

    def get_context(self):
        return self.manager.get_context()
