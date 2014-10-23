import sys

try:
    import psyco
    psyco.full()
except ImportError:
    pass

class InitializationError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return ('InitializationError: %s' % self.msg)